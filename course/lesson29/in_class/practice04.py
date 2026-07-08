"""
[难度: ⭐⭐⭐]
[所属知识点: MNIST 分类网络（含 Dropout），训练 1 epoch + train/val loss]
[预计完成时间: 15 分钟]

用 MNIST 训练一个含 Dropout 的网络，理解 train/val 差异。

任务：
1) 定义 class Net(nn.Module):
   fc1 = Linear(784, 256), relu, Dropout(0.3),
   fc2 = Linear(256, 10)；
2) MNIST 子集 train 3000 + val 600 加速；
3) DataLoader batch_size=128；
4) Adam lr=1e-3, CrossEntropyLoss；
5) 训练 1 epoch，结束后在 train 和 val 上计算平均 loss；
6) 打印 train_loss 和 val_loss。

示例:
    >>> python3 practice04.py
    train_loss: 0.2341
    val_loss: 0.3124
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
train_set = Subset(train_full, range(3000))
val_set = Subset(val_full, range(600))
train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
val_loader = DataLoader(val_set, batch_size=128, shuffle=False)


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        return self.net(x)


model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 训练 1 epoch
model.train()
for data, target in train_loader:
    optimizer.zero_grad()
    out = model(data)
    loss = criterion(out, target)
    loss.backward()
    optimizer.step()

# 评估 train loss
model.eval()
total_loss = 0.0
total_samples = 0
with torch.no_grad():
    for data, target in train_loader:
        out = model(data)
        loss = criterion(out, target)
        total_loss += loss.item() * data.size(0)
        total_samples += data.size(0)
train_loss = total_loss / total_samples

# 评估 val loss
total_loss = 0.0
total_samples = 0
with torch.no_grad():
    for data, target in val_loader:
        out = model(data)
        loss = criterion(out, target)
        total_loss += loss.item() * data.size(0)
        total_samples += data.size(0)
val_loss = total_loss / total_samples

print(f"train_loss: {train_loss:.4f}")
print(f"val_loss: {val_loss:.4f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: loss 是有限正数
    assert 0 < train_loss < 10
    assert 0 < val_loss < 10
    # 测试 2: 模型参数存在
    assert len(list(model.parameters())) == 4
    print("所有测试通过!")
