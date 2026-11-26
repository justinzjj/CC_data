# DS112 smart-contract-intent-vul-dataset

- 收录范围：仅收录 `vulnerabilities` 子表及其通过 `ContractId` 关联的合约，用于识别时间戳依赖、重入等八类问题。
- 数据量：4,029 条子表合约记录，独立源码文件 0 份，对应源码均内嵌于 SQL 的 `contracts.SourceCode`。其中 717 条各有 1 个结构化漏洞类别标签，共列出 814 个名称引用；360 条另附详情与修复说明。
- 标签形式与来源：发布方以 `Vulnerability` JSON 保存“漏洞名 → 名称列表”，如 `{"timestamp dependency":["NXX"]}`。逐条标注的人审或工具来源未知。其余 3,312 条仅有目录和文件线索，`Vulnerability`、`Detail`、`Repair` 均为 NULL，属于缺标。
- 标签对象：每个结构化标签对应一个 `ContractId`，`File` 给出文件路径，名称列表可指向源码中的具名合约。部分 `Detail` 文本进一步指出函数及代码片段。
- 依据：本地实测，提交 `fb4e7998`。按唯一 `ContractId` 连接源码并统计非空 JSON。区块号依赖在本地有 114 条非空标注，发布方数据卡列 116 条。 [SQL 导出](../../data/raw_data/DS112_smart-contract-intent-vul-dataset/web3_all.sql) · [该版本数据卡](https://huggingface.co/datasets/web3se/smart-contract-intent-vul-dataset/blob/fb4e7998333be14f7c56f7e8b3b5370bc127efc6/README.md)
