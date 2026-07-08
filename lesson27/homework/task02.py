"""
[难度: ⭐⭐⭐⭐]
[所属知识点: SGD vs Adam / 优化器对比]
[预计完成时间: 20 分钟]

在二维分类任务中比较 SGD 和 Adam 的收敛速度。
场景: 生成两个半月形数据集 (类似 sklearn.make_moons
的效果，但是纯 NumPy 实现)。

网络结构:
  输入(2) → 隐藏层(10, tanh) → 输出(2, Softmax)
损失函数: 交叉熵损失
优化器: SGD (lr=0.01) vs Adam (lr=0.01)
训练: 200 epochs

任务: 实现完整的训练流程，每 20 epoch 同时打印
两个优化器的损失，比较收敛速度。

示例:
    >>> # 期望输出:
    >>> # Epoch   0: SGD loss=0.6931 | Adam loss=0.6931
    >>> # Epoch  20: SGD loss=0.5123 | Adam loss=0.3891
    >>> # ...
    >>> # Adam 应明显比 SGD 收敛更快
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

    # 生成两个半月形数据 (N=200)
    n_samples = 200
    n = n_samples // 2

    # 上半月 (标签 0)
    theta1 = np.linspace(0, np.pi, n)
    x1 = np.cos(theta1) + np.random.randn(n) * 0.1
    y1 = np.sin(theta1) + np.random.randn(n) * 0.1

    # 下半月 (标签 1)
    theta2 = np.linspace(0, np.pi, n)
    x2 = 1 - np.cos(theta2) + np.random.randn(n) * 0.1
    y2 = -np.sin(theta2) + 0.5 + np.random.randn(n) * 0.1

    X = np.vstack([
        np.column_stack([x1, y1]),
        np.column_stack([x2, y2])
    ])
    y = np.array([0] * n + [1] * n)

    # One-hot 编码
    Y = np.zeros((n_samples, 2))
    Y[np.arange(n_samples), y] = 1

    # 标准化
    X = (X - X.mean(axis=0)) / X.std(axis=0)

    # 初始化两组相同权重
    def init_weights():
        np.random.seed(0)
        W1 = np.random.randn(2, 10) * 0.1
        b1 = np.zeros(10)
        W2 = np.random.randn(10, 2) * 0.1
        b2 = np.zeros(2)
        return W1, b1, W2, b2

    # ---- 训练 ----
    n_epochs = 200
    lr = 0.01

    # SGD 网络
    W1_s, b1_s, W2_s, b2_s = init_weights()
    # Adam 网络 (需要额外状态)
    W1_a, b1_a, W2_a, b2_a = init_weights()
    # Adam 状态初始化
    mt_W1, vt_W1 = np.zeros_like(W1_a), np.zeros_like(W1_a)
    mt_b1, vt_b1 = np.zeros_like(b1_a), np.zeros_like(b1_a)
    mt_W2, vt_W2 = np.zeros_like(W2_a), np.zeros_like(W2_a)
    mt_b2, vt_b2 = np.zeros_like(b2_a), np.zeros_like(b2_a)
    adam_state = {
        'mt_W1': mt_W1, 'vt_W1': vt_W1,
        'mt_b1': mt_b1, 'vt_b1': vt_b1,
        'mt_W2': mt_W2, 'vt_W2': vt_W2,
        'mt_b2': mt_b2, 'vt_b2': vt_b2,
    }

    for epoch in range(n_epochs):
        # SGD 前向
        z1_s = X @ W1_s + b1_s
        a1_s = np.tanh(z1_s)
        z2_s = a1_s @ W2_s + b2_s
        # softmax
        exp_s = np.exp(z2_s - np.max(z2_s, axis=1, keepdims=True))
        a2_s = exp_s / np.sum(exp_s, axis=1, keepdims=True)
        loss_sgd = -np.mean(np.sum(Y * np.log(a2_s + 1e-8), axis=1))

        # Adam 前向
        z1_a = X @ W1_a + b1_a
        a1_a = np.tanh(z1_a)
        z2_a = a1_a @ W2_a + b2_a
        exp_a = np.exp(z2_a - np.max(z2_a, axis=1, keepdims=True))
        a2_a = exp_a / np.sum(exp_a, axis=1, keepdims=True)
        loss_adam = -np.mean(np.sum(Y * np.log(a2_a + 1e-8), axis=1))

        if epoch % 20 == 0:
            print(f"Epoch {epoch:>3d}: "
                  f"SGD loss={loss_sgd:.4f} | "
                  f"Adam loss={loss_adam:.4f}")

        # SGD 反向传播
        dz2_s = a2_s - Y
        dW2_s = a1_s.T @ dz2_s / n_samples
        db2_s = np.mean(dz2_s, axis=0)
        dz1_s = (dz2_s @ W2_s.T) * (1 - np.tanh(z1_s) ** 2)
        dW1_s = X.T @ dz1_s / n_samples
        db1_s = np.mean(dz1_s, axis=0)
        W1_s -= lr * dW1_s
        b1_s -= lr * db1_s
        W2_s -= lr * dW2_s
        b2_s -= lr * db2_s

        # Adam 反向传播
        dz2_a = a2_a - Y
        dW2_a = a1_a.T @ dz2_a / n_samples
        db2_a = np.mean(dz2_a, axis=0)
        dz1_a = (dz2_a @ W2_a.T) * (1 - np.tanh(z1_a) ** 2)
        dW1_a = X.T @ dz1_a / n_samples
        db1_a = np.mean(dz1_a, axis=0)
        # Adam 更新 (简化版)
        t = epoch + 1
        beta1, beta2, eps = 0.9, 0.999, 1e-8
        for param, grad, key_mt, key_vt in [
            (W1_a, dW1_a, 'mt_W1', 'vt_W1'),
            (b1_a, db1_a, 'mt_b1', 'vt_b1'),
            (W2_a, dW2_a, 'mt_W2', 'vt_W2'),
            (b2_a, db2_a, 'mt_b2', 'vt_b2'),
        ]:
            adam_state[key_mt] = beta1 * adam_state[key_mt] + \
                (1 - beta1) * grad
            adam_state[key_vt] = beta2 * adam_state[key_vt] + \
                (1 - beta2) * grad ** 2
            m_hat = adam_state[key_mt] / (1 - beta1 ** t)
            v_hat = adam_state[key_vt] / (1 - beta2 ** t)
            param -= lr * m_hat / (np.sqrt(v_hat) + eps)

    # 测试 1: Adam 最终损失应小于 SGD
    print("\n测试1 - 最终损失对比")
    print(f"SGD  最终损失: {loss_sgd:.4f}")
    print(f"Adam 最终损失: {loss_adam:.4f}")
    print(f"Adam 收敛更快: {loss_adam < loss_sgd}")

    # 测试 2: 两者损失都应明显下降
    print("\n测试2 - 损失下降检查")
    print(f"SGD  损失 < 0.5: {loss_sgd < 0.5}")
    print(f"Adam 损失 < 0.5: {loss_adam < 0.5}")
