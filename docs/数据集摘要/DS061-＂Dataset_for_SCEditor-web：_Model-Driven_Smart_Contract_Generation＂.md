# DS061 Dataset for SCEditor-web: Model-Driven Smart Contract Generation

- 收录范围：仅纳入作者公开的生成合约 Slither 评估子集，覆盖 4 个模型各生成的 3 份合约。
- 数据量：12 条文件评估记录，对应 12 份独立 `.sol` 文件，共 93 条 Slither 检测项（High 6 条、Medium 4 条、Low 11 条、Informational 41 条、Optimization 31 条）。
- 标签形式与来源：Slither 输出检测规则 `check`（15 种）、影响等级 `impact`、置信度 `confidence` 和描述 `description`，其中信息项及优化项也计入总数。
- 标签对象：每条检测项关联一份受评估源码，`elements` 可指向函数、变量或控制流节点，`source_mapping.lines` 给出相应源码行号。
- 依据：固定版发布文件实测，按公开评估仓库提交 `c6d1f56` 中各文件的 `slither_output.results.detectors` 计数。受限 DataPort 全包的独立源码数未知。 [登记说明](https://api.datacite.org/dois/10.21227/pa8k-9m69) · [评估源码目录](https://github.com/YassineDev91/smart-contract-eval/tree/c6d1f560e8a5ad64033c45f151d4736be90b8d74/contracts-evaluation) · [完整报告](https://github.com/YassineDev91/smart-contract-eval/blob/c6d1f560e8a5ad64033c45f151d4736be90b8d74/analysis_reports/full_analysis_report.json)
