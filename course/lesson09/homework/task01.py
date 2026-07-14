"""
[难度: ⭐⭐⭐]
[所属知识点: 装饰器(日志记录)]
[预计完成时间: 20 分钟]

题目描述:
    请编写一个日志装饰器 logger,用于记录函数的调用信息。
    要求:
      - 打印函数名、传入参数(args 和 kwargs)
      - 打印函数返回值
      - 使用 @wraps 保留原函数元信息

    这是实际项目中非常实用的调试工具!

示例:
    >>> @logger
    ... def add(a, b):
    ...     return a + b
    >>> add(3, 5)
    [logger] 调用 add(3, 5)
    [logger] add 返回: 8
    8
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 提示: 需要导入
# from functools import wraps

def logger(func):
    """日志记录装饰器"""
    # 使用 @wraps(func) 保留元信息
    # 在调用前后分别打印参数和返回值
    pass

# 测试用函数
@logger
def add(a, b):
    """两数相加"""
    return a + b

@logger
def greet(name, greeting="你好"):
    """打招呼"""
    return f"{greeting},{name}!"

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 普通调用
    result = add(3, 5)
    print(f"结果: {result}")
    print("-" * 30)
    # 测试 2: 带关键字参数
    result = greet("世界", greeting="Hello")
    print(f"结果: {result}")
