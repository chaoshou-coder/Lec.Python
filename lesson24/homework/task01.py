"""
[难度: ⭐⭐⭐]
[所属知识点: GridSearchCV]
[预计完成时间: 15 分钟]

题目: 加载 load_iris 数据,构建 Pipeline:
      StandardScaler + SVC()。
      使用 GridSearchCV(cv=5) 搜索最佳参数:
      svc__C = [0.1, 1, 10],
      svc__kernel = ["linear", "rbf"]。
      输出 best_params_ 和 best_score_。

示例:
    >>> # best_params 可能为 {'svc__C': 1, 'svc__kernel': 'rbf'}
"""
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
iris = load_iris()
X, y = iris.data, iris.target

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC()),
])

param_grid = {
    "svc__C": [0.1, 1, 10],
    "svc__kernel": ["linear", "rbf"],
}

grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X, y)

best_params = grid.best_params_
best_score = grid.best_score_

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:best_params_ 包含 svc__C 和 svc__kernel
    print(f"最佳参数: {best_params}")
    assert "svc__C" in best_params
    assert "svc__kernel" in best_params
    # 测试 2:best_score_ 在合理范围(> 0.9)
    print(f"最佳得分: {best_score:.4f}")
    assert best_score > 0.9
    print("全部测试通过!")
