"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整 CIFAR-10 迁移学习 pipeline]
[预计完成时间: 20 分钟]

题目描述:
实现完整 CIFAR-10 迁移学习 pipeline:
ResNet18 预训练 → 替换 fc → 解冻最后 2 层 → 训练 5 epoch,
打印 train/val acc。场景:这是迁移学习章节大作业,
把"部分微调"策略完整跑通。

步骤:
1. 加载 resnet18(pretrained=False,本题不下载权重)
2. 替换 model.fc = nn.Linear(512, 10)
3. 冻结全部参数,然后解冻 layer4 和 fc
4. 用 backbone lr=1e-4, head lr=1e-3 参数组训练
5. 训练 5 epoch,每个 epoch 打印 train/val acc

数据集: CIFAR-10, batch_size=64

示例:
    >>> Epoch 1, Train Acc: 35.12%, Val Acc: 32.45%
    >>> Epoch 5, Train Acc: 65.78%, Val Acc: 61.23%
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
val_set = datasets.CIFAR10(root='./data', train=False,
                           download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64,
                                           shuffle=True)
val_loader = torch.utils.data.DataLoader(val_set, batch_size=64,
                                         shuffle=False)

# 模型:解冻 layer4 + fc
model = tvm.resnet18(pretrained=False)
for param in model.parameters():
    param.requires_grad = False
for param in model.layer4.parameters():
    param.requires_grad = True
model.fc = nn.Linear(512, 10)

# 参数组:backbone(含 layer4) lr=1e-4, head lr=1e-3
optimizer = optim.Adam([
    {"params": (p for n, p in model.named_parameters()
                if p.requires_grad and "fc" not in n),
     "lr": 1e-4},
    {"params": model.fc.parameters(), "lr": 1e-3},
])
criterion = nn.CrossEntropyLoss()

# 训练 + 验证
for epoch in range(5):
    # 训练
    model.train()
    correct, total = 0, 0
    for data, target in train_loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        correct += (out.argmax(1) == target).sum().item()
        total += target.size(0)
    train_acc = 100.0 * correct / total

    # 验证
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for data, target in val_loader:
            out = model(data)
            correct += (out.argmax(1) == target).sum().item()
            total += target.size(0)
    val_acc = 100.0 * correct / total
    print(f"Epoch {epoch+1}, Train Acc: {train_acc:.2f}%, "
          f"Val Acc: {val_acc:.2f}%")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: layer4 和 fc 可训练,layer1-3 冻结
    layer1_frozen = all(not p.requires_grad
                       for p in model.layer1.parameters())
    layer4_trainable = all(p.requires_grad
                          for p in model.layer4.parameters())
    assert layer1_frozen and layer4_trainable, \
        "layer1 应冻结,layer4 应可训练"
    print("测试 1 通过")

    # 测试 2: 推理输出 shape 正确
    x = torch.randn(4, 3, 32, 32)
    model.eval()
    with torch.no_grad():
        out = model(x)
    assert out.shape == torch.Size([4, 10])
    print("测试 2 通过")
