"""
[难度: ⭐⭐⭐]
[所属知识点: 迁移学习综合 - 解冻策略 + 参数组]
[预计完成时间: 15 分钟]

题目描述:
实现 choose_params 函数,根据"解冻层数"动态返回 backbone 与 head
参数组,配合 optimizer 差异化学习率使用。场景:你的 mentor
要求你"写一个函数,给定解冻层数 k,自动选出对应的参数组",
便于做消融实验。

函数签名:
    choose_params(model, unfreeze_layers):
        - model: 已替换 fc 的 ResNet18
        - unfreeze_layers: list,如 ["layer4","fc"]
        返回: (backbone_params, head_params)

要求:
    - 解冻层中除 fc 外的参数归入 backbone_params
    - fc 参数归入 head_params
    - 未解冻层(如 layer1-3)不参与分组

示例:
    >>> backbone, head = choose_params(model, ["layer4","fc"])
    >>> len(backbone) > 0, len(head) > 0
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
import torchvision.models as models


def choose_params(model, unfreeze_layers):
    backbone_params = []
    head_params = []
    for name, param in model.named_parameters():
        if "fc" in name:
            head_params.append(param)
        elif any(layer in name for layer in unfreeze_layers):
            backbone_params.append(param)
    return backbone_params, head_params


# 使用示例
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(512, 10)

# 冻结全部
for param in model.parameters():
    param.requires_grad = False
# 解冻 layer4 和 fc
for name, param in model.named_parameters():
    if "layer4" in name or "fc" in name:
        param.requires_grad = True

backbone, head = choose_params(model, ["layer4", "fc"])
print(f"backbone 参数数量: {sum(p.numel() for p in backbone)}")
print(f"head 参数数量: {sum(p.numel() for p in head)}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: backbone 含 layer4 参数
    backbone_numel = sum(p.numel() for p in backbone)
    assert backbone_numel > 0, "backbone 应含 layer4 参数"
    print("测试 1 通过")

    # 测试 2: head = fc 参数 = 512*10 + 10 = 5130
    head_numel = sum(p.numel() for p in head)
    assert head_numel == 5130, \
        f"head 期望 5130,实际 {head_numel}"
    print("测试 2 通过")

    # 测试 3: 未解冻层参数不在任一组中
    all_params = set(id(p) for p in backbone + head)
    for name, p in model.named_parameters():
        if "layer1" in name:
            assert id(p) not in all_params, \
                "layer1 已冻结,不应在任一组"
    print("测试 3 通过")
