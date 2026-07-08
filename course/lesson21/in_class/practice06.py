"""
[难度: ⭐⭐⭐]
[所属知识点: RandomForestClassifier]
[预计完成时间: 15 分钟]

题目: 用 load_iris 对比单棵 DecisionTreeClassifier
和 RandomForestClassifier(n_estimators=100) 在测试集上的
准确率。重复 5 次取平均(不同 random_state 切分),
验证集成学习效果更好。
提示: 每次用不同 random_state 切分数据再训练。

示例:
    >>> run()
    决策树 5 次平均测试准确率: 0.94
    随机森林 5 次平均测试准确率: 0.96
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    dt_scores = []
    rf_scores = []

    # 1. 重复 5 次实验,每次用不同的 random_state
    for seed in range(5):
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=seed
        )

        dt = DecisionTreeClassifier(random_state=seed)
        dt.fit(X_train, y_train)
        dt_scores.append(dt.score(X_test, y_test))

        rf = RandomForestClassifier(n_estimators=100, random_state=seed)
        rf.fit(X_train, y_train)
        rf_scores.append(rf.score(X_test, y_test))

    # 2. 计算并打印平均准确率
    dt_avg = sum(dt_scores) / len(dt_scores)
    rf_avg = sum(rf_scores) / len(rf_scores)
    print(f"决策树 5 次平均测试准确率: {dt_avg:.2f}")
    print(f"随机森林 5 次平均测试准确率: {rf_avg:.2f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 随机森林平均准确率通常高于单棵决策树
    run()
