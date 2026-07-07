"""
[难度: ⭐⭐⭐]
[所属知识点: **kwargs]
[预计完成时间: 15 分钟]

题目描述:
    定义一个函数 print_info(**kwargs),打印所有键值对,
    每行格式: key: value。

示例:
    >>> print_info(name="张三", age=20)
    name: 张三
    age: 20
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 示例调用
print_info(name="张三", age=20)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 多个键值对
    print("测试1:")
    print_info(a=1, b=2, c=3)

    # 测试 2: 单个键值对
    print("测试2:")
    print_info(name="Alice")

    # 测试 3: 无参数
    print("测试3:")
    print_info()
