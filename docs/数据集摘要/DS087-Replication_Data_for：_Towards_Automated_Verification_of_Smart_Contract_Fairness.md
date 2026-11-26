# DS087 Replication Data for: Towards Automated Verification of Smart Contract Fairness

- 收录范围：仅收录 FairCon 在拍卖、投票或性能实验中至少检出一项公平性违反的合约用例。
- 数据量：28 个合约用例（拍卖 12、性能变体 7、R 投票 5、0–1 投票 4），对应 103 份按属性准备的 .sol 源码（按内容去重为 102 份），共 86 个“用例 × 属性”违反标记。
- 标签形式与来源：FairCon 输出 `truth_violate`、`collusion_violate`、`optimal_violate`、`efficient_violate` 等属性字段。1 表示本次检出违反，0 表示本次未检出；同一用例的同一属性只要有一次取 1 即计入。
- 标签对象：标记对应特定模型设置下具名合约的受检属性。按 `name` 定位文件，部分文件名含部署地址。28 个用例涉及 24 个不同文件名。
- 依据：本地实测，Dataverse v1.3。按四张分组原始运行表的模型设置、源码名及属性汇总。0–1 投票的 4 个效率违反在汇总表中均为 0，采用原始运行值。 [原始实验表](../../data/raw_data/DS087_Replication_Data_for_Towards_Automated_Verification_of_/faircon_data/faircon_dataset/faircon_results/raw) · [0–1 投票汇总](../../data/raw_data/DS087_Replication_Data_for_Towards_Automated_Verification_of_/faircon_data/faircon_dataset/faircon_results/summary_voting-0-1.csv) · [用例与目录说明](../../data/raw_data/DS087_Replication_Data_for_Towards_Automated_Verification_of_/README.md)
