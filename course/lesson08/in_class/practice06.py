"""
[难度: ⭐⭐⭐⭐]
[所属知识点: strip() / lstrip() / rstrip()]
[预计完成时间: 20 分钟]

题目描述:
    输入一段前后有空格的文本,用 strip 去除两侧空格,
    用 lstrip 去除左侧,rstrip 去除右侧,分别打印结果。

示例:
    >>> text = "   hello world   "
    strip  → "hello world"
    lstrip → "hello world   "
    rstrip → "   hello world"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
text = input("请输入一段文本: ")
print("原始文本:", repr(text))
print("strip  :", repr(text.strip()))
print("lstrip :", repr(text.lstrip()))
print("rstrip :", repr(text.rstrip()))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两侧空格
    s = "   hello   "
    print(f"测试1 strip:  {repr(s.strip())}")
    print(f"测试1 lstrip: {repr(s.lstrip())}")
    print(f"测试1 rstrip: {repr(s.rstrip())}")

    # 测试 2: 无空格
    s2 = "hello"
    print(f"测试2 strip:  {repr(s2.strip())}")

    # 测试 3: 只有空格
    s3 = "     "
    print(f"测试3 strip:  {repr(s3.strip())}")
