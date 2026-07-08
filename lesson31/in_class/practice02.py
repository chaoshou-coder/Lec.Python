"""
[难度: ⭐⭐]
[所属知识点: 冻结 backbone 参数]
[预计完成时间: 10 分钟]

题目描述:
冻结 ResNet18 的 backbone 参数(仅保留 model.fc 可训练),
打印可训练与冻结参数数量。场景:你在做迁移学习,需要
"冻住预训练特征提取器,只训练最后的分类头"。

提示:
    遍历 model.parameters(),
    除 model.fc 之外的参数全部设 requires_grad=False。

示例:
    >>> 可训练参数: 5120
    >>> 冻结参数:   11176512
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torchvision.models as models
import torch.nn as nn

model = models.resnet18(pretrained=False)

# 冻结除 fc 外的所有参数
for name, param in model.named_parameters():
    if "fc" not in name:
        param.requires_grad = False

# 统计
trainable = sum(p.numel() for p in model.parameters()
                 if p.requires_grad)
frozen = sum(p.numel() for p in model.parameters()
             if not p.requires_grad)

print(f"可训练参数: {trainable}")
print(f"冻结参数:   {frozen}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 可训练参数 = fc.in_features*fc.out_features + bias
    #        = 512*1000 + 1000 = 513000
    assert trainable == 513000, \
        f"期望 513000,实际 {trainable}"
    print("测试 1 通过")

    # 测试 2: fc 层确实可训练
    for p in model.fc.parameters():
        assert p.requires_grad, "fc 层应可训练"
    print("测试 2 通过")
