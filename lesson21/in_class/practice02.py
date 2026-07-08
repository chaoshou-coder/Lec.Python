"""
[难度: ⭐⭐]
[所属知识点: predict_proba]
[预计完成时间: 10 分钟]

题目: 延续 practice01,用 predict_proba 查看前 5 个测试样本
属于两个类别的概率,并对比 predict 输出结果。
说明 predict 取的是概率更大的类别。

示例:
    >>> run()
    样本 0: 类别 0 概率 0.95, 类别 1 概率 0.05, 预测类别: 0
    样本 1: 类别 0 概率 0.12, 类别 1 概率 0.88, 预测类别: 1
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X = iris.data[:100, :2]
    y = iris.target[:100]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 1. predict_proba 获取前 5 个样本的概率
    proba = model.predict_proba(X_test[:5])

    # 2. predict 获取前 5 个样本的预测类别
    preds = model.predict(X_test[:5])

    # 3. 逐样本打印概率与预测结果
    for i in range(5):
        print(
            f"样本 {i}: 类别 0 概率 {proba[i][0]:.2f}, "
            f"类别 1 概率 {proba[i][1]:.2f}, "
            f"预测类别: {preds[i]}"
        )

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常输出 5 个样本的概率和预测
    run()
