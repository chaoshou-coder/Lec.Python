"""
[难度: ⭐⭐⭐]
[所属知识点: 验证循环 + model.eval() 对 Dropout 的影响]
[预计完成时间: 15 分钟]

题目描述:
    小红的验证准确率每次跑都不一样，波动很大。原来她忘了
    在验证前调 model.eval()。
    ★教学红线 2：推理/验证时必须调 model.eval()，让 Dropout
    停止随机丢弃、BatchNorm 使用全局统计。否则每次验证结果
    不同，无法公平比较。

任务:
    1) 定义含 nn.Dropout(0.5) 的网络：
       Linear(784,128)->ReLU->Dropout->Linear(128,10)；
    2) 在 MNIST 子集 (train 2000, val 400) 上训练 3 epoch；
    3) 在 val 上跑 3 次评估：
       a) 不调 eval()（错）  b) 调 eval()+no_grad()（对）
       打印 6 个准确率，展示错的结果波动大、对的结果一致。

示例:
    >>> task02.py
    [错] 第 1 次验证准确率: 80.25%
    [错] 第 2 次验证准确率: 73.50%
    [错] 第 3 次验证准确率: 81.00%
    [对] 第 1 次验证准确率: 85.25%
    [对] 第 2 次验证准确率: 85.25%
    [对] 第 3 次验证准确率: 85.25%
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
    transforms.Lambda(lambda x: x.view(-1)),  # 展平 28*28=784
])
train_full = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
val_full = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)
train_set = Subset(train_full, range(2000))
val_set = Subset(val_full, range(400))
train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
val_loader = DataLoader(val_set, batch_size=128, shuffle=False)


# 含 Dropout 的网络
class DropoutNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10),
        )

    def forward(self, x):
        return self.net(x)


def train_model(model, loader, epochs=3):
    """简单训练若干 epoch。"""
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    model.train()
    for epoch in range(epochs):
        for data, target in loader:
            optimizer.zero_grad()
            out = model(data)
            loss = criterion(out, target)
            loss.backward()
            optimizer.step()


def evaluate(model, loader, use_eval=False):
    """在验证集上评估，use_eval 控制是否调 model.eval()。"""
    correct = 0
    total = 0
    if use_eval:
        model.eval()
    with torch.no_grad():
        for data, target in loader:
            out = model(data)
            pred = out.argmax(dim=1)
            correct += (pred == target).sum().item()
            total += target.size(0)
    return correct / total * 100


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 学员请在此处实现：调用训练与评估函数，完成对比
model = DropoutNet()
train_model(model, train_loader, epochs=3)

wrong_accs = []
correct_accs = []
for i in range(3):
    acc_wrong = evaluate(model, val_loader, use_eval=False)
    acc_correct = evaluate(model, val_loader, use_eval=True)
    wrong_accs.append(acc_wrong)
    correct_accs.append(acc_correct)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == "__main__":
    # 测试 1: 错的结果（不调 eval）应波动
    print("=" * 50)
    print("★ 红灯 2 演示：忘记 model.eval() 验证准确率波动大")
    print("=" * 50)
    for i, acc in enumerate(wrong_accs, 1):
        print(f"[错] 第 {i} 次验证准确率: {acc:.2f}%")

    # 测试 2: 对的结果（调 eval + no_grad）应一致
    print("=" * 50)
    print("★ 正确做法：model.eval() + no_grad() 结果稳定")
    print("=" * 50)
    for i, acc in enumerate(correct_accs, 1):
        print(f"[对] 第 {i} 次验证准确率: {acc:.2f}%")

    # 验证：正确做法的三次结果波动应很小
    correct_std = torch.tensor(correct_accs).std().item()
    print(f"★ 正确做法 3 次准确率标准差: {correct_std:.4f}")
