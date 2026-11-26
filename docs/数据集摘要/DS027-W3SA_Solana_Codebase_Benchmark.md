# DS027 W3SA Solana Codebase Benchmark

- 收录范围：纳入 W3SA Solana 基准中受审的 Rust 项目，以及项目关联的审计发现和人工注入缺陷。
- 数据量：7 个受审项目；独立合约源码文件数未知（233 份扫描文件未区分类型）；共 76 项标注，含 57 项审计发现、19 项人工注入缺陷。
- 标签形式与来源：审计发现来自既有安全报告，部分项目另由发布方人工注入缺陷。数据卡按 Critical、High、Medium、Low/Informational 汇总，逐项标签的编码未知。
- 标签对象：每项发现或注入缺陷均关联到一个项目；原始标注受限，函数和行级定位情况未知。
- 依据：发布方报告。逐项目加总来源列；Port Sundial 按来源计 13 项，按严重度计 14 项，本文按来源计。 [项目统计](https://huggingface.co/datasets/almanax/w3sa-bm-solana#project-statistics) · [版本和下载状态](../../data/raw_data/_manifest.csv)
