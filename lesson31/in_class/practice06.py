"""
[难度: ⭐⭐⭐]
[所属知识点: 迁移学习训练循环]
[预计完成时间: 15 分钟]

题目描述:
实现迁移学习训练循环:冻结 backbone、只训练 fc 分类头,
在 CIFAR-10 上训练 2 个 epoch,每个 epoch 后打印 train acc。
场景:你接到一个小分类任务,数据量少,直接冻住 ResNet18 的
特征提取器是稳妥做法。

要求:
1. 冻结 backbone,替换 fc 为 10 分类
2. 交叉熵损失 + Adam(lr=1e-3) 训练 fc
3. 训练 2 epoch,每个 epoch 打印训练准确率

数据集: CIFAR-10, batch_size=64

示例:
    >>> Epoch 1, Train Acc: 45.23%
    >>> Epoch 2, Train Acc: 58.67%
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as tvm
from torchvision import datasets, transforms

# 数据
transform = transforms.ToTensor()
train_set = datasets.CIFAR10(root='./data', train=True,
                             download=True, transform=transform)
loader = torch.utils.data.DataLoader(train_set, batch_size=64,
                                     shuffle=True)

# 模型:冻 backbone,换 fc
model = tvm.resnet18(pretrained=False)
for param in model.parameters():
    param.requires_grad = False
model.fc = nn.Linear(512, 10)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=1e-3)

# 训练
model.train()
for epoch in range(2):
    correct = 0
    total = 0
    for data, target in loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        pred = out.argmax(dim=1)
        correct += (pred == target).sum().item()
        total += target.size(0)
    acc = 100.0 * correct / total
    print(f"Epoch {epoch+1}, Train Acc: {acc:.2f}%")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 模型推理 shape
    x = torch.randn(4, 3, 32, 32)
    model.eval()
    with torch.no_grad():
        out = model(x)
    assert out.shape == torch.Size([4, 10])
    print("测试 1 通过")

    # 测试 2: 仅 fc 层可训练
    trainable = [n for n, p in model.named_parameters()
                 if p.requires_grad]
    assert all("fc" in n for n in trainable), \
        "应只有 fc 层可训练"
    print("测试 2 通过")
