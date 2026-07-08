"""
[难度: ⭐⭐⭐]
[所属知识点: 回归问题 GridSearchCV]
[预计完成时间: 15 分钟]

题目描述:
用 California Housing 数据,对 GradientBoostingRegressor 进行调参:
  - n_estimators: [50, 100]
  - max_depth: [3, 5]
  - learning_rate: [0.05, 0.1]
使用 GridSearchCV(cv=3) 搜索最佳参数组合,
输出 best_params_ 和对应的 best_score_(负均方误差)。

示例:
    >>> # best_params_ 如 {'learning_rate': 0.1, 'max_depth': 5, ...}
    >>> # best_score_ 为负均方误差,如 -0.2379
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

# 加载数据并切分
housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 定义参数网格
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5],
    "learning_rate": [0.05, 0.1],
}

# 构建 GridSearchCV(cv=3)
gbr = GradientBoostingRegressor(random_state=42)
grid_search = GridSearchCV(
    estimator=gbr,
    param_grid=param_grid,
    cv=3,
    scoring="neg_mean_squared_error",
)

# 执行搜索
grid_search.fit(X_train, y_train)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出最佳参数
    print(f"最佳参数 best_params_: {grid_search.best_params_}")

    # 测试 2: 输出最佳分数(负均方误差)
    print(f"最佳分数 best_score_: "
          f"{grid_search.best_score_:.4f}")

    # 测试 3: 验证参数合法性
    assert grid_search.best_params_["n_estimators"] in [50, 100]
    assert grid_search.best_params_["max_depth"] in [3, 5]
    assert grid_search.best_params_["learning_rate"] in [0.05, 0.1]
    print("测试通过: GridSearchCV 搜索结果合法")
