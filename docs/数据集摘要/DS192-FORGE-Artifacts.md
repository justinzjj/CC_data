# DS192 FORGE-Artifacts

- 收录范围：收录从项目安全审计报告提取的发现及关联项目源码，人工整理版另列于 DS193。
- 数据量：本地 27,495 条审计发现，直接涉及的独立源码文件数未知。共 27,495 条发现标注，其中 27,433 条含非空 CWE 分类。项目树含 78,224 份 Solidity 文件，包括依赖、接口和测试。
- 标签形式与来源：发现来自项目安全审计，FORGE 用大模型提取标题、描述、严重度和位置，并赋予分层 CWE 编号。`severity` 取 critical、high、medium、low、info 或 n/a。
- 标签对象：严重度与 CWE 赋给报告中的单条发现。`location` 为自由文本，可指向合约、函数、文件或源码行。
- 依据：本地实测，提交 `76b75824`，部分下载。累计 6,454 份结果 JSON 的 `findings` 数组（1,142 份为空）。发布方报告 27,497 条发现、项目树内 81,390 份 Solidity 文件。 [发布统计](../../data/raw_data/DS192_FORGE-Artifacts/README.md) · [报告结果](../../data/raw_data/DS192_FORGE-Artifacts/dataset/results) · [单份审计记录](../../data/raw_data/DS192_FORGE-Artifacts/dataset/results/Pandora%20Finance%20Smart%20Contract%20Audit%20Report%20-%20QuillAudits.pdf.json) · [项目代码](../../data/raw_data/DS192_FORGE-Artifacts/dataset/contracts)
