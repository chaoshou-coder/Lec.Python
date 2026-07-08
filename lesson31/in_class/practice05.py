"""
[难度: ⭐⭐⭐]
[所属知识点: ★红灯 2:backbone lr 与分类头 lr 差异化]
[预计完成时间: 15 分钟]

题目描述:
下面这段迁移学习代码把 backbone 和分类头的学习率设成相同,
这在实践中会导致预训练特征被破坏。请诊断问题,并修改优化器
为参数组形式:
    - backbone 参数: lr = 1e-4(小学习率)
    - 分类头 fc 参数: lr = 1e-3(大学习率)

场景:你的 mentor review 代码后说"backbone lr 应该远小于
分类头 lr,否则会破坏预训练特征",让你改。

正确优化器写法(参考):
    optimizer = torch.optim.Adam([
        {"params": backbone_params, "lr": 1e-4},
        {"params": head_params,     "lr": 1e-3},
    ])

示例:
    >>> backbone 参数 lr = 1e-04
    >>> 分类头参数 lr = 1e-03
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
import torchvision.models as models

model = models.resnet18(pretrained=False)
model.fc = nn.Linear(512, 10)

# 分离 backbone 与 head 参数
backbone_params = []
head_params = []
for name, param in model.named_parameters():
    if "fc" in name:
        head_params.append(param)
    else:
        backbone_params.append(param)

# 参数组差异化学习率
optimizer = torch.optim.Adam(
    [
        {"params": backbone_params, "lr": 1e-4},
        {"params": head_params, "lr": 1e-3},
    ]
)

for i, group in enumerate(optimizer.param_groups):
    print(f"参数组 {i}: lr={group['lr']}, "
          f"参数量={sum(p.numel() for p in group['params'])}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: backbone lr = 1e-4
    assert optimizer.param_groups[0]["lr"] == 1e-4, \
        "backbone lr 应为 1e-4"
    print("测试 1 通过")

    # 测试 2: head lr = 1e-3
    assert optimizer.param_groups[1]["lr"] == 1e-3, \
        "head lr 应为 1e-3"
    print("测试 2 通过")

    # 测试 3: backbone lr < head lr
    assert optimizer.param_groups[0]["lr"] < \
           optimizer.param_groups[1]["lr"], \
        "backbone lr 应小于 head lr"
    print("测试 3 通过")
