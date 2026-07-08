"""
[难度: ⭐]
[所属知识点: type() 与基本数据类型]
[预计完成时间: 5 分钟]

题目描述:
  请创建以下 4 个变量,并使用 type() 打印它们的类型:
    - 整数 100
    - 浮点数 3.14
    - 字符串 "Hello"
    - 布尔值 True
  要求输出格式为 "值 -> 类型"。

示例:
    >>> 运行程序
    100 -> <class 'int'>
    3.14 -> <class 'float'>
    Hello -> <class 'str'>
    True -> <class 'bool'>
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 整数类型
    v1 = 100
    print(f"{v1} -> {type(v1)}")
    assert type(v1).__name__ == "int"

    # 测试 2: 浮点数类型
    v2 = 3.14
    print(f"{v2} -> {type(v2)}")
    assert type(v2).__name__ == "float"

    # 测试 3: 字符串类型
    v3 = "Hello"
    print(f"{v3} -> {type(v3)}")
    assert type(v3).__name__ == "str"

    # 测试 4: 布尔类型
    v4 = True
    print(f"{v4} -> {type(v4)}")
    assert type(v4).__name__ == "bool"

    print("所有测试通过!")
