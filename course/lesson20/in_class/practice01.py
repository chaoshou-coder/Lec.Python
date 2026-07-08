"""
[难度: ⭐]
[所属知识点: MSE 公式]
[预计完成时间: 5 分钟]

题目描述:
实现函数 my_mse(y_true, y_pred),手动计算均方误差(MSE)。
公式: MSE = mean((y_true - y_pred)²)
请使用 numpy 完成计算。

示例:
    >>> import numpy as np
    >>> y_true = np.array([1, 3])
    >>> y_pred = np.array([2, 4])
    >>> my_mse(y_true, y_pred)
    1.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def my_mse(y_true, y_pred):
    """手动计算均方误差 MSE"""
    # 将输入转为 numpy 数组
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # 计算均方误差
    mse = np.mean((y_true - y_pred) ** 2)
    return mse


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本示例(期望 MSE=1.0)
    y_true = np.array([1, 3])
    y_pred = np.array([2, 4])
    result = my_mse(y_true, y_pred)
    print(f"测试1 - MSE: {result}")

    # 测试 2: 完美预测(边界)
    y_true2 = np.array([1, 2, 3])
    y_pred2 = np.array([1, 2, 3])
    result2 = my_mse(y_true2, y_pred2)
    print(f"测试2 - MSE: {result2}")

    # 测试 3: 较大误差
    y_true3 = np.array([10, 20, 30])
    y_pred3 = np.array([5, 15, 25])
    result3 = my_mse(y_true3, y_pred3)
    print(f"测试3 - MSE: {result3}")
