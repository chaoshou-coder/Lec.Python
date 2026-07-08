"""
[难度: ⭐⭐]
[所属知识点: R² 公式]
[预计完成时间: 10 分钟]

题目描述:
实现函数 my_r2(y_true, y_pred),手动计算决定系数 R²。
公式: R² = 1 - SS_res / SS_tot
其中 SS_res = sum((y_true - y_pred)²),
SS_tot = sum((y_true - mean(y_true))²)
请使用 numpy 完成计算。

示例:
    >>> import numpy as np
    >>> y_true = np.array([3, 5, 7])
    >>> y_pred = np.array([2.8, 5.1, 7.1])
    >>> round(my_r2(y_true, y_pred), 2)
    0.98
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def my_r2(y_true, y_pred):
    """手动计算决定系数 R²"""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # 计算残差平方和 SS_res
    ss_res = np.sum((y_true - y_pred) ** 2)
    # 计算总平方和 SS_tot
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    # 计算 R²
    r2 = 1 - ss_res / ss_tot
    return r2


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本示例
    y_true = np.array([3, 5, 7])
    y_pred = np.array([2.8, 5.1, 7.1])
    result = my_r2(y_true, y_pred)
    print(f"测试1 - R²: {result:.4f}")

    # 测试 2: 完美预测(边界)
    y_true2 = np.array([1, 2, 3, 4, 5])
    y_pred2 = np.array([1, 2, 3, 4, 5])
    result2 = my_r2(y_true2, y_pred2)
    print(f"测试2 - R²: {result2}")

    # 测试 3: 较差预测
    y_true3 = np.array([1, 2, 3])
    y_pred3 = np.array([3, 2, 1])
    result3 = my_r2(y_true3, y_pred3)
    print(f"测试3 - R²: {result3}")
