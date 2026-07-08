"""
[难度: ⭐⭐]
[所属知识点: 多层 CNN 搭建]
[预计完成时间: 10 分钟]

题目描述:
实现一个 2 层 CNN 特征提取器,结构为 Conv→ReLU→Conv→ReLU,
在 MNIST 测试集上前向传播并打印输出 shape。
场景:这是 CNN 章节热身,你负责搭一个"裸"特征提取器
(没有池化、没有全连接),看它把图像映射成了什么形状。

网络结构: 1x28x28 → Conv(1→16, k=3) → ReLU
         → Conv(16→32, k=3) → ReLU

提示:
    第一层输出: 28 - 3 + 1 = 26
    第二层输出: 26 - 3 + 1 = 24
    所以最终 shape = [N, 32, 24, 24]

示例:
    >>> 输出 shape
    torch.Size([1000, 32, 24, 24])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
from torchvision import datasets, transforms

# 数据加载(仅取第一个 batch)
transform = transforms.ToTensor()
dataset = datasets.MNIST(root='./data', train=False,
                         download=True, transform=transform)
loader = torch.utils.data.DataLoader(dataset, batch_size=1000)
images, _ = next(iter(loader))

# 2 层 CNN
model = nn.Sequential(
    nn.Conv2d(1, 16, kernel_size=3),
    nn.ReLU(),
    nn.Conv2d(16, 32, kernel_size=3),
    nn.ReLU(),
)

out = model(images)
print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape 为 [1000, 32, 24, 24]
    assert out.shape == torch.Size([1000, 32, 24, 24]), \
        f"期望 [1000,32,24,24],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 输出值 ≥ 0 (ReLU 保证非负)
    assert (out >= 0).all(), "ReLU 后不应有负值"
    print("测试 2 通过")
