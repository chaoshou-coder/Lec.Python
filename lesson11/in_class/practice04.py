"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 默认参数 + if/elif/else]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 calc(a, b, op='+'),根据 op 返回对应运算结果,
    支持 + - * /,默认加法。除数为 0 时返回 None 并提示。

示例:
    >>> calc(3, 5)
    8
    >>> calc(10, 2, op='/')
    5.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def calc(a, b, op='+'):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            print("除数不能为 0")
            return None
        return a / b
    else:
        print(f"不支持的运算符: {op}")
        return None


# 示例调用
print("3 + 5 =", calc(3, 5))
print("10 / 2 =", calc(10, 2, op='/'))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 加法(默认)
    print(f"测试1: {calc(3, 5)}")

    # 测试 2: 除法
    print(f"测试2: {calc(10, 3, op='/')}")

    # 测试 3: 除数为 0
    print(f"测试3: {calc(5, 0, op='/')}")

    # 测试 4: 非法运算符
    print(f"测试4: {calc(1, 2, op='%')}")
