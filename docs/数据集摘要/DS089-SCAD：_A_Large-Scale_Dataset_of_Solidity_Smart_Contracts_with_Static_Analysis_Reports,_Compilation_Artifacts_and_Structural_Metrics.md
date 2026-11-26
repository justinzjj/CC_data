# DS089 SCAD: A Large-Scale Dataset of Solidity Smart Contracts with Static Analysis Reports, Compilation Artifacts and Structural Metrics

- 收录范围：收录至少含一条 High、Medium 或 Low 影响告警的 Slither 分析报告及对应源码。
- 数据量：221,995 份符合筛选条件的报告，对应 221,995 份独立 `.sol` 源码文件，共 2,594,866 条高、中或低影响的工具告警。
- 标签形式与来源：Slither 按检测器分组给出每条告警的 ID 和文字说明，并标注 `Impact` 和 `Confidence`。例如 `controlled-delegatecall` 在 UserWallet 报告中标为 High 影响、Medium 置信度。
- 标签对象：每条告警指向一份源码中的检测对象，可定位到合约、函数、变量及一处或多处行范围。例如 UserWallet 的告警指向 `sweep` 函数第 85–89 行及其中的第 88 行。
- 依据：本地实测，从 1.0.0 版全包的 286,638 份报告中，按源码路径对 56 个高、中或低影响检测器的计数求和，保留和大于零者。 [检测器计数表](../../data/raw_data/DS089_SCAD_A_Large-Scale_Dataset_of_Solidity_Smart_Contracts_/stats/slither_issue_counts.csv) · [报告格式及 Impact](../../data/raw_data/DS089_SCAD_A_Large-Scale_Dataset_of_Solidity_Smart_Contracts_/analysis/0-1-0x84dabbb8999f508ce1cbb7057d260c74c6c9815c-UserWallet-v0.4.11.sol-slither-v110.md)
