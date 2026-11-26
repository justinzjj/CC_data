# DS009 DAppSCAN

- 收录范围：收录 DAppSCAN-source 中有 SWC 审计标注的 Solidity 源码，另列字节码侧标注的规模。
- 数据量：948 份带标注的源码样本，对应 948 份独立 `.sol` 文件（本地有其中 12 份正文）和 1,646 条源码侧 SWC 标注。字节码侧另有 493 份标注文件、888 条 SWC 标注。
- 标签形式与来源：发布方依据安全审计报告整理发现。`SWCs[].category` 用 SWC 编号和名称表示类别，如 `SWC-113-DoS with Failed Call`，源码侧共 34 类。
- 标签对象：每条源码侧发现归属 `filePath` 指向的文件，`lineNumber` 可指向单行或行范围（5 条仅指整份合约），`function` 可标出函数（411 条为 `N/A`，11 条为空）。
- 依据：本地实测，按不同 `filePath` 匹配固定版源码树，按两套 JSON 的 `SWCs` 数组分别计数。 [本地全部源码侧标注](../../data/raw_data/DS009_DAppSCAN/DAppSCAN-source/SWCsource) · [ReversibleICO 标注示例](../../data/raw_data/DS009_DAppSCAN/DAppSCAN-source/SWCsource/consensys-rICO/rICO-smart-contracts-77517a4dceed53ff7c5a7f7580cb805831a7f8d5/ReversibleICO.json) · [发布方源码树](https://github.com/InPlusLab/DAppSCAN/tree/66a56619c44770e05c2db600fa6468115ff0dcd5/DAppSCAN-source/contracts) · [字节码侧标注](../../data/raw_data/DS009_DAppSCAN/DAppSCAN-bytecode/SWCbytecode)
