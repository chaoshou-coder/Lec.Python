"""
[难度: ⭐⭐]
[所属知识点: requires_grad 与 backward 自动微分]
[预计完成时间: 10 分钟]

自动微分是 PyTorch 的核心。请验证 dy/dx = 2x：对 y = x**2
求和再反向传播，梯度应为 2*x。

任务:
  1) 创建 x=torch.tensor([1.0, 2.0, 3.0], requires_grad=True)；
  2) 计算 y = x**2（逐元素平方）；
  3) 调 y.sum().backward()；
  4) 打印 x.grad 并验证它等于 2*x；
  5) 调 torch.allclose(x.grad, 2*x) 打印 True。

示例:
    >>> python3 practice03.py
    x.grad: tensor([2., 4., 6.])
    torch.allclose(x.grad, 2*x): True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch

# 1) 创建需要梯度的张量 x
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# 2) 逐元素平方
y = x ** 2

# 3) 对 y 求和后反向传播，计算梯度
y.sum().backward()

# 4) 打印 x 的梯度
print("x.grad:", x.grad)

# 5) 验证梯度等于 2*x
print("torch.allclose(x.grad, 2*x):", torch.allclose(x.grad, 2 * x))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 梯度存在且形状正确
    assert x.grad is not None
    assert x.grad.shape == torch.Size([3])

    # 测试 2: 梯度值等于 [2, 4, 6]
    expected_grad = torch.tensor([2., 4., 6.])
    assert torch.allclose(x.grad, expected_grad)
    print("所有测试通过!")
