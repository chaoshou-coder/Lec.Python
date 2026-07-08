"""
[难度: ⭐⭐]
[所属知识点: Adam 优化器 / 偏差校正]
[预计完成时间: 10 分钟]

Adam 是目前最常用的优化器，它结合了动量和自适应
学习率。单步更新规则:

mt = β1 * mt + (1 - β1) * dW        # 一阶矩估计
vt = β2 * vt + (1 - β2) * dW^2      # 二阶矩估计
m̂t = mt / (1 - β1^t)                # 偏差校正
v̂t = vt / (1 - β2^t)                # 偏差校正
W  = W - lr * m̂t / (√v̂t + ε)

任务: 实现 adam_update 函数，返回更新后的
(W, mt, vt)。验证第一步的偏差校正。

示例:
    >>> W = np.array([0.5, -0.3])
    >>> dW = np.array([0.1, -0.2])
    >>> mt = np.zeros(2)
    >>> vt = np.zeros(2)
    >>> adam_update(W, dW, mt, vt, t=1, lr=0.001)
    (array([0.499, -0.299]), array([0.01, -0.02]),
     array([0.0001, 0.0004]))
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ==========================
# 测试区(教师可复制到终端验证)
# ==========================
if __name__ == '__main__':
    import numpy as np

    np.random.seed(42)
    W = np.random.randn(3, 2)
    dW = np.random.randn(3, 2) * 0.1
    mt = np.zeros_like(W)
    vt = np.zeros_like(W)

    # 测试 1: 第一步 Adam 更新
    W1, mt1, vt1 = adam_update(
        W.copy(), dW, mt, vt, t=1, lr=0.001
    )
    print("测试1 - Adam 第一步")
    print("原始 W[0]:", W[0])
    print("更新后 W[0]:", W1[0])
    print("mt[0]:", mt1[0])
    print("vt[0]:", vt1[0])

    # 测试 2: 连续两步更新，观察偏差校正效果
    W2, mt2, vt2 = adam_update(
        W1.copy(), dW, mt1.copy(), vt1.copy(),
        t=2, lr=0.001
    )
    print("\n测试2 - Adam 第二步")
    print("更新后 W[0]:", W2[0])
    print("mt 在第二步应该更大(累积):", mt2[0])
    print("mt[0,0] > mt1[0,0]:", mt2[0, 0] > mt1[0, 0])
