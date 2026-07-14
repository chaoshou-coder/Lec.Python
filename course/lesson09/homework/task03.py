"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合(生成器 + 装饰器 + map/filter)]
[预计完成时间: 30 分钟]

题目描述:
    综合运用生成器、装饰器和高阶函数,完成以下任务:

    1. 编写装饰器 @log_calls,记录函数被调用的次数
    2. 编写生成器函数 read_numbers(data),
       从嵌套列表中逐个 yield 数字
    3. 使用 map/filter 过滤出偶数并求平方

    要求: 三个知识点必须全部使用。

示例:
    >>> data = [[1, 2, 3], [4, 5], [6]]
    >>> list(read_numbers(data))
    [1, 2, 3, 4, 5, 6]
    >>> process(data)
    [4, 16, 36]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 提示: 需要导入
# from functools import wraps

def log_calls(func):
    """记录函数调用次数的装饰器"""
    # 使用 func.call_count 属性计数
    pass

def read_numbers(data):
    """从嵌套列表中逐个生成数字"""
    # 提示: for sublist in data:
    #           for num in sublist:
    #               yield num
    pass

@log_calls
def process(data):
    """过滤偶数并求平方"""
    # 提示: 用 read_numbers 展开,filter 偶数,map 平方
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5], [6]]
    # 测试 1: 生成器展开
    print(f"展开: {list(read_numbers(data))}")
    # 测试 2: 过滤 + 平方
    result = process(data)
    print(f"偶数平方: {result}")
    # 测试 3: 调用计数
    print(f"调用次数: {process.call_count}")
