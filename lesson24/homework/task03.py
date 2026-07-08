"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 模型选择 / 流水线综合]
[预计完成时间: 20 分钟]

题目: 封装函数 find_best_model(X, y),
      使用 cross_val_score(cv=5) 评估以下三个模型
      (均用 Pipeline 包裹 StandardScaler):
      - LogisticRegression(max_iter=200)
      - SVC(kernel="rbf")
      - RandomForestClassifier(random_state=42)
      返回平均分最高的模型名(score 最高者)。

示例:
    >>> # 返回 ("LogisticRegression", 0.97) 等
"""
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def find_best_model(X, y, cv=5):
    """评估三个模型,返回 (最佳模型名, 平均分)"""
    candidates = {
        "LogisticRegression": Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=200)),
        ]),
        "SVC": Pipeline([
            ("scaler", StandardScaler()),
            ("clf", SVC(kernel="rbf")),
        ]),
        "RandomForestClassifier": Pipeline([
            ("scaler", StandardScaler()),
            ("clf", RandomForestClassifier(random_state=42)),
        ]),
    }

    best_name = None
    best_score = -1
    for name, pipe in candidates.items():
        scores = cross_val_score(pipe, X, y, cv=cv)
        mean_score = scores.mean()
        print(f"{name}: {mean_score:.4f}")
        if mean_score > best_score:
            best_score = mean_score
            best_name = name

    return best_name, best_score


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from sklearn.datasets import load_iris

    iris = load_iris()
    X, y = iris.data, iris.target

    name, score = find_best_model(X, y)
    # 测试 1:返回的模型名在候选列表中
    assert name in {
        "LogisticRegression", "SVC", "RandomForestClassifier"
    }
    # 测试 2:分数在合理范围
    print(f"最佳模型: {name},得分: {score:.4f}")
    assert 0.0 < score <= 1.0
    assert score > 0.9
    print("全部测试通过!")
