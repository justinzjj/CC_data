# DS083 How are Solidity smart contracts tested in open source projects? An exploratory study

- 收录范围：仅纳入工作簿 `audit_reports` 索引中能从正文核实具体发现的审计报告。
- 数据量：至少 10 份报告；工作簿中有 0 份独立合约源码文件，外部报告所涉源码数未知；至少 100 项发现。
- 标签形式与来源：标签来自审计团队的报告正文。Balancer 逐项给出标题、类别、严重度、目标和文字描述，PeckShield 用 PVE 编号区分发现。
- 标签对象：标签直接赋给一项审计发现，可通过正文定位受影响的文件或函数，如 Balancer 第 10 项指向 `joinPool` 和 `exitPool`。工作簿仅以 `project/file` 关联项目与报告。
- 依据：本地实测索引，发现数按发布方报告核实下限。按报告去重，Balancer 1 份含 15 项，PeckShield 9 份含 85 项；部分索引路径失效，总量未知。 [audit_reports 索引](../../data/raw_data/DS083_How_are_Solidity_smart_contracts_tested_in_open_source_/solidity_sc_testing_data.xlsx) · [Balancer 原报告](https://github.com/balancer-labs/balancer-core/blob/master/Trail%20of%20Bits%20Full%20Audit.pdf) · [Keep3r 原报告](https://github.com/keep3r-network/keep3r.network/blob/HEAD/audits/PeckShield-Audit-Report-Keep3r-v1.0.pdf)
