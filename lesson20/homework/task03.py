"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 线性回归解析解]
[预计完成时间: 20 分钟]

题目描述:
手写正规方程 normal_eq(X, y) 计算线性回归参数。
公式: θ = (X^T X)^(-1) X^T y
需要向 X 添加一列 1 用于表示截距项。
给定 X = [[1], [2], [3]], y = [2, 4, 6],
验证 θ = [0, 2](截距为 0, 系数为 2)。

提示: 使用 numpy.linalg.inv 求逆矩阵。

示例:
    >>> import numpy as np
    >>> X = np.array([[1], [2], [3]])
    >>> y = np.array([2, 4, 6])
    >>> theta = normal_eq(X, y)
    >>> # theta 接近 [0, 2]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def normal_eq(X, y):
    """使用正规方程计算线性回归参数"""
    X = np.array(X)
    y = np.array(y)
    # 向 X 添加一列 1(用于截距)
    ones = np.ones((X.shape[0], 1))
    X_b = np.hstack([ones, X])
    # 正规方程: θ = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    return theta


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: y = 2x (截距为 0, 系数为 2)
    print("测试1: y = 2x")
    X = np.array([[1], [2], [3]])
    y = np.array([2, 4, 6])
    theta = normal_eq(X, y)
    print(f"θ = {theta}")
    print(f"截距: {theta[0]:.4f} (期望 ~0)")
    print(f"系数: {theta[1]:.4f} (期望 ~2)")

    # 测试 2: y = 3x + 1 (边界: 非零截距)
    print("\n测试2: y = 3x + 1")
    X2 = np.array([[1], [2], [3], [4]])
    y2 = np.array([4, 7, 10, 13])
    theta2 = normal_eq(X2, y2)
    print(f"θ = {theta2}")
    print(f"截距: {theta2[0]:.4f} (期望 ~1)")
    print(f"系数: {theta2[1]:.4f} (期望 ~3)")

    # 测试 3: 验证与 sklearn 结果一致
    print("\n测试3: 与 sklearn 对比")
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    print(f"sklearn 系数: {model.coef_[0]:.4f}")
    print(f"sklearn 截距: {model.intercept_:.4f}")
    print(f"正规方程系数: {theta[1]:.4f}")
    print(f"正规方程截距: {theta[0]:.4f}")
