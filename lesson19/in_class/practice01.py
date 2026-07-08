"""
[难度: ⭐]
[所属知识点: MinMaxScaler 原理]
[预计完成时间: 5 分钟]

题目描述:
给定一个年龄列表 age = [20, 30, 40, 50, 60],
手写一个手动 MinMax 归一化函数 `minmax_scale(values)`,
将数据缩放到 [0, 1]。
公式: x_scaled = (x - min) / (max - min)。
返回 numpy 数组。

示例:
    >>> minmax_scale([20, 30, 40, 50, 60])
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def minmax_scale(values):
    """手动实现 MinMax 归一化,将数据缩放到 [0, 1]"""
    arr = np.array(values, dtype=float)
    min_val = arr.min()
    max_val = arr.max()
    # 防止除零: 如果最大值等于最小值,直接返回全 0
    if max_val == min_val:
        return np.zeros_like(arr)
    return (arr - min_val) / (max_val - min_val)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    result = minmax_scale([20, 30, 40, 50, 60])
    print("测试1 - 正常情况:", result)

    # 测试 2: 边界情况 — 所有值相同
    result2 = minmax_scale([5, 5, 5])
    print("测试2 - 全部相同:", result2)

    # 测试 3: 只有两个值
    result3 = minmax_scale([0, 100])
    print("测试3 - 两个值:", result3)
