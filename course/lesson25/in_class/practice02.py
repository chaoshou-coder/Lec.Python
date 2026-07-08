"""
[难度: ⭐⭐]
[所属知识点: 探索性数据分析 / EDA]
[预计完成时间: 10 分钟]

题目描述:
从 sklearn.datasets.fetch_california_housing 加载数据
(使用 as_frame=True 返回 DataFrame)。
输出前 5 行、describe() 统计信息、缺失值统计。
初步观察数据分布,为后续建模做准备。

示例:
    >>> # housing_df.head() 显示前 5 行
    >>> # housing_df.describe() 显示均值/标准差/分位数
    >>> # housing_df.isnull().sum() 显示每列缺失值数量(应全为 0)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing

# 加载 California Housing 数据为 DataFrame
housing = fetch_california_housing(as_frame=True)
df = housing.frame  # 包含特征 + target 列

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出数据前 5 行
    print("===== 前 5 行数据 =====")
    print(df.head())

    # 测试 2: 输出 describe() 统计信息
    print("\n===== describe() 统计信息 =====")
    print(df.describe())

    # 测试 3: 输出缺失值统计(边界: 应无缺失)
    print("\n===== 缺失值统计 =====")
    missing = df.isnull().sum()
    print(missing)
    assert missing.sum() == 0, "数据存在缺失值"
    print("测试通过: 数据无缺失值")
