# DS028 W3SA Aptos Codebase Benchmark

- 收录范围：收录 Aptos Move 的三个子集：`aptos_audits` 的真实审计项目，以及 `aptos_ctf_1`、`aptos_ctf_2` 的有意设缺挑战。
- 数据量：审计组 10 个项目，两组 CTF 分别有 9 道、4 道题。独立 Move 合约源码文件数未知（审计组列出 99 份项目文件）。审计组有 92 项发现，两组 CTF 的 13 道题均有缺陷类型说明，一题可列多种缺陷，逐项缺陷数未知。
- 标签形式与来源：人工审计发现按严重度分为 Critical（4 项）、High（18 项）、Medium（14 项）、Low（27 项）、Informational（29 项）。CTF 以文字标明出题方设置的缺陷，如 `Unlimited token minting`、`Arithmetic Overflow`。
- 标签对象：审计发现归属项目，挑战缺陷说明归属具体题目。发布方说明 `ground_truth` JSON 可记录受影响函数和代码片段，字段覆盖率未知。
- 依据：发布方报告，文件受限。项目数和发现数取审计表，题数按两张挑战表的实际行数统计（第一组跳过题号 6）。 [发布方分组统计与结构](https://huggingface.co/datasets/almanax/w3sa-bm-aptos#project-statistics) · [固定版本文件目录](https://huggingface.co/api/datasets/almanax/w3sa-bm-aptos/revision/258ff2856c1d70d6ed94a8f8a60e6dd52496c5da)
