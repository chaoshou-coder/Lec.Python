"""
[难度: ⭐⭐]
[所属知识点: 模型持久化应用]
[预计完成时间: 10 分钟]

题目描述:
用 practice03 训练的 LinearRegression 模型,
通过 joblib.dump 保存为 "lr_model.joblib"。
然后在同一脚本中模拟"新建脚本"场景:
用 joblib.load 加载模型,对测试集前 5 条数据进行预测,
输出预测值与真实值的对比表。

示例:
    >>> # 预测值 vs 真实值对比(前 5 条)
    >>> # [2.7821, 2.1379, 2.4899, 2.0390, 1.9678]
    >>> # [3.450,  2.472,  2.582,  2.169,  1.808 ]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 加载数据并切分
housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练线性回归模型
lr = LinearRegression()
lr.fit(X_train, y_train)

# 保存模型到文件
joblib.dump(lr, "lr_model.joblib")

# ---- 模拟新建脚本: 加载模型并推理 ----
loaded_model = joblib.load("lr_model.joblib")
# 取测试集前 5 条
X_sample = X_test[:5]
y_true_sample = y_test[:5]
y_pred_sample = loaded_model.predict(X_sample)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出预测值与真实值对比
    print("===== 预测值 vs 真实值(前 5 条) =====")
    for i in range(5):
        print(f"  预测值: {y_pred_sample[i]:.4f}, "
              f"真实值: {y_true_sample[i]:.3f}")

    # 测试 2: 加载模型的预测应与原模型一致
    original_pred = lr.predict(X_sample)
    assert np.allclose(y_pred_sample, original_pred), \
        "加载模型预测与原模型不一致"
    print("\n测试通过: 加载模型与原模型预测完全一致")
