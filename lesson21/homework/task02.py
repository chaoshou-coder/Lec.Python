"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 分类器对比]
[预计完成时间: 20 分钟]

题目: 用 load_iris(3 类)对比 LogisticRegression(max_iter=200)
和 DecisionTreeClassifier 的测试准确率。各跑 3 次取均值
(不同 random_state),输出对比表(含每次准确率和平均值)。

示例:
    >>> run()
      次数  逻辑回归  决策树
    0   1   0.97   0.93
    1   2   0.93   0.97
    2   3   0.97   0.93
    平均       0.96   0.94
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    seeds = [0, 1, 2]
    results = []

    for seed in seeds:
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=seed
        )

        lr = LogisticRegression(max_iter=200)
        lr.fit(X_train, y_train)
        lr_acc = lr.score(X_test, y_test)

        dt = DecisionTreeClassifier(random_state=seed)
        dt.fit(X_train, y_train)
        dt_acc = dt.score(X_test, y_test)

        results.append({
            "次数": seed + 1,
            "逻辑回归": round(lr_acc, 2),
            "决策树": round(dt_acc, 2),
        })

    df = pd.DataFrame(results)
    lr_avg = df["逻辑回归"].mean()
    dt_avg = df["决策树"].mean()
    print(df.to_string(index=False))
    print(f"平均       {lr_avg:.2f}   {dt_avg:.2f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两种分类器准确率都应较高
    run()
