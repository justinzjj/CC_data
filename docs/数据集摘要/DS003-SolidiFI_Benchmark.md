# DS003 SolidiFI Benchmark

- 收录范围：收录 SolidiFI 在 Solidity 合约中注入七类缺陷后生成的变体及其注入日志。
- 数据量：350 份合约变体（每类 50 份），对应 350 份独立 `.sol` 源码文件和 9,369 条注入标注。七类变体复用基础合约。
- 标签形式与来源：标签由 SolidiFI 注入时生成。`bug type` 记录漏洞类别（如重入、时间戳依赖，原始拼写有变体），`approach` 记录注入方式：9,364 条为 `code snippet injection`，5 条为 `weakening security`。
- 标签对象：每条标注指向同类别、同编号的变体文件，`loc` 和 `length` 给出注入起始行和长度。一份源码可有多处注入。
- 依据：本地实测，按类别目录和合约编号配对 350 份源码与 BugLog，统计 CSV 数据行。 [本地配对数据](../../data/raw_data/DS003_SolidiFI/buggy_contracts) · [注入日志](../../data/raw_data/DS003_SolidiFI/buggy_contracts/Re-entrancy/BugLog_1.csv) · [固定版说明](https://github.com/DependableSystemsLab/SolidiFI-benchmark/blob/4b0573e1b3f7031396de6f48f7f3e7380222ad3a/README.md)
