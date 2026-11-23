"""Import the local catalogue snapshot. Run with Python and openpyxl."""
import csv
import io
import json
import re
import subprocess
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw_data"
STATUS = {
    "完整下载": "succeeded", "部分或仅样本": "partial", "受限": "restricted",
    "下载失败": "failed", "集合已核对": "reviewed",
}


def read_records():
    with (RAW / "_manifest.csv").open(encoding="utf-8-sig", newline="") as f:
        manifest = list(csv.DictReader(f))
    book = load_workbook(ROOT / "docs/区块链数据集基础表.xlsx", read_only=True, data_only=True)
    rows = list(book["数据集基础表"].values)[1:]
    book.close()
    details = {r[0]: r for r in rows}
    if len(details) != len(rows) or set(details) != {m["编号"] for m in manifest}:
        raise ValueError("Workbook and manifest IDs disagree")
    summaries = {}
    for line in (ROOT / "docs/数据集摘要.md").read_text().splitlines():
        if line.startswith("| [DS"):
            cells = line.strip("| ").split(" | ")
            code = re.match(r"\[(DS\d+)", cells[0])[1]
            summaries[code] = cells[3].split("<br>")[0]

    for m in manifest:
        code = m["编号"]
        _, _, publication, tags, coverage, _, note = details[code]
        path = ROOT / m["本地路径"] if m["本地路径"] else None
        if path and not path.is_dir():
            raise FileNotFoundError(path)
        description = summaries.get(code, m["标签来源及定位粒度"] or note)
        dates = re.search(r"(\d{4}-\d{2}-\d{2})\s*(?:至|到|～|—)\s*(\d{4}-\d{2}-\d{2})",
                          (coverage or "") + " " + (description or ""))
        sources = re.findall(r"https?://[^\s|]+", m["发布来源"])
        yield dict(code=code, name=m["名称"], source=sources[0] if sources else None,
                   tags={"对象": tags.split("；")}, publication=publication, coverage=coverage,
                   published=publication if re.fullmatch(r"\d{4}-\d{2}-\d{2}", publication or "") else None,
                   start=dates[1] if dates else None, end=dates[2] if dates else None,
                   description=description, path=str(path) if path else None,
                   status=STATUS[m["状态"]], size=int(m["字节数"]), manifest=m)


def main():
    data = io.StringIO()
    writer = csv.writer(data, lineterminator="\n")
    for record in read_records():
        writer.writerow([json.dumps(record, ensure_ascii=False)])
    sql = """BEGIN;
CREATE TEMP TABLE incoming (r jsonb) ON COMMIT DROP;
COPY incoming FROM STDIN WITH (FORMAT csv);
""" + data.getvalue() + r"""\.
INSERT INTO datasets(catalog_code, name, source_url)
SELECT r->>'code', r->>'name', r->>'source' FROM incoming ORDER BY r->>'code'
ON CONFLICT (catalog_code) DO UPDATE SET name=excluded.name, source_url=excluded.source_url;
CREATE TEMP VIEW mapped AS SELECT id, r FROM incoming JOIN datasets ON catalog_code=r->>'code';
INSERT INTO dataset_info(dataset_id, tags, published_on, publication_note, coverage_start,
                         coverage_end, coverage_note, description)
SELECT id, r->'tags', (r->>'published')::date, r->>'publication', (r->>'start')::date,
       (r->>'end')::date, r->>'coverage', r->>'description' FROM mapped
ON CONFLICT (dataset_id) DO UPDATE SET
    (tags,published_on,publication_note,coverage_start,coverage_end,coverage_note,description)=
    (excluded.tags,excluded.published_on,excluded.publication_note,excluded.coverage_start,
     excluded.coverage_end,excluded.coverage_note,excluded.description);
INSERT INTO dataset_downloads(dataset_id, import_source, status, downloaded_bytes, total_bytes,
                              local_path, error_message, source_record)
SELECT id, '_manifest.csv', r->>'status', (r->>'size')::bigint,
       CASE WHEN r->>'status'='succeeded' THEN (r->>'size')::bigint END, r->>'path',
       CASE WHEN r->>'status' IN ('partial','failed','restricted')
            THEN nullif(r->'manifest'->>'覆盖与未完成原因','') END, r->'manifest' FROM mapped
ON CONFLICT (dataset_id, import_source) DO UPDATE SET
    (status,downloaded_bytes,total_bytes,local_path,error_message,source_record)=
    (excluded.status,excluded.downloaded_bytes,excluded.total_bytes,excluded.local_path,
     excluded.error_message,excluded.source_record);
COMMIT;
"""
    subprocess.run(["docker", "compose", "exec", "-T", "postgres", "psql", "-X",
                    "-v", "ON_ERROR_STOP=1", "-U", "cc_data", "-d", "cc_data"],
                   cwd=ROOT, input=sql, text=True, check=True)


if __name__ == "__main__":
    main()
