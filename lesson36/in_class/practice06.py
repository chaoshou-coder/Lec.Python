"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Trainer 微调 + TrainingArguments]
[预计完成时间: 20 分钟]

对 5 条内置中文情感数据用 Trainer 微调 bert-base-chinese
跑 1 epoch,需包含 TrainingArguments 配置。
注意:运行需联网下载模型,训练可能较慢。

示例:
    >>> 输出训练 loss
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
    # 测试 1: 构造 5 条数据并训练
    # 测试 2: 训练后做预测
    pass
