"""
[难度: ⭐⭐]
[所属知识点: 替换 model.fc 层]
[预计完成时间: 10 分钟]

题目描述:
把 ResNet18 的 model.fc 替换为 nn.Linear(512, 10),
在 CIFAR-10 上做一次前向传播验证输出 shape。
场景:你的任务是把 ImageNet 预训练模型"嫁接"到 CIFAR-10
10 分类任务,第一步就是换掉 fc 层。

注意:CIFAR-10 图像是 3×32×32,直接给 ResNet18 也可推理
(会缩放到 7×7),本题仅验证 shape,不要求训练效果。

示例:
    >>> 输入 [4, 3, 32, 32]
    >>> 输出 shape torch.Size([4, 10])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torchvision.models as models
import torch.nn as nn

model = models.resnet18(pretrained=False)

# 替换 fc 层:512 → 10
model.fc = nn.Linear(512, 10)

# 模拟 CIFAR-10 一批图像(3 通道,32×32)
x = torch.randn(4, 3, 32, 32)

model.eval()
with torch.no_grad():
    out = model(x)

print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape [4, 10]
    assert out.shape == torch.Size([4, 10]), \
        f"期望 [4,10],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 输出不是全零(参数随机初始化,应随)
    assert not torch.allclose(out, torch.zeros_like(out))
    print("测试 2 通过")
