"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整 ML 工程流程]
[预计完成时间: 20 分钟]

题目描述:
综合以上所有知识点,完成 California Housing 完整 ML 项目交付:
  1. fetch_california_housing 加载数据
  2. train_test_split(test_size=0.2, random_state=42) 切分
  3. StandardScaler 标准化特征
  4. GradientBoostingRegressor + GridSearchCV(cv=3) 调参
     - n_estimators: [50, 100]
     - max_depth: [3, 5]
     - learning_rate: [0.05, 0.1]
  5. best_estimator_ 在测试集上预测
  6. joblib.dump 保存最佳模型为 "california_model.joblib"
  7. 打印测试集 RMSE 和 R²

示例:
    >>> # 测试集 RMSE: 0.4389 (示例值)
    >>> # 测试集 R2: 0.8415 (示例值)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. 加载数据
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 2. 切分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 标准化特征
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. GridSearchCV 调参
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5],
    "learning_rate": [0.05, 0.1],
}
gbr = GradientBoostingRegressor(random_state=42)
grid_search = GridSearchCV(
    estimator=gbr,
    param_grid=param_grid,
    cv=3,
    scoring="neg_mean_squared_error",
)
grid_search.fit(X_train_scaled, y_train)

# 5. 最佳模型在测试集上预测
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test_scaled)

# 6. 保存模型
joblib.dump(best_model, "california_model.joblib")

# 7. 计算测试集 RMSE 和 R²
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出最佳参数与测试集指标
    print(f"最佳参数: {grid_search.best_params_}")
    print(f"测试集 RMSE: {rmse:.4f}")
    print(f"测试集 R²:   {r2:.4f}")

    # 测试 2: 验证模型性能达标
    assert rmse < 0.6, f"RMSE 偏高: {rmse}"
    assert r2 > 0.7, f"R² 偏低: {r2}"
    print("测试 2 通过: 模型性能达标")

    # 测试 3: 验证模型可加载(持久化成功)
    loaded = joblib.load("california_model.joblib")
    y_pred_loaded = loaded.predict(X_test_scaled)
    assert np.allclose(y_pred, y_pred_loaded), "加载后预测不一致"
    print("测试 3 通过: joblib 保存/加载成功")
