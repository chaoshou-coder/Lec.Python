"""
[难度: ⭐⭐⭐]
[所属知识点: nn.Module 实现简单线性层]
[预计完成时间: 15 分钟]

要实现 y = xW + b 的线性层（类似 nn.Linear），并掌握
nn.Parameter 与初始化方法。

任务:
  定义类 LinearLayer(nn.Module)，
  __init__(self, in_features, out_features):
      用 nn.Parameter 定义 weight(out×in) 和 bias(out)，
      用 nn.init.kaiming_normal_ 初始化 weight，
      nn.init.zeros_ 初始化 bias。
  forward(self, x): 返回 x @ weight.T + bias。
  测试: layer=LinearLayer(3,2); x=torch.randn(4,3);
  打印输出 shape 应为 (4,2)。

示例:
    >>> python3 practice04.py
    输出形状: torch.Size([4, 2])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch
import torch.nn as nn


class LinearLayer(nn.Module):
    """手写线性层: y = x @ W^T + b"""

    def __init__(self, in_features, out_features):
        super().__init__()
        # 定义可学习参数 weight 和 bias
        self.weight = nn.Parameter(
            torch.empty(out_features, in_features)
        )
        self.bias = nn.Parameter(
            torch.empty(out_features)
        )
        # 初始化
        nn.init.kaiming_normal_(self.weight)
        nn.init.zeros_(self.bias)

    def forward(self, x):
        return x @ self.weight.T + self.bias


# 测试: 4 个样本, 输入维度 3, 输出维度 2
layer = LinearLayer(3, 2)
x = torch.randn(4, 3)
out = layer(x)
print("输出形状:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出形状为 (4, 2)
    assert out.shape == torch.Size([4, 2])

    # 测试 2: weight 和 bias 是可学习参数
    params = list(layer.parameters())
    assert len(params) == 2
    # weight 形状 (out, in)
    assert params[0].shape == torch.Size([2, 3])
    # bias 形状 (out,)
    assert params[1].shape == torch.Size([2])

    # 测试 3: bias 全零
    assert torch.all(layer.bias == 0)
    print("所有测试通过!")
