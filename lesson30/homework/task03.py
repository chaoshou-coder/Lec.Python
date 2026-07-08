"""
[难度: ⭐⭐]
[所属知识点: nn.Conv2d 综合 + 尺寸公式手算]
[预计完成时间: 10 分钟]

题目描述:
任务:用 nn.Sequential 搭建一个 3 层 CNN 并在 MNIST 上验证输出 shape,
巩固"卷积+池化"尺寸计算公式。场景:你正在阅读一个 CNN 论文,
需要手动核对每一层的尺寸是否匹配。

网络结构:
    Conv(1→8, k=3, p=1) → ReLU → MaxPool(2)
    → Conv(8→16, k=3) → ReLU → MaxPool(2)
    → Conv(16→32, k=3) → ReLU

尺寸推导(请手算验证):
    输入 28×28
    Conv(3,p=1): (28+2-3)/1+1 = 28
    MaxPool(2):  28/2 = 14
    Conv(3,p=0): (14-3)/1+1 = 12
    MaxPool(2):  12/2 = 6
    Conv(3,p=0): (6-3)/1+1 = 4
    最终 shape = [N, 32, 4, 4]

数据集: MNIST 测试集,取 batch=64

示例:
    >>> 输出 shape: torch.Size([64, 32, 4, 4])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
from torchvision import datasets, transforms

transform = transforms.ToTensor()
dataset = datasets.MNIST(root='./data', train=False,
                         download=True, transform=transform)
loader = torch.utils.data.DataLoader(dataset, batch_size=64)
images, _ = next(iter(loader))

model = nn.Sequential(
    nn.Conv2d(1, 8, kernel_size=3, padding=1),  # 28→28
    nn.ReLU(),
    nn.MaxPool2d(2),                             # 28→14
    nn.Conv2d(8, 16, kernel_size=3),             # 14→12
    nn.ReLU(),
    nn.MaxPool2d(2),                             # 12→6
    nn.Conv2d(16, 32, kernel_size=3),            # 6→4
    nn.ReLU(),
)

out = model(images)
print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape = [64, 32, 4, 4]
    assert out.shape == torch.Size([64, 32, 4, 4]), \
        f"期望 [64,32,4,4],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 输出值非负(ReLU 保证)
    assert (out >= 0).all(), "ReLU 后不应有负值"
    print("测试 2 通过")
