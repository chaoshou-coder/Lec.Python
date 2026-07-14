"""
[难度: ⭐⭐⭐]
[所属知识点: map/filter 高阶函数]
[预计完成时间: 15 分钟]

题目描述:
    给定一个整数列表 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    请使用 map 和 filter 完成以下任务:
      1. 用 filter 筛选出所有偶数
      2. 用 map 对筛选后的偶数求平方
      3. 将结果转为列表输出

    map(函数, 可迭代对象) — 对每个元素执行函数
    filter(函数, 可迭代对象) — 保留使函数返回 True 的元素

示例:
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> process_numbers(nums)
    [4, 16, 36, 64, 100]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def process_numbers(nums):
    """筛选偶数并求平方"""
    # 提示: 先 filter 偶数,再 map 平方
    # evens = filter(lambda x: x % 2 == 0, nums)
    # squares = map(lambda x: x ** 2, evens)
    # return list(squares)
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 测试 1: 常规列表
    print(f"偶数平方: {process_numbers(nums)}")
    # 测试 2: 全奇数
    print(f"全奇数: {process_numbers([1, 3, 5])}")
    # 测试 3: 空列表
    print(f"空列表: {process_numbers([])}")
