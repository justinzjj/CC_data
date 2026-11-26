# DS042 BCCC-VulSCs-2023

- 收录范围：以太坊合约安全／脆弱二分类，纳入 Secure、Vulnerable 两张特征表及其对应的 Solidity 源码。
- 数据量：36,670 个合约（安全 26,914 个、脆弱 9,756 个），36,670 份独立 `.sol` 文件。两表共 36,671 条标签记录（安全 26,915 条、脆弱 9,756 条），按 `hash_id` 去重为 36,670 个合约标签。
- 标签形式与来源：发布方汇集 SmartBugs 与 ESCs 数据，以整数 `label` 表示安全 0／脆弱 1。CSV 未提供逐例判定依据。
- 标签对象：每行标签赋给整个合约，通过 `hash_id` 对应同名源码文件，无函数或行号字段。
- 依据：本地实测 Kaggle v1 两张 CSV 与源码目录。安全表有一个 `hash_id` 出现两次。 [安全表](../../data/raw_data/DS042_BCCC_VulSCs_2023/bccc-vulscs-2023/BCCC-VolSCs-2023_Secure.csv) · [脆弱表](../../data/raw_data/DS042_BCCC_VulSCs_2023/bccc-vulscs-2023/BCCC-VolSCs-2023_Vulnerable.csv) · [作者论文 §6.1.2](https://doi.org/10.1016/j.bcra.2023.100171)
