"""
[难度: ⭐]
[所属知识点: LogisticRegression 二分类基础]
[预计完成时间: 5 分钟]

题目: 用 sklearn.datasets.load_iris 加载数据,只取前 100 条
(两个类别: Setosa 和 Versicolor),特征为"花萼长度"和
"花萼宽度"。用 LogisticRegression 训练二分类模型,
输出测试集准确率。

示例:
    >>> run()
    测试集准确率: 1.0
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    # 1. 加载 iris 数据,只取前 100 条(两个类别)
    iris = load_iris()
    X = iris.data[:100, :2]  # 花萼长度、花萼宽度
    y = iris.target[:100]

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. 训练逻辑回归模型
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 4. 输出测试集准确率
    acc = model.score(X_test, y_test)
    print(f"测试集准确率: {acc}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常运行,准确率应接近 1.0
    run()
