"""
[难度: ⭐⭐]
[所属知识点: sklearn.metrics]
[预计完成时间: 10 分钟]

题目描述:
使用 sklearn.metrics 中的 mean_squared_error 和 r2_score
重写 MSE 和 R² 的计算。给定数据,打印 MSE 和 R²,
验证与手动实现结果一致。

示例:
    >>> y_true = [1, 2, 3, 4, 5]
    >>> y_pred = [1.1, 2.2, 2.8, 4.1, 5.2]
    >>> # 打印的 MSE 约为 0.028
    >>> # 打印的 R² 约为 0.996
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def sklearn_metrics_demo(y_true, y_pred):
    """使用 sklearn 计算 MSE 和 R²"""
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"MSE: {mse:.6f}")
    print(f"R²:  {r2:.6f}")
    return mse, r2


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本示例
    y_true = [1, 2, 3, 4, 5]
    y_pred = [1.1, 2.2, 2.8, 4.1, 5.2]
    print("测试1:")
    mse, r2 = sklearn_metrics_demo(y_true, y_pred)

    # 测试 2: 完美预测(边界)
    print("\n测试2:")
    y_true2 = [10, 20, 30]
    y_pred2 = [10, 20, 30]
    sklearn_metrics_demo(y_true2, y_pred2)

    # 测试 3: 验证与手动实现一致
    print("\n测试3: 对比手动实现")
    y_true3 = np.array([3, 5, 7])
    y_pred3 = np.array([2.8, 5.1, 7.1])
    sklearn_mse = mean_squared_error(y_true3, y_pred3)
    manual_mse = np.mean((y_true3 - y_pred3) ** 2)
    print(f"sklearn MSE: {sklearn_mse:.6f}")
    print(f"手动实现 MSE: {manual_mse:.6f}")
