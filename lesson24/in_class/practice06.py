"""
[难度: ⭐⭐⭐]
[所属知识点: Pipeline]
[预计完成时间: 15 分钟]

题目: 加载 load_iris 数据,构建 Pipeline:
      第一步 scaler = StandardScaler(),
      第二步 clf = LogisticRegression(max_iter=200)。
      使用 cross_val_score(cv=5) 评估 Pipeline,
      输出平均准确率。

示例:
    >>> # 平均准确率约 0.95~0.98
"""
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
iris = load_iris()
X, y = iris.data, iris.target

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=200)),
])

scores = cross_val_score(pipe, X, y, cv=5)
mean_score = scores.mean()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Pipeline 含两个步骤
    print(f"Pipeline 步骤: {[name for name, _ in pipe.steps]}")
    assert len(pipe.steps) == 2
    # 测试 2:平均准确率 > 0.9
    print(f"平均准确率: {mean_score:.4f}")
    assert mean_score > 0.9
    print("全部测试通过!")
