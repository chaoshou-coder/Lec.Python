"""
[难度: ⭐⭐⭐]
[所属知识点: OneHotEncoder 原理]
[预计完成时间: 15 分钟]

题目描述:
不使用 sklearn,手写 `one_hot_encode(values)` 实现 OneHotEncoder
功能。输入 ["红", "蓝", "绿", "红"],返回二维数组和类别列表。
类别按 Unicode 码点排序(即 sorted 默认顺序)。

示例:
    >>> encoded, cats = one_hot_encode(["红", "蓝", "绿", "红"])
    >>> encoded = array([[1,0,0],[0,0,1],[0,1,0],[1,0,0]])
    >>> cats = ["红", "绿", "蓝"]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def one_hot_encode(values):
    """手写 OneHot 编码"""
    # 按字母排序得到类别列表
    categories = sorted(set(values))
    # 类别到索引的映射
    mapping = {cat: idx for idx, cat in enumerate(categories)}
    # 构建二维零矩阵,逐行填 1
    encoded = np.zeros((len(values), len(categories)), dtype=int)
    for i, val in enumerate(values):
        encoded[i, mapping[val]] = 1
    return encoded, categories


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    encoded, cats = one_hot_encode(["红", "蓝", "绿", "红"])
    print("测试1 - 编码结果:")
    print(encoded)
    print("测试1 - 类别列表:", cats)

    # 测试 2: 只有两个类别
    encoded2, cats2 = one_hot_encode(["男", "女", "女", "男"])
    print("\n测试2 - 二分类:")
    print(encoded2)
    print("测试2 - 类别列表:", cats2)
