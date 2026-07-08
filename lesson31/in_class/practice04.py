"""
[难度: ⭐⭐]
[所属知识点: CIFAR-10 数据集加载]
[预计完成时间: 10 分钟]

题目描述:
加载 CIFAR-10 训练集,打印 dataset[0] 的 image shape、类别名称,
以及像素值范围。场景:你接手一个图像分类项目,第一件事
就是"看一眼数据长什么样",避免后续 pipeline 里尺寸或归一化出错。

数据集: torchvision.datasets.CIFAR10

类别名称:
    ['airplane','automobile','bird','cat','deer',
     'dog','frog','horse','ship','truck']

示例:
    >>> image shape: torch.Size([3, 32, 32])
    >>> 类别: cat (label=3)
    >>> 像素值范围: [0.0, 1.0]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
from torchvision import datasets, transforms

transform = transforms.ToTensor()
dataset = datasets.CIFAR10(root='./data', train=True,
                           download=True, transform=transform)

img, label = dataset[0]
classes = ['airplane','automobile','bird','cat','deer',
           'dog','frog','horse','ship','truck']

print("image shape:", img.shape)
print(f"类别: {classes[label]} (label={label})")
print(f"像素值范围: [{img.min():.2f}, {img.max():.2f}]")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: image shape = [3, 32, 32]
    assert img.shape == torch.Size([3, 32, 32]), \
        f"期望 [3,32,32],实际 {img.shape}"
    print("测试 1 通过")

    # 测试 2: 像素值在 [0, 1] 范围(ToTensor 自动除 255)
    assert img.min() >= 0.0 and img.max() <= 1.0, \
        f"像素应在 [0,1],实际 [{img.min():.2f},{img.max():.2f}]"
    print("测试 2 通过")
