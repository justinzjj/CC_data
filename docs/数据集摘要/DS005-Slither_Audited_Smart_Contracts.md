# DS005 Slither Audited Smart Contracts

- 收录范围：纳入按部署地址关联的 Etherscan 已验证 Solidity 源码、字节码及 Slither 静态检测结果。
- 数据量：120,608 条部署地址记录；独立源码文件 0 份，源码内嵌于 Parquet 的 `source_code` 列；85,478 个地址共 203,764 条检测项，另有 35,130 个地址检测成功且无告警。
- 标签形式与来源：Slither 自动生成 `check`、`impact`、`confidence`，如 `uninitialized-state / High / High`。全量多标签配置用编号序列表示 38 类检测项及 `safe`；`safe` 表示工具无告警。
- 标签对象：检测项直接标在部署地址对应的合约上，原始分片未提供函数、文件或源码行位置。
- 依据：本地实测。提交 `1359410` 的 9 个原始分片按地址计数；big、small 及不同标签表示均取自同一底表。 [原始分片](../../data/raw_data/DS005_Slither_Audited/data/raw) · [配置与切分](../../data/raw_data/DS005_Slither_Audited/dataset_infos.json) · [检测器映射](../../data/raw_data/DS005_Slither_Audited/data/label_mappings.json)
