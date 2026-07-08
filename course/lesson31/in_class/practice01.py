"""
[难度: ⭐]
[所属知识点: torchvision.models.resnet18]
[预计完成时间: 5 分钟]

题目描述:
用 torchvision.models.resnet18 构建模型,打印 model.fc 的
in_features 和 out_features。场景:你准备做迁移学习,
第一步是"摸清预训练模型的最后一层长什么样",以便后续替换。

注意:本题设 pretrained=False,不下载权重,仅看结构。

示例:
    >>> fc.in_features  = 512
    >>> fc.out_features = 1000
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torchvision.models as models
import torch.nn as nn

# 构建 ResNet18(不加载预训练权重)
model = models.resnet18(pretrained=False)

fc = model.fc
print("fc 层:", fc)
print("fc.in_features: ", fc.in_features)
print("fc.out_features:", fc.out_features)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: ResNet18 的 fc.in_features 应为 512
    assert fc.in_features == 512, \
        f"期望 in_features=512,实际 {fc.in_features}"
    print("测试 1 通过")

    # 测试 2: 默认 fc.out_features = 1000(ImageNet)
    assert fc.out_features == 1000, \
        f"期望 out_features=1000,实际 {fc.out_features}"
    print("测试 2 通过")
