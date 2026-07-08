"""
[难度: ⭐⭐]
[所属知识点: StandardScaler 原理]
[预计完成时间: 10 分钟]

题目描述:
手写 `standard_scale(values)` 实现 Z-score 标准化。
公式: z = (x - mean) / std。
输入 [10, 20, 30, 40, 50],
返回标准化后数组(验证 mean≈0, std≈1)。

示例:
    >>> result = standard_scale([10, 20, 30, 40, 50])
    >>> mean ≈ 0.0,  std ≈ 1.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def standard_scale(values):
    """手动实现 Z-score 标准化"""
    arr = np.array(values, dtype=float)
    mean_val = arr.mean()
    std_val = arr.std(ddof=0)
    # 防止除零: 如果标准差为 0,直接返回全 0
    if std_val == 0:
        return np.zeros_like(arr)
    return (arr - mean_val) / std_val


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况,验证 mean≈0, std≈1
    data = [10, 20, 30, 40, 50]
    result = standard_scale(data)
    print("测试1 - 标准化结果:", result)
    print("  mean ≈", round(result.mean(), 6))
    print("  std  ≈", round(result.std(ddof=0), 6))

    # 测试 2: 边界情况 — 所有值相同
    result2 = standard_scale([7, 7, 7, 7])
    print("测试2 - 全部相同:", result2)
