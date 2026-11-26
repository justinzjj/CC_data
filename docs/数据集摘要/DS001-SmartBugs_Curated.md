# DS001 SmartBugs Curated

- 收录范围：纳入 SmartBugs Curated 漏洞索引收录的 Solidity 源码，用于识别漏洞类别及所在行。
- 数据量：143 份带标注源码，均为独立 `.sol` 文件；207 条漏洞标注，累计引用 222 个行号。
- 标签形式与来源：发布方及社区整理公开案例，将源码注释汇入索引。`category` 为漏洞类别字符串，共 10 类，如 `access_control`、`reentrancy`。
- 标签对象：每条标注通过 `path` 关联一份源码，通过 `lines` 定位到一个或多个行号；一份源码可有多条标注。
- 依据：本地实测。按提交 `230e649` 的索引路径回查源码，行号按出现次数计。 [漏洞索引](../../data/raw_data/DS001_SmartBugs_Curated/smartbugs-curated-230e649123477eff332742a59a1c7cc6dc286cab/smartbugs-curated-230e649123477eff332742a59a1c7cc6dc286cab/vulnerabilities.json) · [标注约定](../../data/raw_data/DS001_SmartBugs_Curated/smartbugs-curated-230e649123477eff332742a59a1c7cc6dc286cab/smartbugs-curated-230e649123477eff332742a59a1c7cc6dc286cab/README.md)
