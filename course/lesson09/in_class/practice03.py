"""
[难度: ⭐⭐]
[所属知识点: 生成器表达式]
[预计完成时间: 10 分钟]

题目描述:
    请使用生成器表达式(Generator Expression)完成以下任务:
      1. 生成 1~20 中所有偶数的平方
      2. 将字符串列表 ["Hello", "World", "Python"]
         中每个元素转为大写

    注意: 生成器表达式使用圆括号 (), 区别于列表推导式 []。

示例:
    >>> list(even_squares)
    [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    >>> list(upper_words)
    ['HELLO', 'WORLD', 'PYTHON']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 任务 1: 1~20 中所有偶数的平方
# 提示: (x ** 2 for x in range(1, 21) if x % 2 == 0)
even_squares = None  # 替换为生成器表达式

# 任务 2: 字符串列表转大写
words = ["Hello", "World", "Python"]
# 提示: (w.upper() for w in words)
upper_words = None  # 替换为生成器表达式

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 偶数平方
    print(f"偶数平方: {list(even_squares)}")
    # 测试 2: 转大写
    print(f"大写列表: {list(upper_words)}")
