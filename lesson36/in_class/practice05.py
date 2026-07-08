"""
[难度: ⭐⭐⭐]
[所属知识点: datasets 加载与 tokenize]
[预计完成时间: 15 分钟]

加载 imdb 数据集前 100 条,写 tokenize_fn(batch) 函数
进行 batch encode,处理后打印 input_ids 的 shape 示例。
注意:运行需联网下载数据集。

示例:
    >>> batch shape: (batch_size, seq_len)
"""

from datasets import load_dataset
from transformers import AutoTokenizer

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 加载集合并取 batch
    # 测试 2: tokenize 后打印维度
    pass
