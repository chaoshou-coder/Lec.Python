"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整神经网络训练 / Adam + Softmax]
[预计完成时间: 20 分钟]

鸢花 (Iris-like) 三特征二分类任务。生成 60 个样
本 (每类 30 个)，3 个输入特征，2 个输出类别。

完整流程:
  1. 生成数据并标准化
  2. 前向传播: 输入(3) → 隐藏层(4, ReLU) → 输出(2, Softmax)
  3. 交叉熵损失
  4. 反向传播: 手动推导完整链式法则
  5. Adam 优化器更新
  6. 训练 300 epoch，每 60 epoch 打印损失
  7. 输出最终准确率

示例:
    >>> # 期望输出:
    >>> # Epoch   0: loss=0.6931, acc=50.0%
    >>> # Epoch  60: loss=0.3214, acc=88.3%
    >>> # ...
    >>> # Epoch 300: loss=0.0891, acc=96.7%
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

    # ---- 数据生成 ----
    n_per_class = 30
    # 类别 0: 均值 [2, 3, 1]，标准差 0.5
    X0 = np.random.randn(n_per_class, 3) * 0.5 + [2, 3, 1]
    # 类别 1: 均值 [4, 5, 3]，标准差 0.5
    X1 = np.random.randn(n_per_class, 3) * 0.5 + [4, 5, 3]
    X = np.vstack([X0, X1])
    y = np.array([0] * n_per_class + [1] * n_per_class)
    n_samples = len(y)

    # One-hot 编码
    Y = np.zeros((n_samples, 2))
    Y[np.arange(n_samples), y] = 1

    # 标准化 (减均值除标准差)
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X_norm = (X - X_mean) / X_std

    # ---- 初始化参数 ----
    np.random.seed(0)
    input_dim = 3
    hidden_dim = 4
    output_dim = 2

    W1 = np.random.randn(input_dim, hidden_dim) * 0.1
    b1 = np.zeros(hidden_dim)
    W2 = np.random.randn(hidden_dim, output_dim) * 0.1
    b2 = np.zeros(output_dim)

    # ---- Adam 状态初始化 ----
    mt = {k: np.zeros_like(v) for k, v in
          [('W1', W1), ('b1', b1), ('W2', W2), ('b2', b2)]}
    vt = {k: np.zeros_like(v) for k, v in
          [('W1', W1), ('b1', b1), ('W2', W2), ('b2', b2)]}

    lr = 0.01
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    n_epochs = 300

    # ---- 训练循环 ----
    for epoch in range(n_epochs):
        # 前向传播
        z1 = X_norm @ W1 + b1
        a1 = np.maximum(0, z1)  # ReLU
        z2 = a1 @ W2 + b2
        # Softmax (数值稳定)
        z2_max = np.max(z2, axis=1, keepdims=True)
        exp_z = np.exp(z2 - z2_max)
        a2 = exp_z / np.sum(exp_z, axis=1, keepdims=True)

        # 交叉熵损失
        loss = -np.mean(np.sum(Y * np.log(a2 + 1e-8), axis=1))

        # 准确率
        pred_labels = np.argmax(a2, axis=1)
        acc = np.mean(pred_labels == y)

        if epoch % 60 == 0 or epoch == n_epochs - 1:
            print(f"Epoch {epoch:>3d}: "
                  f"loss = {loss:.4f}, "
                  f"acc = {acc * 100:.1f}%")

        # 反向传播
        dz2 = a2 - Y                       # (N, 2)
        dW2 = a1.T @ dz2 / n_samples       # (4, 2)
        db2 = np.mean(dz2, axis=0)         # (2,)
        dz1 = (dz2 @ W2.T) * (z1 > 0).astype(float)
        dW1 = X_norm.T @ dz1 / n_samples   # (3, 4)
        db1 = np.mean(dz1, axis=0)         # (4,)

        # Adam 更新
        t = epoch + 1
        grads = {'W1': dW1, 'b1': db1, 'W2': dW2, 'b2': db2}
        params = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
        for key in params:
            mt[key] = beta1 * mt[key] + (1 - beta1) * grads[key]
            vt[key] = beta2 * vt[key] + (1 - beta2) * grads[key] ** 2
            m_hat = mt[key] / (1 - beta1 ** t)
            v_hat = vt[key] / (1 - beta2 ** t)
            params[key] -= lr * m_hat / (np.sqrt(v_hat) + eps)
        W1, b1, W2, b2 = params['W1'], params['b1'], params['W2'], params['b2']

    # ---- 最终评估 ----
    print("\n" + "=" * 40)
    print("最终评估:")
    z1 = X_norm @ W1 + b1
    a1 = np.maximum(0, z1)
    z2 = a1 @ W2 + b2
    z2_max = np.max(z2, axis=1, keepdims=True)
    exp_z = np.exp(z2 - z2_max)
    a2 = exp_z / np.sum(exp_z, axis=1, keepdims=True)
    final_loss = -np.mean(np.sum(Y * np.log(a2 + 1e-8), axis=1))
    pred_labels = np.argmax(a2, axis=1)
    final_acc = np.mean(pred_labels == y)

    print(f"最终损失: {final_loss:.4f}")
    print(f"最终准确率: {final_acc * 100:.1f}%")

    # 测试 1: 准确率应大于 90%
    print(f"\n测试1 - 准确率达标: {final_acc > 0.9}")

    # 测试 2: 损失应明显小于初始
    print(f"测试2 - 损失下降: {final_loss < 0.3}")

    # 测试 3: 预测概率每行和为 1
    print(f"测试3 - 概率归一: {np.allclose(a2.sum(axis=1), 1.0)}")
