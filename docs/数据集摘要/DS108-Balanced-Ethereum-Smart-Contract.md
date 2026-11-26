# DS108 Balanced-Ethereum-Smart-Contract

- 收录范围：仅纳入已取得的 SB_Curate 非平衡版和平衡版，用于 Solidity 合约漏洞类别预测。
- 数据量：非平衡版 143 条记录、平衡版 520 条记录（每类 52 条），两版去重并集为 143 对源码与类别。两版共 0 份独立源码文件（源码内嵌于 JSON 的 `X` 字段），分别有 143 个、520 个类别标注。
- 标签形式与来源：发布者整理 SB_Curate 并过采样生成平衡版。`y` 为单个类别字符串，取值包括 `reentrancy`、`access_control`、`arithmetic`、`bad_randomness`、`denial_of_service`、`front_running`、`other`、`short_addresses`、`time_manipulation`、`unchecked_low_level_calls`。
- 标签对象：每个 `y` 关联整段 `X` 源码；两版源码均含 `@vulnerable_at_lines` 注释，非平衡版引用 222 个行号，平衡版重复采样后累计引用 957 次。
- 依据：本地实测固定提交 `1ef3e5a1` 的两份 JSON，按完整 `(X, y)` 去重，两版得到相同的 143 对。全包未完整下载。 [非平衡 JSON](../../data/raw_data/DS108_Balanced-Ethereum-Smart-Contract/SB_Curate_Imbalanced.json) · [平衡 JSON](../../data/raw_data/DS108_Balanced-Ethereum-Smart-Contract/SB_Curate_Balanced.json) · [发布方数据卡](https://huggingface.co/datasets/Thi-Thu-Huong/Balanced-Ethereum-Smart-Contract/blob/1ef3e5a1e9909669a9d8defa443e6a44c9cb54ef/README.md)
