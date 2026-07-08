"""
[难度: ⭐⭐⭐]
[所属知识点: 反向传播 / 梯度计算]
[预计完成时间: 15 分钟]

反向传播是神经网络训练的核心。给定上游梯度 da2
(Softmax 输出的误差信号) 和前向传播的缓存，
计算所有权重的梯度。

梯度计算链:
  dz2 = da2                               # Softmax+MSE 简化
  dW2 = a1.T @ dz2                        # (4, N) @ (N, 2) = (4, 2)
  db2 = sum(dz2, axis=0)                  # (2,)
  dz1 = (dz2 @ W2.T) * relu'(z1)          # (N, 4)
  dW1 = x.T @ dz1                         # (3, N) @ (N, 4) = (3, 4)
  db1 = sum(dz1, axis=0)                  # (4,)

任务: 实现 backward 函数，返回所有梯度。

示例:
    >>> grads = backward(da2, cache, W2)
    >>> dW1, db1, dW2, db2 = grads
    >>> # 梯度形状应与权重形状一致
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import numpy as np

    np.random.seed(42)
    W1 = np.random.randn(3, 4) * 0.1
    b1 = np.zeros(4)
    W2 = np.random.randn(4, 2) * 0.1
    b2 = np.zeros(2)

    # 前向传播生成缓存
    x = np.array([[1, 2, 3], [4, 5, 6]])
    z1 = x @ W1 + b1
    a1 = np.maximum(0, z1)
    z2 = a1 @ W2 + b2
    # softmax
    exp_z = np.exp(z2 - np.max(z2, axis=1, keepdims=True))
    a2 = exp_z / np.sum(exp_z, axis=1, keepdims=True)

    # 模拟上游梯度 (真实标签与预测之差)
    da2 = a2 - np.array([[1, 0], [0, 1]])

    cache = (x, z1, a1, z2, a2)

    # 测试 1: 梯度形状验证
    dW1, db1, dW2, db2 = backward(da2, cache, W2)
    print("测试1 - 梯度形状验证")
    print("dW1 形状:", dW1.shape, "(应为 (3,4))")
    print("db1 形状:", db1.shape, "(应为 (4,))")
    print("dW2 形状:", dW2.shape, "(应为 (4,2))")
    print("db2 形状:", db2.shape, "(应为 (2,))")

    # 测试 2: 梯度数值不为零 (确认反向传播正确)
    print("\n测试2 - 梯度数值检查")
    print("dW1 不应全为零:", not np.allclose(dW1, 0))
    print("dW2 不应全为零:", not np.allclose(dW2, 0))
    print("db1 不应全为零:", not np.allclose(db1, 0))
    print("db2 不应全为零:", not np.allclose(db2, 0))
