BEGIN;
CREATE TABLE datasets (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    catalog_code text UNIQUE,
    name text NOT NULL CHECK (btrim(name) <> ''),
    source_url text,
    created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE dataset_info (
    dataset_id bigint PRIMARY KEY REFERENCES datasets(id),
    tags jsonb NOT NULL DEFAULT '{}' CHECK (jsonb_typeof(tags) = 'object'),
    published_on date,
    publication_note text,
    coverage_start date,
    coverage_end date,
    coverage_note text,
    description text,
    CHECK (coverage_end >= coverage_start)
);
CREATE TABLE dataset_downloads (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    dataset_id bigint NOT NULL REFERENCES datasets(id),
    import_source text,
    download_url text,
    status text NOT NULL CHECK (status IN
      ('pending','running','succeeded','partial','restricted','failed','cancelled','reviewed')),
    downloaded_bytes bigint NOT NULL DEFAULT 0 CHECK (downloaded_bytes >= 0),
    total_bytes bigint CHECK (total_bytes >= downloaded_bytes),
    progress_pct numeric(5,2) GENERATED ALWAYS AS
      (CASE WHEN status = 'succeeded' THEN 100
            ELSE round(100.0 * downloaded_bytes / nullif(total_bytes, 0), 2) END) STORED,
    local_path text CHECK (local_path LIKE '/%'),
    error_message text,
    source_record jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    started_at timestamptz,
    finished_at timestamptz,
    UNIQUE (dataset_id, import_source)
);
CREATE INDEX dataset_downloads_latest ON dataset_downloads(dataset_id, created_at DESC, id DESC);
COMMIT;
