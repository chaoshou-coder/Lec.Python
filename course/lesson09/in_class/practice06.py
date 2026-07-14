"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 自定义装饰器(@wraps + 计时器)]
[预计完成时间: 20 分钟]

题目描述:
    请编写一个计时器装饰器 timer,用于测量函数的执行时间。
    要求:
      - 使用 @wraps 保留原函数的元信息(如 __name__)
      - 打印函数名和耗时(秒,保留 4 位小数)
      - 不影响原函数的返回值

    wraps 需从 functools 导入,用于"包裹"内部函数。

示例:
    >>> @timer
    ... def slow_add(a, b):
    ...     import time
    ...     time.sleep(0.1)
    ...     return a + b
    >>> slow_add(3, 5)
    [timer] slow_add 耗时: 0.1001 秒
    8
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 提示: 需要导入
# import time
# from functools import wraps

def timer(func):
    """计时器装饰器"""
    # 使用 @wraps(func) 保留元信息
    # 内部函数记录开始时间、调用 func、计算耗时
    pass

# 测试用函数
@timer
def slow_add(a, b):
    """模拟耗时加法"""
    import time
    time.sleep(0.1)
    return a + b

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 计时功能
    result = slow_add(3, 5)
    print(f"返回值: {result}")
    # 测试 2: wraps 保留元信息
    print(f"函数名: {slow_add.__name__}")
    print(f"文档字符串: {slow_add.__doc__}")
