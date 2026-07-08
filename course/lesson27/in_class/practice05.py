"""
[难度: ⭐⭐⭐]
[所属知识点: 前向传播 / 多层神经网络]
[预计完成时间: 15 分钟]

二分类神经网络的前向传播。输入 3 个特征，隐藏层
4 个神经元 (ReLU 激活)，输出 2 个类别 (Softmax)。

网络结构:
  z1 = x @ W1 + b1        # (N, 3) @ (3, 4) + (4,) = (N, 4)
  a1 = relu(z1)           # (N, 4)
  z2 = a1 @ W2 + b2       # (N, 4) @ (4, 2) + (2,) = (N, 2)
  a2 = softmax(z2)        # (N, 2)

任务: 实现 forward 函数，返回所有中间值。

示例:
    >>> x = np.array([[1, 2, 3]])
    >>> z1, a1, z2, a2 = forward(x)
    >>> a2 应满足每行概率和为 1
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

    # 测试 1: 单样本输入
    x1 = np.array([[1, 2, 3]])
    z1, a1, z2, a2 = forward(x1, W1, b1, W2, b2)
    print("测试1 - 单样本前向传播")
    print("输入形状:", x1.shape)
    print("z1 形状:", z1.shape)
    print("a1 形状:", a1.shape)
    print("z2 形状:", z2.shape)
    print("a2 (Softmax输出):", a2)
    print("概率和:", np.sum(a2, axis=1))

    # 测试 2: 批量输入
    x_batch = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    z1_b, a1_b, z2_b, a2_b = forward(
        x_batch, W1, b1, W2, b2
    )
    print("\n测试2 - 批量前向传播")
    print("输入形状:", x_batch.shape)
    print("a2 形状:", a2_b.shape)
    print("每行概率和:", np.sum(a2_b, axis=1))
    print("概率和应都为 1.0")
