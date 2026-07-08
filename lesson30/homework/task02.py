"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整 MNIST CNN 分类器]
[预计完成时间: 20 分钟]

题目描述:
实现一个完整的 MNIST CNN 分类器,网络包含 Conv2d + BN + ReLU +
MaxPool + Dropout + FC,训练 2 个 epoch 并打印 loss。
场景:这是 CNN 章节结课作业,把"卷积 + 归一化 + 正则化"
三大机制全部串起来,跑通一个能真正的训练流程。

网络结构:
    Conv(1→16, k=3) → BN(16) → ReLU → MaxPool(2)
    → Conv(16→32, k=3) → BN(32) → ReLU → MaxPool(2)
    → Flatten → FC(32*5*5→128) → Dropout(0.5) → FC(128→10)

数据集: MNIST (torchvision.datasets.MNIST)
优化器: Adam, lr=1e-3
Loss: CrossEntropyLoss

示例:
    >>> Epoch 1, Batch 100, Loss: 0.3125
    >>> Epoch 2, Batch 100, Loss: 0.1023
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 数据
transform = transforms.ToTensor()
train_set = datasets.MNIST(root='./data', train=True,
                           download=True, transform=transform)
loader = torch.utils.data.DataLoader(train_set, batch_size=64,
                                     shuffle=True)

# 模型
class MNISTCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3),    # 28→26
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2),        # 26→13
            nn.Conv2d(16, 32, 3),   # 13→11
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),        # 11→5
        )
        self.classifier = nn.Sequential(
            nn.Linear(32 * 5 * 5, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)


model = MNISTCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 训练 2 epoch
model.train()
for epoch in range(2):
    total_loss = 0.0
    for batch_idx,(data, target) in enumerate(loader):
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        if batch_idx % 200 == 0:
            print(f"Epoch {epoch+1}, Batch {batch_idx}, "
                  f"Loss: {loss.item():.4f}")
    avg_loss = total_loss / len(loader)
    print(f"== Epoch {epoch+1} 平均 Loss: {avg_loss:.4f} ==")

# ======================
# 测试区(教师可复制到终端验证)
# ==========================
if __name__ == '__main__':
    # 测试 1: 模型可推理,输出 shape 正确
    x = torch.randn(4, 1, 28, 28)
    model.eval()
    with torch.no_grad():
        out = model(x)
    assert out.shape == torch.Size([4, 10]), \
        f"期望 [4,10],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 模型参数量 > 0
    total_params = sum(p.numel() for p in model.parameters())
    assert total_params > 0
    print(f"测试 2 通过,总参数量: {total_params}")
