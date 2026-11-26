# DS193 FORGE-Curated

- 收录范围：纳入 FORGE-Curated 中可关联到项目源码的审计发现，另列未取得源码的报告发现。
- 数据量：2,485 条有源码项目的审计发现；至少 1,003 份直接目标源码（独立 `.sol` 文件）；2,485 条发现标注。无源码组另有 1,121 条发现及对应的 1,121 条标注。
- 标签形式与来源：原始发现来自 11 家审计团队。FORGE 提取标题、描述和严重度并归入分层 CWE 类别；有源码组严重度取 Critical、High、Medium、Low、Informational，另有 52 条为空。
- 标签对象：标签直接赋给一项报告发现。`files` 可关联多个文件，`location` 可细至函数及行范围；部分发现缺少定位。位置由模型提取，作者持续人工核验。
- 依据：本地实测（提交 `c2829d4`）。分别累计 208 份有源码及 115 份无源码报告的 `findings`。按报告项目根目录匹配目标路径，24 个报告与 Solidity 路径组合未精确命中；本地项目树的 29,150 份源码含依赖和测试，展平表示不另计。 [发布方统计与模式](../../data/raw_data/DS193_FORGE-Curated/README.md) · [Safe 报告发现](../../data/raw_data/DS193_FORGE-Curated/dataset-curated/findings/ackee-blockchain-safe-smart-account-report.json) · [Symmio 报告的项目根目录及两条目标路径](../../data/raw_data/DS193_FORGE-Curated/dataset-curated/findings/2025.03.10%20-%20Final%20-%20Symmio%2C%20Staking%20and%20Vesting%20Audit%20Report.json)
