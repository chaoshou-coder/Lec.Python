"""
[难度: ⭐⭐⭐]
[所属知识点: 完整训练循环 / 反向传播实战]
[预计完成时间: 15 分钟]

XOR 问题是神经网络经典入门案例。单层感知机无法
解决 XOR，但含隐藏层的 MLP 可以完美拟合。

数据集: XOR 真值表
  X = [[0,0], [0,1], [1,0], [1,1]]
  y = [0, 1, 1, 0]

网络结构: 输入(2) → 隐藏层(8, ReLU) → 输出(1, Sigmoid)
损失函数: MSE
优化器: SGD, lr=0.1, 200 epochs

任务: 补全 forward、mse_loss、backward、sgd_update
四个函数，完成整个训练循环。每 40 epoch 打印损失。

示例:
    >>> # 期望输出:
    >>> # Epoch 0: loss = 0.2501
    >>> # Epoch 40: loss = 0.1987
    >>> # ...
    >>> # Epoch 200: loss ≈ 0.0012
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

    # XOR 数据集
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]],
                 dtype=np.float64)
    y = np.array([[0], [1], [1], [0]], dtype=np.float64)

    np.random.seed(0)
    # 初始化权重
    W1 = np.random.randn(2, 8) * np.sqrt(2.0 / 2)
    b1 = np.zeros((1, 8))
    W2 = np.random.randn(8, 1) * np.sqrt(2.0 / 8)
    b2 = np.zeros((1, 1))

    lr = 0.1
    n_epochs = 200

    # ---- 训练循环 ----
    for epoch in range(n_epochs):
        # 前向传播
        z1, a1, z2, a2 = forward(X, W1, b1, W2, b2)
        # 计算损失
        loss = mse_loss(a2, y)
        # 反向传播
        dW1, db1, dW2, db2 = backward(
            X, y, z1, a1, z2, a2, W2
        )
        # SGD 更新
        W1, b1, W2, b2 = sgd_update(
            W1, b1, W2, b2, dW1, db1, dW2, db2, lr
        )
        # 打印损失
        if epoch % 40 == 0 or epoch == n_epochs - 1:
            print(f"Epoch {epoch:>3d}: loss = {loss:.6f}")

    # 测试 1: 最终损失应足够小
    print("\n测试1 - 收敛检查")
    _, _, _, pred = forward(X, W1, b1, W2, b2)
    final_loss = mse_loss(pred, y)
    print(f"最终损失: {final_loss:.6f}")
    print(f"损失应小于 0.01: {final_loss < 0.01}")

    # 测试 2: 预测值应接近真实标签
    print("\n测试2 - 预测准确性")
    print("预测值:", pred.flatten())
    print("真实值:", y.flatten())
    pred_binary = (pred > 0.5).astype(int)
    accuracy = np.mean(pred_binary == y)
    print(f"准确率: {accuracy * 100:.1f}%")
    print(f"准确率应为 100%: {accuracy == 1.0}")
