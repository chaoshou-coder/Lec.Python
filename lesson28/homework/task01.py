"""
[难度: ⭐⭐]
[所属知识点: 手动实现 2 层 MLP（nn.Module）]
[预计完成时间: 10 分钟]

题目描述: 从零搭一个 2 层 MLP 分类器，理解 nn.Module 的结构。
    定义 class TwoLayerMLP(nn.Module)：
        __init__(self, input_dim, hidden_dim, output_dim)：
            self.fc1 = nn.Linear(input_dim, hidden_dim)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(hidden_dim, output_dim)
        forward(self, x)：
            返回 self.fc2(self.relu(self.fc1(x)))
    测试: model = TwoLayerMLP(784, 128, 10)
          x = torch.randn(64, 784)
          打印 model(x).shape 应为 (64, 10)。

示例:
    >>> model = TwoLayerMLP(784, 128, 10)
    >>> x = torch.randn(64, 784)
    >>> print(model(x).shape)
    torch.Size([64, 10])
"""

import torch
import torch.nn as nn

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class TwoLayerMLP(nn.Module):
    """两层 MLP 分类器: input -> Linear -> ReLU -> Linear -> output"""

    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # 学员请在此处实现
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # 学员请在此处实现
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 标准输入 (batch=64, input_dim=784)
    model = TwoLayerMLP(784, 128, 10)
    x = torch.randn(64, 784)
    out = model(x)
    print("测试 1 输出形状:", out.shape)
    assert out.shape == torch.Size([64, 10]), \
        f"期望 (64, 10), 实际 {out.shape}"

    # 测试 2: 单样本输入 (batch=1, input_dim=784)
    x_single = torch.randn(1, 784)
    out_single = model(x_single)
    print("测试 2 输出形状:", out_single.shape)
    assert out_single.shape == torch.Size([1, 10]), \
        f"期望 (1, 10), 实际 {out_single.shape}"

    # 测试 3: 自定义维度 (input=20, hidden=10, output=5)
    model2 = TwoLayerMLP(20, 10, 5)
    x2 = torch.randn(3, 20)
    out2 = model2(x2)
    print("测试 3 输出形状:", out2.shape)
    assert out2.shape == torch.Size([3, 5]), \
        f"期望 (3, 5), 实际 {out2.shape}"

    print("全部测试通过!")
