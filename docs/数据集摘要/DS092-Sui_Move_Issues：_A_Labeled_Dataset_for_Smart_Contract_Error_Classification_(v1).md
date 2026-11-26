# DS092 Sui Move Issues: A Labeled Dataset for Smart Contract Error Classification (v1)

- 收录范围：仅纳入主类别为 `SecurityError` 的 Sui Move 代码片段，用于安全问题分类。
- 数据量：SecurityError 子集数量未知，独立合约源码文件数、类别标注数及修复建议条数均未知。发布方报告全包有 3,321 条去重代码片段，覆盖 5 个主类别。
- 标签形式与来源：研究团队发布的 `label` 给出主类别（入选值为 `SecurityError`）及可选细分类别，`output` 存放人工撰写的修复建议。发布说明未披露逐例分类方法。
- 标签对象：类别和修复建议关联同一条记录的 `code` 片段，发布方列出的字段未提供函数或行号定位。
- 依据：发布方报告（Zenodo v1），文件禁运，公开说明仅披露全包规模。 [发布记录及字段定义](https://zenodo.org/records/19682589) · [发布方登记的字段说明](https://api.datacite.org/dois/10.5281/zenodo.19682589)
