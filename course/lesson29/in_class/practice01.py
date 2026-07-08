"""
[难度: ⭐]
[所属知识点: MNIST 数据加载（transform + DataLoader）]
[预计完成时间: 5 分钟]

搭建 MNIST 数据管道是训练的第一步。

任务：
1) 用 torchvision.datasets.MNIST 下载训练集
   transform=ToTensor(), root='./data'；
2) 用 DataLoader(dataset, batch_size=64, shuffle=True)；
3) 取第一个 batch，打印 images.shape 和 labels.shape
   （应为 [64,1,28,28] 和 [64]）；
4) 打印 labels 的 dtype。

示例:
    >>> python3 practice01.py
    batch images shape: torch.Size([64, 1, 28, 28])
    batch labels shape: torch.Size([64])
    labels dtype: torch.int64
"""

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请自有实现
transform = transforms.Compose([
    transforms.ToTensor(),
])
train_set = datasets.MNIST(
    root="./data", train=True,
    download=True, transform=transform
)
train_loader = DataLoader(
    train_set, batch_size=64, shuffle=True
)

# 取第一个 batch
images, labels = next(iter(train_loader))
print("batch images shape:", images.shape)
print("batch labels shape:", labels.shape)
print("labels dtype:", labels.dtype)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: images shape = (64, 1, 28, 28)
    assert images.shape == torch.Size([64, 1, 28, 28])
    # 测试 2: labels shape = (64,)
    assert labels.shape == torch.Size([64])
    # 测试 3: labels dtype 是 int64
    assert labels.dtype == torch.int64
    print("所有测试通过!")
