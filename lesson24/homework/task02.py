"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 多分类综合评估]
[预计完成时间: 20 分钟]

题目: 加载 load_iris 数据(多分类),训练 LogisticRegression,
      编写函数 full_report(y_true, y_pred) 返回字典,包含:
      - accuracy (accuracy_score)
      - precision (precision_score, average="macro")
      - recall (recall_score, average="macro")
      - f1 (f1_score, average="macro")

示例:
    >>> # 返回类似
    >>> # {"accuracy": 0.96, "precision": 0.96,
    >>> #  "recall": 0.96, "f1": 0.96}
"""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)
y_pred = model.predict(X)


def full_report(y_true, y_pred):
    """返回多分类综合评估字典"""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
        "recall": recall_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
        "f1": f1_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
    }


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    report = full_report(y, y_pred)
    print("综合报告:")
    for k, v in report.items():
        print(f"  {k}: {v:.4f}")
    # 测试 1:四个指标都存在
    assert set(report.keys()) == {
        "accuracy", "precision", "recall", "f1"
    }
    # 测试 2:所有指标在 (0, 1] 内
    assert all(0 < v <= 1.0 for v in report.values())
    # 测试 3:集束预测指标应较高(> 0.9)
    assert report["accuracy"] > 0.9
    print("全部测试通过!")
