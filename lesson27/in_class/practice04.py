"""
[难度: ⭐⭐]
[所属知识点: 学习率对比 / 文本可视化]
[预计完成时间: 10 分钟]

学习率是训练神经网络的关键超参数。太大的学习率
会导致震荡甚至发散，太小的学习率收敛缓慢。

场景: 真实模型 y = 2x + 1 + 噪声，用 SGD 训练
简单线性模型 y = wx + b，对比学习率
lr = 0.001、0.01、0.1 的收敛情况。

任务: 用 '*' 字符绘制文本损失曲线，找出最优学习率。

示例:
    >>> # 输出示例 (损失曲线文本图)
    >>> # lr=0.001: ****.
    >>> # lr=0.01:  **..
    >>> # lr=0.1:   *#@! (震荡)
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
    x = np.linspace(0, 10, 50)
    y_true = 2 * x + 1 + np.random.randn(50) * 0.5

    lrs = [0.001, 0.01, 0.1]
    histories = {}

    # 学员需要在下方实现训练循环和文本绘图
    for lr in lrs:
        w, b = 0.0, 0.0
        losses = []
        for epoch in range(50):
            y_pred = w * x + b
            loss = np.mean((y_pred - y_true) ** 2)
            losses.append(loss)
            # 梯度
            dw = 2 * np.mean((y_pred - y_true) * x)
            db = 2 * np.mean(y_pred - y_true)
            w -= lr * dw
            b -= lr * db
        histories[lr] = losses

    # 测试 1: 打印最终损失
    print("测试1 - 各学习率最终损失:")
    for lr in lrs:
        final_loss = histories[lr][-1]
        print(f"  lr={lr}: 最终损失 = {final_loss:.4f}")

    # 测试 2: 判断哪个学习率收敛最快
    print("\n测试2 - 收敛速度比较:")
    for lr in lrs:
        min_loss = min(histories[lr])
        print(f"  lr={lr}: 最低损失 = {min_loss:.4f}")
