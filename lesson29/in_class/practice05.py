"""
[难度: ⭐⭐⭐]
[所属知识点: ★红灯 2 — 忘记 model.eval() 导致 Dropout 在验证时生效]
[预计完成时间: 15 分钟]

验证时如果忘记调 model.eval()，Dropout 会继续随机丢弃神经
元，导致准确率波动。
★教学红线 2：验证/测试阶段必须调 model.eval()，让 Dropout
和 BatchNorm 切换到推理模式。

任务：
1) 定义含 nn.Dropout(0.5) 的 Net
   (Linear(784,128) -> relu -> Dropout -> Linear(128,10))；
2) 在 MNIST 子集 (train 3000, val 500) 上训练 3 epoch；
3) 在 val 集上分别评估两次：
   - 不调 model.eval()（WRONG）
   - 调 model.eval() + torch.no_grad()（RIGHT）
   每个情况跑 3 次 val，打印 3 次准确率看波动；
4) 对比：WRONG 准确率波动大，RIGHT 准确率稳定。

示例:
    >>> python3 practice05.py
    [错] 验证 1: 76.40%
    [错] 验证 2: 81.20%
    [错] 验证 3: 73.80%
    [对] 验证 1: 84.60%
    [对] 验证 2: 84.60%
    [对] 验证 3: 84.60%
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
val_set = Subset(val_full, range(500))
train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
val_loader = DataLoader(val_set, batch_size=128, shuffle=False)


class Net(nn.Module):
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


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现 训练
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 训练 3 epoch
for epoch in range(3):
    model.train()
    for data, target in train_loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()


def evaluate(use_eval=False):
    """在 val 上评估准确率。"""
    if use_eval:
        model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in val_loader:
            out = model(data)
            pred = out.argmax(dim=1)
            correct += (pred == target).sum().item()
            total += target.size(0)
    return correct / total * 100


# 跑 3 次错/对的评估
wrong_accs = [evaluate(use_eval=False) for _ in range(3)]
right_accs = [evaluate(use_eval=True) for _ in range(3)]

print("[错] 忘记 model.eval():")
for i, acc in enumerate(wrong_accs, 1):
    print(f"  验证 {i}: {acc:.2f}%")
print("[对] 使用 model.eval() + no_grad:")
for i, acc in enumerate(right_accs, 1):
    print(f"  验证 {i}: {acc:.2f}%")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 准确率在合理范围
    for acc in wrong_accs + right_accs:
        assert 0 < acc < 100
    # 测试 2: RIGHT 的 3 次结果应非常接近
    right_tensor = torch.tensor(right_accs)
    assert right_tensor.std().item() < 1.0, (
        "正确做法 3 次准确率应稳定"
    )
    print("★ 红灯 2 验证通过：eval() 让验证结果稳定。")
