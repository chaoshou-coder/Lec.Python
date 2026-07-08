"""
[难度: ⭐]
[所属知识点: 中文分词 (jieba)]
[预计完成时间: 5 分钟]

题目: 电商评论分词
某电商平台需要把用户评论切成关键词做后续分析。
请用 jieba.lcut 对给定中文句子做分词,并打印结果。

示例:
    >>> words = jieba.lcut("我爱自然语言处理")
    >>> print(words)
    ['我', '爱', '自然语言', '处理']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import jieba

# 对下面这句话做分词
sentence = "我爱自然语言处理"
words = jieba.lcut(sentence)
print("分词结果:", words)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基础分词
    result = jieba.lcut("我爱自然语言处理")
    print("测试1:", result)
    assert "我" in result
    assert "爱" in result
    assert "自然语言" in result
    assert "处理" in result

    # 测试 2: 电商评论句子
    comment = "这件衣服质量很好,物流也很快"
    result2 = jieba.lcut(comment)
    print("测试2:", result2)
    assert "质量" in result2
    assert "物流" in result2
