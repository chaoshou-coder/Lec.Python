"""
[难度: ⭐⭐]
[所属知识点: SGD 更新规则 / 动量 SGD]
[预计完成时间: 10 分钟]

在神经网络训练中，梯度下降是最基础的优化方法。
给定权重 W、梯度 dW 和学习率 lr，更新规则为:
W = W - lr * dW

此外，动量 SGD 引入速度变量 v 来加速收敛:
v = beta * v + dW
W = W - lr * v

任务: 实现普通 SGD 和动量 SGD 两种更新函数。

示例:
    >>> W = np.array([[0.1, 0.2], [0.3, 0.4]])
    >>> dW = np.array([[0.01, 0.02], [0.03, 0.04]])
    >>> sgd_update(W, dW, lr=0.01)
    array([[0.0999, 0.1998], [0.2997, 0.3996]])
    >>> momentum_sgd_update(W, dW, v=np.zeros_like(W), lr=0.01, beta=0.9)
    (updated_W, updated_v)
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

    np.random.seed(0)
    W = np.random.randn(3, 4)
    dW = np.random.randn(3, 4) * 0.01

    # 测试 1: 普通 SGD
    W_new = W.copy()
    W_new = sgd_update(W_new, dW, lr=0.01)
    print("测试1 - 普通 SGD")
    print("更新前 W[0,0]:", W[0, 0])
    print("更新后 W[0,0]:", W_new[0, 0])
    print("差值应约为 lr*dW =", 0.01 * dW[0, 0])

    # 测试 2: 动量 SGD (第一次迭代, v 初始为零)
    W_new2 = W.copy()
    v = np.zeros_like(W)
    W_new2, v_new = momentum_sgd_update(
        W_new2, dW, v, lr=0.01, beta=0.9
    )
    print("\n测试2 - 动量 SGD (首次)")
    print("更新后 W[0,0]:", W_new2[0, 0])
    print("速度 v[0,0]:", v_new[0, 0])
    print("v 应等于 dW (因为 v 从零开始):", np.allclose(v_new, dW))
