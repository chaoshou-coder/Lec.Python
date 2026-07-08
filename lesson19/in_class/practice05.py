"""
[难度: ⭐⭐⭐]
[所属知识点: SimpleImputer]
[预计完成时间: 15 分钟]

题目描述:
使用 sklearn SimpleImputer(strategy="median") 填充一个含
缺失值的 DataFrame,并对比均值填充结果。
给定 df 含 3 行 [1,NaN,3],[4,5,NaN],[NaN,8,9],
展示两种策略填充后行列的值。

示例:
    >>> 中位数填充后的 DataFrame 和均值填充后的 DataFrame
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


def impute_compare(df):
    """分别用中位数和均值填充缺失值,返回两个 DataFrame"""
    # 中位数填充
    imp_median = SimpleImputer(strategy="median")
    arr_median = imp_median.fit_transform(df)
    df_median = pd.DataFrame(arr_median, columns=df.columns)

    # 均值填充
    imp_mean = SimpleImputer(strategy="mean")
    arr_mean = imp_mean.fit_transform(df)
    df_mean = pd.DataFrame(arr_mean, columns=df.columns)

    return df_median, df_mean


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    df = pd.DataFrame(
        [[1, np.nan, 3],
         [4, 5, np.nan],
         [np.nan, 8, 9]],
        columns=["A", "B", "C"],
    )
    print("原始数据:")
    print(df)
    df_med, df_mean = impute_compare(df)
    print("\n中位数填充:")
    print(df_med)
    print("\n均值填充:")
    print(df_mean)
