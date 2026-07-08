"""
[难度: ⭐⭐⭐⭐]
[所属知识点: torch.autograd.gradcheck 自定义 Function]
[预计完成时间: 20 分钟]

题目描述: 要实现一个自定义的平方操作，并用 gradcheck 验证梯度。
    1) 定义 class SquareFn(torch.autograd.Function):
            @staticmethod forward(ctx, input):
                ctx.save_for_backward(input);
                return input ** 2
            @staticmethod backward(ctx, grad_output):
                input, = ctx.saved_tensors
                return 2 * input * grad_output
    2) 对 x = torch.randn(5, requires_grad=True, dtype=torch.double)
        调 torch.autograd.gradcheck(SquareFn.apply, (x,))
        打印返回值（应为 True）
    注意: gradcheck 要求输入为 double 精度 (torch.float64)。

示例:
    >>> x = torch.randn(5, requires_grad=True, dtype=torch.double)
    >>> torch.autograd.gradcheck(SquareFn.apply, (x,))
    True
"""

import torch

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class SquareFn(torch.autograd.Function):
    """自定义平方函数: f(x) = x^2, f'(x) = 2x"""

    @staticmethod
    def forward(ctx, input):
        # 学员请在此处实现: 保存输入, 返回平方
        ctx.save_for_backward(input)
        return input ** 2

    @staticmethod
    def backward(ctx, grad_output):
        # 学员请在此处实现: 返回 2 * input * grad_output
        (input,) = ctx.saved_tensors
        return 2 * input * grad_output


# 学员请在此处定义 double 精度的测试张量
x = torch.randn(5, requires_grad=True, dtype=torch.double)

# 学员请在此处调用 gradcheck
result = torch.autograd.gradcheck(SquareFn.apply, (x,))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: gradcheck 应返回 True
    print("测试 1: gradcheck 结果 =", result)
    assert result, "gradcheck 未通过, 反向传播可能有误！"

    # 测试 2: 换另一组 double 精度随机数再验证
    torch.manual_seed(123)
    x2 = torch.randn(5, requires_grad=True, dtype=torch.double)
    r2 = torch.autograd.gradcheck(SquareFn.apply, (x2,))
    print("测试 2: 新参数 gradcheck =", r2)
    assert r2, "换参数后 gradcheck 未通过！"

    # 测试 3: 验证前向输出正确 (x=2 时, x^2=4)
    x3 = torch.tensor([2.0], dtype=torch.double)
    y3 = SquareFn.apply(x3)
    print("测试 3: SquareFn(2.0) =", y3.item())
    assert y3.item() == 4.0, "前向计算错误！"

    # 测试 4: 多维张量 gradcheck
    torch.manual_seed(0)
    x4 = torch.randn(3, 4, requires_grad=True, dtype=torch.double)
    r4 = torch.autograd.gradcheck(SquareFn.apply, (x4,))
    print("测试 4: 多维张量 gradcheck =", r4)
    assert r4, "多维张量 gradcheck 未通过！"

    print("全部测试通过!")
