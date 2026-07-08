"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Early Stopping 类 + MNIST 训练]
[预计完成时间: 20 分钟]

题目描述:
    Early Stopping 是防止过拟合的关键技巧。当验证 loss
    连续 N 个 epoch 不再下降就提前终止训练。

任务:
    1) 定义 class EarlyStopping:
       __init__(patience=3, min_delta=1e-4):
           counter=0; best_loss=None
       __call__(self, val_loss, model):
           若 best_loss 为 None 或 val_loss < best_loss - min_delta:
               best_loss = val_loss; counter = 0
           否则: counter += 1
           返回 counter >= patience
    2) 训练 MNIST (5000 train, 1000 val),
       MLP(784->256->10), Adam lr=1e-3;
    3) 每 epoch 计算 val_loss，传给 EarlyStopping；
    4) 当触发停止，打印 "Early stopping at epoch X"；
    5) 最多跑 50 epoch（应提前停止）。

示例:
    >>> task03.py
    Epoch  1 | train_loss=0.3124 | val_loss=0.2891
    Epoch  2 | train_loss=0.2543 | val_loss=0.2410
    ...
    Early stopping at epoch 9
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

# 固定随机种子，保证可复现
torch.manual_seed(42)

# 数据加载
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


# MLP 网络
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


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

class EarlyStopping:
    """当验证 loss 连续 patience 次不下降则返回 True。"""

    def __init__(self, patience=3, min_delta=1e-4):
        # 学员请在此处实现
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None

    def __call__(self, val_loss, model):
        # 学员请在此处实现
        if self.best_loss is None:
            self.best_loss = val_loss
            self.counter = 0
        elif val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
        return self.counter >= self.patience


def train_one_epoch(model, loader, criterion, optimizer):
    """训练一个 epoch，返回平均 loss。"""
    model.train()
    total_loss = 0.0
    for data, target in loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * data.size(0)
    return total_loss / len(loader.dataset)


def evaluate_loss(model, loader, criterion):
    """在验证集上评估 loss。"""
    model.eval()
    total_loss = 0.0
    with torch.no_grad():
        for data, target in loader:
            out = model(data)
            loss = criterion(out, target)
            total_loss += loss.item() * data.size(0)
    return total_loss / len(loader.dataset)


def train_with_early_stopping(max_epochs=50):
    """完整训练流程，使用 EarlyStopping。"""
    model = MLP()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    early_stop = EarlyStopping(patience=3, min_delta=1e-4)

    for epoch in range(1, max_epochs + 1):
        train_loss = train_one_epoch(
            model, train_loader, criterion, optimizer
        )
        val_loss = evaluate_loss(model, val_loader, criterion)
        print(
            f"Epoch {epoch:>2} | "
            f"train_loss={train_loss:.4f} | "
            f"val_loss={val_loss:.4f}"
        )
        if early_stop(val_loss, model):
            print(f"Early stopping at epoch {epoch}")
            break
    return model


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == "__main__":
    # 测试 1: 训练应提前停止（< 50 epoch）
    model = train_with_early_stopping(max_epochs=50)
    print("★ Early Stopping 训练完成。")

    # 测试 2: 验证 EarlyStopping 类行为
    es = EarlyStopping(patience=2, min_delta=0.01)
    assert es(1.0, None) is False   # 首次，best_loss=1.0
    assert es(0.98, None) is False  # 下降不够，counter=1
    assert es(0.97, None) is True   # counter=2 >= patience
    print("★ EarlyStopping 类逻辑验证通过。")
