"""
[难度: ⭐⭐⭐]
[所属知识点: 选择性参数冻结]
[预计完成时间: 15 分钟]

题目描述:
对 nn.Sequential(
    nn.Linear(32, 64),   # 命名 fc1
    nn.ReLU(),
    nn.Linear(64, 32),   # 命名 fc2
) 构建的模型,使用 LoRA 只对 "fc1" 层的 Linear
权重做微调 (target_modules=["fc1"], r=4)。
完成后遍历 model.named_parameters(),打印每个参数名和
requires_grad 状态,观察哪些被冻结、哪些可训练。

提示: 要给 Sequential 中的层分别命名,
最简单的方式是用 nn.Module 显式构建。

示例:
    >>> show_freeze_status()
    fc1.base_model.model.linear.weight: True
    fc1.base_model.model.linear.bias: False
    fc2.weight: False
    fc2.bias: False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch.nn as nn
from peft import LoraConfig, get_peft_model


class TwoLayerModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(32, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))


def show_freeze_status():
    """对 fc1 层应用 LoRA 后打印所有参数的冻结状态。"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    show_freeze_status()
    # 预期: fc1 相关 A/B 矩阵 requires_grad=True,
    #       fc2 的 weight/bias requires_grad=False
    print("测试通过 ✓")
