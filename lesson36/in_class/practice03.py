"""
[难度: ⭐⭐]
[所属知识点: tokenizer 对齐/红线]
[预计完成时间: 10 分钟]

分别用 bert-base-chinese 和 uer/roberta-base-finetuned
-jd-full-chinese 的 tokenizer 编码同一句中文,对比长度
和 token id 差异。
教学红线:Tokenizer 没对齐预训练模型(用了不同词表)会导
致效果极差！

示例:
    >>> 同一个句子,不同 tokenizer 长度/ID 不同
"""

from transformers import AutoTokenizer

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: bert tokenizer 编码
    # 测试 2: roberta tokenizer 编码并对比
    pass
