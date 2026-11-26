# DS140 solidity-findings

- 收录范围：收录 `default/train` 中 Slither 和 Mythril 输出的静态分析发现。
- 数据量：69,228 条发现记录，独立合约源码文件 0 份（55,874 条记录在 Parquet 的 `snippet` 中内嵌非空代码片段）。共 69,228 条工具告警，Slither 69,130 条、Mythril 98 条，非空金标准标注 0 条。
- 标签形式与来源：工具给出 `detector`、`category`、`severity`、`confidence` 和文字说明。严重度取 Info、Low、Medium、High、Optimization，置信度取 High、Medium 或空。`label.gold_label` 全为空，无法据此区分真阳性与误报。
- 标签对象：每组标签赋给一条发现的 `id`。记录可列出相关合约、函数和符号；每个 `provenances` 条目的 `file`、`lines` 标出文件和行号，`locations` 可列出多处位置。同一份源码可对应多条发现。
- 依据：固定版发布文件实测，按 Parquet 行和工具字段计数，片段剔除空值与空白。本地预览含 15 条样例。 [本地预览与嵌套字段](../../data/raw_data/DS140_solidity-findings/huggingface-first-rows.json) · [固定版 Parquet 数据表](https://huggingface.co/datasets/nguyenan0808/solidity-findings/blob/da2665c1a695690cb8aba019ecb293998883235a/data/train-00000-of-00001.parquet)
