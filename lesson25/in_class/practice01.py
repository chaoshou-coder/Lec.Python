"""
[难度: ⭐]
[所属知识点: joblib 保存模型]
[预计完成时间: 5 分钟]

题目描述:
用 sklearn 的 load_iris 数据集 + LogisticRegression 训练一个小模型,
用 joblib.dump 保存为 "iris_model.joblib"。
再用 joblib.load 加载,验证加载后的模型与原模型在相同输入上
的预测是否一致(用 allclose 或 array_equal 判断)。

示例:
    >>> # 训练集上取前 5 条验证预测是否一致
    >>> # np.array_equal(original_pred, loaded_pred) -> True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
import joblib  # 练习使用 joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 加载 iris 数据
iris = load_iris()
X, y = iris.data, iris.target

# 训练 LogisticRegression 模型
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 用 joblib.dump 保存模型到 "iris_model.joblib"
joblib.dump(model, "iris_model.joblib")

# 用 joblib.load 加载模型
loaded_model = joblib.load("iris_model.joblib")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 原始模型与加载模型在训练集上前 5 条预测一致
    original_pred = model.predict(X[:5])
    loaded_pred = loaded_model.predict(X[:5])
    assert np.array_equal(original_pred, loaded_pred), "预测不一致"
    print("测试 1 通过: 原始模型与加载模型预测一致")

    # 测试 2: 在全量数据上预测结果也一致
    full_original = model.predict(X)
    full_loaded = loaded_model.predict(X)
    assert np.array_equal(full_original, full_loaded), "全量预测不一致"
    print("测试 2 通过: 全量数据预测一致, joblib 保存/加载成功")
