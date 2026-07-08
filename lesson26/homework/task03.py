"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 两层 MLP 完整训练循环 / MSE / SGD]
[预计完成时间: 20 分钟]

客户流失预测:输入 3 维特征,隐藏层 8 个神经元用 ReLU,
输出层 1 个神经元用 Sigmoid。网络 input(3) → hidden(8)
→ output(1)。用随机数据(n=100)训练 200 epoch,lr=0.01,
MSE 损失,SGD 更新。请实现完整的 forward + loss +
backward + update 循环,每 40 epoch 打印 loss。

示例:
    >>> train_churn()
    epoch=0    loss=0.30
    epoch=40   loss=0.22
    epoch=80   loss=0.18
    epoch=120  loss=0.15
    epoch=160  loss=0.13
    epoch=199   loss=0.11
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 完整训练 200 epoch,loss 递减
    # 测试 2: 最终 loss < 初始 loss 的一半
    pass
