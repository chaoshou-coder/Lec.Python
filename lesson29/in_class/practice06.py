"""
[难度: ⭐⭐⭐⭐]
[所属知识点: MNIST 完整训练 + 测试（train/val acc 曲线输出）]
[预计完成时间: 20 分钟]

把训练循环串完整: 5 epoch，打印 train/val 准确率曲线。

任务：
1) class MLP(nn.Module): fc1 = Linear(784, 256), relu,
   fc2 = Linear(256, 10)；
2) MNIST 用 5000 train + 1000 val 子集（加速）；
3) DataLoader batch_size=128, shuffle=True；
4) Adam lr=1e-3, CrossEntropyLoss；
5) 跑 5 epoch，每 epoch 计算 train acc 和 val acc；
6) 用纯文本（* 字符）打印准确率曲线，不用 matplotlib。
   例如: "Epoch 1: train ******** (70%) val ***** (40%)"

示例:
    >>> python3 practice06.py
    Epoch 1: train ******* (75%) val ****** (62%)
    Epoch 2: train ********* (88%) val ******* (79%)
    ...
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

torch.manual_seed(42)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x.view(-1)),
])
train_full = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
val_full = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)
train_set = Subset(train_full, range(5000))
val_set = Subset(val_full, range(1000))
train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
val_loader = DataLoader(val_set, batch_size=128, shuffle=False)


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        return self.net(x)


def compute_acc(model, loader):
    """计算准确率。"""
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in loader:
            out = model(data)
            pred = out.argmax(dim=1)
            correct += (pred == target).sum().item()
            total += target.size(0)
    return correct / total * 100


model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(1, 6):
    # 训练
    model.train()
    for data, target in train_loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
    # 评估
    train_acc = compute_acc(model, train_loader)
    val_acc = compute_acc(model, val_loader)
    star_n_train = int(train_acc // 10)
    star_n_val = int(val_acc // 10)
    print(
        f"Epoch {epoch}: "
        f"train {'*' * star_n_train} ({train_acc:.0f}%) "
        f"val {'*' * star_n_val} ({val_acc:.0f}%)"
    )

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 最终 val acc 应 > 70% (5 epoch on MNIST)
    final_val = compute_acc(model, val_loader)
    assert final_val > 70, f"val acc 太低: {final_val}"
    # 测试 2: 模型参数有效
    assert len(list(model.parameters())) == 4
    print(f"最终 val 准确率: {final_val:.2f}%")
    print("所有测试通过!")
