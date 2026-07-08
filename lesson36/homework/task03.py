"""
[难度: ⭐⭐⭐⭐]
[所属知识点: HF 完整中文情感分类]
[预计完成时间: 20 分钟]

使用 uer/roberta-base-finetuned-jd-full-chinese 模型,
用 8 条中文情感数据(4 正/4 负)完整走通 Trainer 微调
流程,跑 2 个 epoch。
注意:运行需联网下载模型,训练可能较慢。
教学红线:Tokenizer 没对齐预训练模型(用了不同词表)会导
致效果极差！本请务必使用模型自带 tokenizer。

示例:
    >>> 输出训练 loss 下降
"""

from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer, Trainer, TrainingArguments
)
from datasets import Dataset

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 构造 8 条数据并训练
    # 测试 2: 训练后做预测
    pass
