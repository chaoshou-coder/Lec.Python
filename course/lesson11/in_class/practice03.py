"""
[难度: ⭐⭐]
[所属知识点: 向量化运算(对比 for 循环)]
[预计完成时间: 15 分钟]

题目描述:
    对比 for 循环和 NumPy 向量化运算的性能差异。

    任务:
      1. 创建包含 10000 个元素的数组
      2. 用 for 循环对每个元素平方,记录时间
      3. 用 NumPy 向量化(arr ** 2)平方,记录时间
      4. 打印两种方式的耗时对比

    向量化运算: 对整个数组一次性操作,无需显式循环。

示例:
    >>> # 向量化比 for 循环快数十倍
    for 循环耗时: 0.002 秒
    向量化耗时: 0.0001 秒
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np
import time

# 创建大数组
arr = np.arange(10000)

# 方法 1: for 循环平方
# 提示: 遍历 arr,逐个计算平方,存入列表
start = time.time()
result_for = []
# 在此编写 for 循环
time_for = time.time() - start

# 方法 2: 向量化平方
start = time.time()
result_vec = None  # 替换为 arr ** 2
time_vec = time.time() - start

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    print(f"for 循环耗时: {time_for:.6f} 秒")
    print(f"向量化耗时: {time_vec:.6f} 秒")
    # 验证结果一致
    print(f"结果一致: {np.array_equal(result_for, result_vec)}")
