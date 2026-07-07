"""
[难度: ⭐⭐⭐]
[所属知识点: 字符串替换]
[预计完成时间: 15 分钟]

题目描述:
  输入一段文本,将其中的敏感词 "xxx" 全部替换为 "***"。
  要求使用 replace() 方法完成替换。

示例:
    >>> "xxx 是个好网站,xxx 很好用" → "*** 是个好网站,*** 很好用"
    >>> "这里没有敏感词" → "这里没有敏感词"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
text = "xxx 是个好网站,xxx 很好用"
clean_text = text.replace("xxx", "***")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 包含多个敏感词
    text_1 = "xxx 是个好网站,xxx 很好用"
    result_1 = text_1.replace("xxx", "***")
    print(result_1)
    assert result_1 == "*** 是个好网站,*** 很好用"

    # 测试 2: 没有敏感词
    text_2 = "这里没有敏感词"
    result_2 = text_2.replace("xxx", "***")
    print(result_2)
    assert result_2 == "这里没有敏感词"

    # 测试 3: 敏感词连续出现
    text_3 = "xxxxxx"
    result_3 = text_3.replace("xxx", "***")
    print(result_3)
    assert result_3 == "******"

    # 测试 4: 空字符串
    text_4 = ""
    result_4 = text_4.replace("xxx", "***")
    print(result_4)
    assert result_4 == ""

    print("所有测试通过!")
