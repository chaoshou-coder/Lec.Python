"""
[难度: ⭐⭐]
[所属知识点: 训练循环 + optimizer.zero_grad() 梯度累积 Bug]
[预计完成时间: 10 分钟]

题目描述:
    小明的训练 loss 一直不降。他写了以下训练循环，请你
    帮他诊断并修复。
    ★教学红线 1：optimizer.zero_grad() 必须在每个 batch 的
    forward 前调用。忘记它会让梯度不断累积，loss 震荡甚至
    发散。修复方法：在 optimizer.step() 之后（或下次 forward
    前）调用 optimizer.zero_grad()。

任务:
    1) 写一个有 BUG 的版本（故意漏掉 zero_grad）和一个
       FIXED 版本；
    2) 在合成数据 sklearn.make_classification
       (n_samples=300, n_features=8, 2 classes) 上分别
       跑 10 epoch；
    3) 打印每个 epoch 的两个 loss，对比；
    4) 验证：BUG 版 loss 不降或震荡，FIXED 版 loss 下降。

示例:
    >>> task01.py
    Epoch  1 | BUG loss=0.7123 | FIXED loss=0.6912
    Epoch  2 | BUG loss=0.8541 | FIXED loss=0.6701
    ...
    Epoch 10 | BUG loss=0.9012 | FIXED loss=0.4210
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification

# 固定随机种子，保证可复现
np.random.seed(42)
torch.manual_seed(42)

# 合成数据集
X, y = make_classification(
    n_samples=300, n_features=8,
    n_classes=2, random_state=42
)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)


# 简单的二分类网络
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(8, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def train_bug_or_fixed(use_zero_grad: bool, epochs: int = 10):
    """训练一个 epoch，返回每 epoch 平均 loss 列表。
    use_zero_grad=True 时在每个 batch 前清零梯度。
    """
    model = SimpleNet()
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    losses = []
    for epoch in range(1, epochs + 1):
        # 学员请在此处实现
        if use_zero_grad:
            optimizer.zero_grad()
        out = model(X)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    return losses


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == "__main__":
    # 测试 1: 有 BUG 版本（不清零梯度）
    print("=" * 50)
    print("BUG 版（忘记 zero_grad）训练开始")
    print("=" * 50)
    bug_losses = train_bug_or_fixed(use_zero_grad=False)
    for i, loss in enumerate(bug_losses, 1):
        print(f"Epoch {i:>2} | BUG   loss={loss:.4f}")

    # 测试 2: FIXED 版本（正确清零梯度）
    print("=" * 50)
    print("FIXED 版（正确 zero_grad）训练开始")
    print("=" * 50)
    fixed_losses = train_bug_or_fixed(use_zero_grad=True)
    for i, loss in enumerate(fixed_losses, 1):
        print(f"Epoch {i:>2} | FIXED loss={loss:.4f}")

    # 测试 3: 对比输出
    print("=" * 50)
    print("对比：BUG 最终 loss =", f"{bug_losses[-1]:.4f}")
    print("对比：FIXED 最终 loss =", f"{fixed_losses[-1]:.4f}")
    assert fixed_losses[-1] < fixed_losses[0], (
        "FIXED 版 loss 应下降"
    )
    print("★ 红灯 1 验证通过：FIXED 版 loss 正常下降。")
