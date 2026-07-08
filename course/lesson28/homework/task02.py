"""
[难度: ⭐⭐⭐]
[所属知识点: 矩阵乘法与广播综合 + 梯度验证]
[预计完成时间: 15 分钟]

题目描述: 理解矩阵乘法和广播后，用 autograd 验证一个复合函数的梯度。
    1) x = torch.randn(3, requires_grad=True)
    2) W = torch.randn(2, 3)（不需求梯度）
    3) 计算 y = (x @ W.T).sum()
    4) 调 y.backward()
    5) 打印 x.grad，应等于 W 按行求和 (W.sum(dim=0))
    6) 用 torch.allclose(x.grad, W.sum(dim=0)) 验证

示例:
    >>> x.grad = tensor([...])  # 应等于 W.sum(dim=0)
    >>> torch.allclose(x.grad, W.sum(dim=0))
    True
"""

import torch

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 设置随机种子，保证可复现
torch.manual_seed(42)

# 学员请在此处实现: 定义张量 x, W
x = torch.randn(3, requires_grad=True)
W = torch.randn(2, 3)

# 学员请在此处实现: 计算 y = (x @ W.T).sum()
y = (x @ W.T).sum()

# 学员请在此处实现: 反向传播
y.backward()

# 学员请在此处实现: 用 allclose 验证
is_correct = torch.allclose(x.grad, W.sum(dim=0))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 打印梯度与理论值
    print("测试 1: x.grad =", x.grad)
    print("测试 1: W.sum(dim=0) =", W.sum(dim=0))

    # 测试 2: allclose 验证
    print("测试 2: allclose 验证结果 =", is_correct)
    assert is_correct, "梯度验证不通过！"

    # 测试 3: 换一组随机种子再验证
    torch.manual_seed(0)
    x3 = torch.randn(3, requires_grad=True)
    W3 = torch.randn(2, 3)
    y3 = (x3 @ W3.T).sum()
    y3.backward()
    ok3 = torch.allclose(x3.grad, W3.sum(dim=0))
    print("测试 3: 新参数 allclose =", ok3)
    assert ok3, "换参数后梯度验证不通过！"

    # 测试 4: 非标准维度 (x(4), W(3, 4))
    torch.manual_seed(7)
    x4 = torch.randn(4, requires_grad=True)
    W4 = torch.randn(3, 4)
    y4 = (x4 @ W4.T).sum()
    y4.backward()
    ok4 = torch.allclose(x4.grad, W4.sum(dim=0))
    print("测试 4: 非标准维度 allclose =", ok4)
    assert ok4, "非标准维度梯度验证不通过！"

    print("全部测试通过!")
