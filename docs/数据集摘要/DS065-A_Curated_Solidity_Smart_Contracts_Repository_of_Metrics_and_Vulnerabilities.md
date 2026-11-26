# DS065 A Curated Solidity Smart Contracts Repository of Metrics and Vulnerabilities

- 收录范围：纳入 SmarthER 对主网 Solidity 源码成功完成的 Slither 检测报告及相关告警。
- 数据量：14,494 份成功检测报告，对应 14,430 份独立 `.sol` 源码；其中 14,456 份报告有告警（对应 14,392 份源码），共 634,808 条检测器告警，另有 38 份报告无告警。CSV 另列 1,409,040 条程序元素记录，一条告警可涉及多个元素。
- 标签形式与来源：Slither 自动生成告警。`Check` 标识检测项，`Impact` 取 High、Medium、Low、Informational 或 Optimization，`Confidence` 取 High 或 Medium。无告警仅表示该次检测未报问题。
- 标签对象：每条告警关联被分析的合约文件；CSV 的 `Type`、`Name` 标识函数、变量或语句节点等元素，`Lines` 给出对应行号。
- 依据：本地实测（Zenodo 11075555）。文件主名相同或同地址唯一时配对源码，按源码与报告内容哈希去重。全部 28,274 份去重报告匹配 28,210 份源码，此范围含失败和不可解析的报告。 [原始报告](../../data/raw_data/DS065_A_Curated_Solidity_Smart_Contracts_Repository_of_Metric/SmarthER/SmarthER/Report/Vulnearbility%20Reports) · [CSV 字段及记录](../../data/raw_data/DS065_A_Curated_Solidity_Smart_Contracts_Repository_of_Metric/SmarthER/SmarthER/Report/CSVVulnerabilityReport/33VulnerabilityReport.csv) · [发布源码](../../data/raw_data/DS065_A_Curated_Solidity_Smart_Contracts_Repository_of_Metric/SmarthER/SmarthER/mainnet)
