"""
[难度: ⭐⭐⭐]
[所属知识点: DataCollator 中文 pad]
[预计完成时间: 15 分钟]

实现中文数据 collator 函数,对 batch 中不等长的
input_ids 做右侧 padding,返回字典含 input_ids、
attention_mask、labels。

示例:
    >>> 输入不等长 batch,返回 pad 后张量
"""

import torch
from transformers import AutoTokenizer

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 不等长 batch
    # 测试 2: 含标签 batch
    pass
