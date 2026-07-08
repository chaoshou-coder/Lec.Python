"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 端到端 Pipeline]
[预计完成时间: 20 分钟]

题目描述:
构建 California Housing 完整 Pipeline:
  - ("preprocess", StandardScaler) 标准化特征
  - ("model", GradientBoostingRegressor(n_estimators=100,
     random_state=42))
使用 cross_val_score(cv=5, scoring="neg_mean_squared_error") 评估,
输出 RMSE 的均值 ± 标准差。

示例:
    >>> # RMSE 均值 ± 标准差,如 0.4938 ± 0.0065
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline

# 加载数据(交叉验证不需要手动切分)
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 构建 Pipeline
pipe = Pipeline([
    ("preprocess", StandardScaler()),
    ("model", GradientBoostingRegressor(
        n_estimators=100, random_state=42
    )),
])

# 用 cross_val_score 进行 5 折交叉验证
scores = cross_val_score(
    pipe, X, y, cv=5, scoring="neg_mean_squared_error"
)
# 分数为负均方误差,取负号后开方得到 RMSE
rmse_scores = np.sqrt(-scores)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出每折 RMSE
    for i, rmse in enumerate(rmse_scores):
        print(f"第 {i + 1} 折 RMSE: {rmse:.4f}")

    # 测试 2: 输出 RMSE 均值 ± 标准差
    mean_rmse = rmse_scores.mean()
    std_rmse = rmse_scores.std()
    print(f"\nRMSE 均值 ± 标准差: {mean_rmse:.4f} ± {std_rmse:.4f}")

    # 测试 3: 验证结果合理性
    assert mean_rmse < 0.8, f"RMSE 均值偏高: {mean_rmse}"
    assert std_rmse < 0.1, f"标准差过大: {std_rmse}"
    print("测试通过: Pipeline 交叉验证 RMSE 在合理范围")
