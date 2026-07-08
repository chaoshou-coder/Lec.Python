"""
[难度: ⭐⭐]
[所属知识点: LinearRegression fit/predict]
[预计完成时间: 10 分钟]

题目描述:
使用 sklearn.linear_model.LinearRegression 拟合数据。
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]
训练后输出 coef_(系数) 和 intercept_(截距),
并预测 x=6 时的 y 值。
理论结果: coef=2.0, intercept=0.0。

示例:
    >>> # coef_ 约为 [2.]
    >>> # intercept_ 约为 0.
    >>> # 预测 x=6 的结果为 [12.]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.linear_model import LinearRegression
import numpy as np


def simple_linear_fit():
    """使用 LinearRegression 拟合简单数据"""
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    # 创建并训练模型
    model = LinearRegression()
    model.fit(X, y)
    # 输出参数
    print(f"coef_: {model.coef_}")
    print(f"intercept_: {model.intercept_}")
    # 预测 x=6
    x_test = np.array([[6]])
    y_pred = model.predict(x_test)
    print(f"预测 x=6: {y_pred}")
    return model


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本拟合
    print("测试1: y = 2x 拟合")
    model = simple_linear_fit()

    # 测试 2: 验证参数
    print("\n测试2: 验证参数值")
    print(f"系数是否接近 2.0: "
          f"{np.isclose(model.coef_[0], 2.0)}")
    print(f"截距是否接近 0.0: "
          f"{np.isclose(model.intercept_, 0.0)}")

    # 测试 3: 预测多个值
    print("\n测试3: 预测 x=[6, 7, 8]")
    X_new = np.array([[6], [7], [8]])
    y_new = model.predict(X_new)
    print(f"预测结果: {y_new}")
