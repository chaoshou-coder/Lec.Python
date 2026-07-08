"""
[难度: ⭐⭐]
[所属知识点: DecisionTreeClassifier]
[预计完成时间: 10 分钟]

题目: 使用 load_iris 全套数据(150 条,3 类),
用 DecisionTreeClassifier(max_depth=3) 训练模型。
输出测试集准确率,并打印特征重要性(feature_importances_)。

示例:
    >>> run()
    测试集准确率: 0.97
    花萼长度 (cm) 重要性: 0.00
    花萼宽度 (cm) 重要性: 0.02
    花瓣长度 (cm) 重要性: 0.55
    花瓣宽度 (cm) 重要性: 0.43
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # 1. 创建决策树模型,max_depth=3
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 2. 输出测试集准确率
    acc = model.score(X_test, y_test)
    print(f"测试集准确率: {acc:.2f}")

    # 3. 打印每个特征的重要性
    for name, score in zip(iris.feature_names,
                           model.feature_importances_):
        print(f"{name} 重要性: {score:.2f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常运行,准确率应在 0.9 以上
    run()
