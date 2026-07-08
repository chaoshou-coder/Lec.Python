"""
[难度: ⭐]
[所属知识点: torch.tensor 创建与属性]
[预计完成时间: 5 分钟]

你是一名 AI 工程师，刚接触 PyTorch。请创建一个张量并查看其
属性(dtype/shape/requires_grad)，这是理解张量的第一步。

任务:
  1) 用 torch.tensor 从列表 [1.0, 2.0, 3.0, 4.0] 创建张量 x；
  2) 打印 x.dtype, x.shape, x.requires_grad；
  3) 再创建 requires_grad=False 的整数张量 y=torch.tensor([5,6,7])，
     打印 y.dtype。

示例:
    >>> python3 practice01.py
    x.dtype: torch.float32
    x.shape: torch.Size([4])
    x.requires_grad: False
    y.dtype: torch.int64
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch

# 1) 用 torch.tensor 从列表创建浮点张量 x
x = torch.tensor([1.0, 2.0, 3.0, 4.0])

# 2) 打印 x 的三个属性
print("x.dtype:", x.dtype)
print("x.shape:", x.shape)
print("x.requires_grad:", x.requires_grad)

# 3) 创建整数张量 y，打印其 dtype
y = torch.tensor([5, 6, 7])
print("y.dtype:", y.dtype)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: x 是 float32，长度为 4 的一维张量
    assert x.dtype == torch.float32
    assert x.shape == torch.Size([4])
    assert x.requires_grad is False

    # 测试 2: y 是 int64，长度为 3
    assert y.dtype == torch.int64
    assert y.shape == torch.Size([3])
    print("所有测试通过!")
