# DS076 DataSet: Empirical study of the smart contract evolution based standard upgradability methods used in Blockchain

- 收录范围：仅纳入 Raw Data 中工具列为 Slither 的升级合约版本安全测量。
- 数据量：148 条合约版本测量记录，0 份独立源码文件（Excel 无源码正文），148 组严重度计数。其中 136 条测量报告问题，按原行累计 3,642 次（低 2,206 次、中 1,021 次、高 415 次）。
- 标签形式与来源：Slither 工具检测。三个 `Security-(severity …)` 字段分别记录低、中、高严重度的问题数，`Security -Number of issue` 记录总数。0 表示该次测量未报告问题。
- 标签对象：每组计数赋给一行 `Contract ID`、`Project`、`Version` 标识的测量。相同地址和版本可重复测量，表中无逐项发现、函数或行号，去重后的发现数未知。
- 依据：本地实测 Mendeley Data v1 的 Raw Data 工作表，筛选工具名 Slither（忽略大小写），按测量行累加严重度列。 [Raw Data 工作表](../../data/raw_data/DS076_DataSet_Empirical_study_of_the_smart_contract_evolution/Dataset_smart_contract_evolution.xlsx)
