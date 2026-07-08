"""
[难度: ⭐⭐]
[所属知识点: ★红灯 1 — 找 Bug：忘记 optimizer.zero_grad() 梯度累积]
[预计完成时间: 10 分钟]

下面这段训练循环有 Bug，loss 始终不下降。请找到原因并修复。
★教学红线 1：optimizer.zero_grad() 必须在每个 batch 前调用，
否则梯度会不断累积，导致 loss 震荡/不降。

任务：
1) 运行 BUGGY 版本，观察 loss 变化；
2) 修复代码（添加 optimizer.zero_grad()）；
3) 在合成数据 sklearn.make_classification 上对比；
4) 打印两个版本的最终 loss，FIXED 应明显更低。

示例:
    >>> python3 practice02.py
    BUG  最终 loss: 0.8712
    FIXED 最终 loss: 0.4321
    红灯 1 验证通过：FIXED 版 loss 正常下降。
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification

np.random.seed(42)
torch.manual_seed(42)

# 合成数据
X_np, y_np = make_classification(
    n_samples=500, n_features=10, n_classes=2, random_state=42
)
X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.float32).unsqueeze(1)


class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(10, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def run_train(use_zero_grad: bool, epochs: int = 8):
    """训练循环。use_zero_grad 控制是否清零梯度。"""
    model = TinyNet()
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    losses = []
    for epoch in range(epochs):
        # 学员请在此处实现：在 forward 前清零梯度
        if use_zero_grad:
            optimizer.zero_grad()
        out = model(X)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    return losses

# 运行两个版本
bug_losses = run_train(use_zero_grad=False)
fixed_losses = run_train(use_zero_grad=True)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 打印两个版本的 loss 对比
    for i in range(len(bug_losses)):
        print(
            f"Epoch {i+1} | "
            f"BUG loss={bug_losses[i]:.4f} | "
            f"FIXED loss={fixed_losses[i]:.4f}"
        )
    # 测试 2: FIXED 版最终 loss < 初始 loss
    assert fixed_losses[-1] < fixed_losses[0], (
        "FIXED 版 loss 应下降"
    )
    # 测试 3: FIXED 版最终 loss < BUG 版
    assert fixed_losses[-1] < bug_losses[-1], (
        "FIXED 应比 BUG 更低"
    )
    print("★ 红灯 1 验证通过：FIXED 版 loss 正常下降。")
