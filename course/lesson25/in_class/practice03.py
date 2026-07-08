"""
[难度: ⭐⭐]
[所属知识点: 基准模型]
[预计完成时间: 10 分钟]

题目描述:
用 fetch_california_housing 的 data 和 target,
通过 train_test_split(test_size=0.2, random_state=42) 切分数据。
训练 LinearRegression,输出测试集上的 RMSE 和 R²。
此结果作为后续模型的基准(baseline)。

示例:
    >>> # RMSE 约为 0.7459
    >>> # R2 约为 0.5758
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 切分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练线性回归模型
lr = LinearRegression()
lr.fit(X_train, y_train)

# 预测测试集
y_pred = lr.predict(X_test)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 计算并输出 RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"测试集 RMSE: {rmse:.4f}")

    # 测试 2: 计算并输出 R²
    r2 = r2_score(y_test, y_pred)
    print(f"测试集 R²: {r2:.4f}")

    # 验证基准值范围
    assert rmse < 1.0, f"RMSE 异常: {rmse}"
    assert 0 < r2 < 1, f"R² 异常: {r2}"
    print("测试通过: 基准模型 RMSE 和 R² 在合理范围")
