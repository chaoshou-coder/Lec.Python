"""
[难度: ⭐⭐⭐]
[所属知识点: 梯度提升提升效果]
[预计完成时间: 15 分钟]

题目描述:
用 California Housing 数据,对比 LinearRegression 和
GradientBoostingRegressor(n_estimators=100) 在测试集上的 RMSE。
输出两者结果,验证非线性模型的预测效果优于线性模型。

提示: from sklearn.ensemble import GradientBoostingRegressor

示例:
    >>> # LinearRegression RMSE 约 0.7459
    >>> # GradientBoostingRegressor RMSE 约 0.4928
    >>> # 梯度提升模型 RMSE 明显低于线性回归
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# 加载数据并切分
housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练线性回归基准模型
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

# 训练梯度提升模型
gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
gbr.fit(X_train, y_train)
y_pred_gbr = gbr.predict(X_test)
rmse_gbr = np.sqrt(mean_squared_error(y_test, y_pred_gbr))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出两者 RMSE 对比
    print(f"LinearRegression RMSE:          {rmse_lr:.4f}")
    print(f"GradientBoostingRegressor RMSE: {rmse_gbr:.4f}")

    # 测试 2: 验证梯度提升优于线性回归
    assert rmse_gbr < rmse_lr, \
        f"梯度提升 RMSE({rmse_gbr:.4f}) 应低于线性回归({rmse_lr:.4f})"
    print(f"\n测试通过: 梯度提升比线性回归 RMSE 降低了 "
          f"{(rmse_lr - rmse_gbr):.4f}")
