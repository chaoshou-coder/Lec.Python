"""
[难度: ⭐⭐⭐]
[所属知识点: ColumnTransformer 前置 — 特征类型识别]
[预计完成时间: 15 分钟]

题目描述:
给定一个混合类型的 DataFrame(列:城市、年龄、收入、性别),
写函数 `identify_feature_types(df)` 识别哪些是数值特征、
哪些是分类特征,返回 {"num": [...], "cat": [...]}。
判断规则: object/类别型→分类,数值型→数值。

测试数据:
    pd.DataFrame({
        "城市": ["北京", "上海", "北京"],
        "年龄": [25, 30, 35],
        "收入": [10000, 20000, 15000],
        "性别": ["男", "女", "男"],
    })

示例:
    >>> identify_feature_types(df)
    {"num": ["年龄", "收入"], "cat": ["城市", "性别"]}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import pandas as pd


def identify_feature_types(df):
    """识别数值特征和分类特征"""
    num_cols = []
    cat_cols = []
    for col in df.columns:
        if df[col].dtype == "object":
            cat_cols.append(col)
        else:
            num_cols.append(col)
    return {"num": num_cols, "cat": cat_cols}


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    df = pd.DataFrame({
        "城市": ["北京", "上海", "北京"],
        "年龄": [25, 30, 35],
        "收入": [10000, 20000, 15000],
        "性别": ["男", "女", "男"],
    })
    result = identify_feature_types(df)
    print("测试1 - 特征类型识别:", result)

    # 测试 2: 全是数值列
    df2 = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.0]})
    print("测试2 - 全数值:", identify_feature_types(df2))
