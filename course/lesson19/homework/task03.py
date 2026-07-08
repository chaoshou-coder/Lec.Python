"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 预处理组合拳]
[预计完成时间: 20 分钟]

题目描述:
模拟一个完整预处理流水线:给定 DataFrame 含缺失值和分类列
({"城市":["北京","上海",None],"年龄":[25,None,35],
"收入":[10000,20000,15000]}),
先用 SimpleImputer 填充缺失值,
再用 LabelEncoder 编码城市列,返回处理后的 DataFrame。

示例:
    >>> 缺失值被填充,城市列变为 0/1 整数
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def preprocess_pipeline(df):
    """完整的预处理流水线:填充缺失值 + 编码分类列"""
    df_result = df.copy()

    # 第一步: 对数值列用中位数填充缺失值
    num_cols = df_result.select_dtypes(exclude="object").columns
    imp_median = SimpleImputer(strategy="median")
    df_result[num_cols] = imp_median.fit_transform(df_result[num_cols])

    # 第二步: 对分类列用众数填充缺失值
    cat_cols = df_result.select_dtypes(include="object").columns
    imp_most = SimpleImputer(strategy="most_frequent")
    df_result[cat_cols] = imp_most.fit_transform(df_result[cat_cols])

    # 第三步: 对分类列进行 LabelEncoder 编码
    le = LabelEncoder()
    for col in cat_cols:
        df_result[col] = le.fit_transform(df_result[col])

    return df_result


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    df = pd.DataFrame({
        "城市": ["北京", "上海", None],
        "年龄": [25, None, 35],
        "收入": [10000, 20000, 15000],
    })
    print("原始数据:")
    print(df)
    result = preprocess_pipeline(df)
    print("\n预处理后:")
    print(result)

    # 测试 2: 多个缺失值
    df2 = pd.DataFrame({
        "城市": [None, "北京", "上海"],
        "年龄": [None, None, 30],
        "收入": [5000, None, None],
    })
    print("\n多缺失原始数据:")
    print(df2)
    print("\n预处理后:")
    print(preprocess_pipeline(df2))
