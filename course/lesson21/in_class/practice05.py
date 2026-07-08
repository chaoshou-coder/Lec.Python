"""
[难度: ⭐⭐⭐]
[所属知识点: 树深度 / 过拟合]
[预计完成时间: 15 分钟]

题目: 用 load_iris 数据,分别设置 max_depth = 1/2/3/5/None
训练 DecisionTreeClassifier,记录每种情况下训练集和测试集
准确率。返回 DataFrame 展示过拟合趋势。
提示: 观察 max_depth=None 时训练集准确率与测试集的差距。

示例:
    >>> df = run()
    >>> print(df)
       max_depth  训练集准确率  测试集准确率
    0          1       0.68       0.66
    1          2       0.96       0.93
    2          3       0.98       0.97
    3          5       1.00       0.97
    4       None       1.00       0.95
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    depths = [1, 2, 3, 5, None]
    results = []

    for d in depths:
        model = DecisionTreeClassifier(max_depth=d, random_state=42)
        model.fit(X_train, y_train)
        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)
        results.append({
            "max_depth": d,
            "训练集准确率": round(train_acc, 2),
            "测试集准确率": round(test_acc, 2),
        })

    df = pd.DataFrame(results)
    return df

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 查看不同 max_depth 下的过拟合趋势
    df = run()
    print(df)
