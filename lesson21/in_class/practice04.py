"""
[难度: ⭐⭐]
[所属知识点: plot_tree]
[预计完成时间: 10 分钟]

题目: 在 practice03 的基础上,使用 sklearn.tree.plot_tree
画出决策树(设置 filled=True, feature_names=iris.feature_names,
class_names=list(iris.target_names))。保存为 iris_tree.png。

示例:
    >>> run()
    决策树已保存为 iris_tree.png
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 1. 绘制决策树并保存
    plt.figure(figsize=(12, 8))
    plot_tree(
        model,
        filled=True,
        feature_names=iris.feature_names,
        class_names=list(iris.target_names),
    )
    plt.savefig("iris_tree.png", bbox_inches="tight")
    print("决策树已保存为 iris_tree.png")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常生成图片文件
    run()
