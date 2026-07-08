"""
[难度: ⭐⭐]
[所属知识点: 缺失值处理 / SimpleImputer 前置]
[预计完成时间: 10 分钟]

题目描述:
给定含 NaN 的 DataFrame(列:身高、体重、年龄,部分值为 NaN),
写函数 `check_missing(df)` 返回每列缺失率的 Series,
并按缺失率降序排列。

测试数据:
    {"身高":[170,165,None,180,175],
     "体重":[60,None,55,70,65],
     "年龄":[25,30,None,35,40]}

示例:
    >>> check_missing(df)
    体重    0.2
    年龄    0.2
    身高    0.2
    dtype: float64
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import pandas as pd
import numpy as np


def check_missing(df):
    """返回每列缺失率,按缺失率降序排列"""
    # 计算每列缺失率
    missing_rate = df.isnull().mean()
    # 按缺失率降序排列
    return missing_rate.sort_values(ascending=False)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    df = pd.DataFrame({
        "身高": [170, 165, None, 180, 175],
        "体重": [60, None, 55, 70, 65],
        "年龄": [25, 30, None, 35, 40],
    })
    print("测试1 - 缺失率统计:")
    print(check_missing(df))

    # 测试 2: 有列完全为空
    df2 = pd.DataFrame({
        "A": [None, None, None],
        "B": [1, 2, 3],
    })
    print("\n测试2 - 整列缺失:")
    print(check_missing(df2))
