# DS064 A benchmark dataset of Solidity smart contracts

- 收录范围：对真实 Solidity 合约进行十类漏洞的合约级分类。
- 数据量：4,364 个经人工标注的合约。独立源码文件数、漏洞标注总条数和各类条数均未知。
- 标签形式与来源：发布方人工标注 DC、IOU、NC、RE、TD、TO、TOD、UcC、UpS、FE 十类，分别涉及委托调用、整数溢出、嵌套调用、重入、时间戳依赖、tx.origin、交易顺序依赖、未检查调用、无保护自毁和以太币冻结。实际标签编码与类别重叠情况未知。
- 标签对象：标签赋给合约。公开说明未披露函数或行级位置。
- 依据：发布方报告。Zenodo 记录 7744053 须申请访问，合约数和分类取自该版本的 DOI 登记说明。 [发布页](https://zenodo.org/records/7744053) · [DOI 登记说明](https://api.datacite.org/dois/10.5281/zenodo.7744053)
