# DS059 Solidity 函数级漏洞严重性分类集

- 收录范围：Solidity 函数和代码片段的漏洞严重度分类，含审计发现及已审计的对照函数。
- 数据量：2,910 条函数或片段记录（1,972 条有漏洞严重度，938 条为对照），独立合约源码文件 0 份，代码内嵌于 Parquet。共 2,910 个严重度标签。
- 标签形式与来源：`severity` 取 high（588 条）、medium（1,010 条）、low（374 条）或 none（938 条）。前三类来自五家审计机构，none 是发布方从 Etherscan 收集的已审计无漏洞对照。
- 标签对象：每个标签对应一条 `function` 代码文本，部分片段上下文不完整。分片未提供合约 ID 或源码行号。
- 依据：本地实测，提交 `59d909ca`。训练集 2,473 条、测试集 437 条。按 `function` 原文去重为 2,577 段，其中 64 段跨切分重复，9 段在全表有多个严重度。 [训练分片](../../data/raw_data/DS059_Solidity_Function_Severity/data/train-00000-of-00001.parquet) · [测试分片](../../data/raw_data/DS059_Solidity_Function_Severity/data/test-00000-of-00001.parquet) · [该版本数据卡](https://huggingface.co/datasets/msc-smart-contract-auditing/vulnerability-severity-classification/blob/59d909ca5a3441c7ab673cffab4a06b5ffa07779/README.md)
