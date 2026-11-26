# DS075 DATASET-BASED-EVIDENCE OF THE MEASUREMENTS OF SECURITY CODE METRIC APPLICABLE TO SMART CONTRACT ON 146 DEPLOYED ETHEREUM SMAR CONTRACT

- 收录范围：收录以太坊主网合约度量表中 Slither 给出的合约级问题总数。
- 数据量：146 条按主网地址记录的合约度量，独立合约源码文件 0 份（DOCX 只列源码文件名）。146 个合约级计数合计 8,276 项工具问题，其中 145 个合约的计数大于零。
- 标签形式与来源：`Sum of all issue` 是 Slither 自动检测的问题数，取值为 0 至 612 的整数。1 个合约为 0，表示该次检测无告警。
- 标签对象：每个计数归属 `SolidityFile` 中以地址命名的整份合约文件。文档未列逐项问题、类别、函数或源码行。
- 依据：本地实测，按 Mendeley v1 的 DOCX 主表逐行核对地址文件名和问题总数列。 [原始表格与工具说明](../../data/raw_data/DS075_DATASET-BASED-EVIDENCE_OF_THE_MEASUREMENTS_OF_SECURITY_/DATASET_SECOND_CONT.docx)
