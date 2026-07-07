"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 混合参数顺序]
[预计完成时间: 25 分钟]

题目描述:
    定义一个函数 process_data(data, *args, **kwargs),
    分别打印 data、所有 args 和所有 kwargs,
    理解 Python 中位置参数、可变参数、关键字参数的顺序。

示例:
    >>> process_data("hello", 1, 2, 3, x=10, y=20)
    data: hello
    args: (1, 2, 3)
    kwargs: {'x': 10, 'y': 20}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def process_data(data, *args, **kwargs):
    print(f"data: {data}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


# 示例调用
process_data("hello", 1, 2, 3, x=10, y=20)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 完整调用
    print("测试1:")
    process_data("test", "a", "b", key1="v1")

    # 测试 2: 只有位置参数和关键字参数
    print("测试2:")
    process_data("only", name="Tom")

    # 测试 3: 无额外参数
    print("测试3:")
    process_data("none")

    # 测试 4: 只有可变位置参数
    print("测试4:")
    process_data("var", 100, 200, 300)
