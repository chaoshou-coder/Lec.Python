"""
[难度: ⭐⭐]
[所属知识点: nn.MaxPool2d]
[预计完成时间: 10 分钟]

题目描述:
用 nn.MaxPool2d 对一批特征图做 2×2 池化,验证输入输出尺寸。
场景:你在调试 CNN 的维度,需要确认 MaxPool2d(2) 确实
把空间分辨率减半,同时验证输出是局部最大值。

池化公式:
    H_out = floor(H_in / kernel_size)

示例:
    >>> 输入 [1, 8, 26, 26],池化后输出 shape torch.Size([1, 8, 13, 13])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn

# 模拟 8 张 26x26 特征图
x = torch.randn(1, 8, 26, 26)

pool = nn.MaxPool2d(kernel_size=2)
out = pool(x)

print("输入 shape:", x.shape)
print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 26x26 特征图池化后应为 13x13
    assert out.shape == torch.Size([1, 8, 13, 13]), \
        f"期望 [1,8,13,13],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 构造张量让 max 明确 —— 一个 2x2 区域 [1,9,4,3] 最大值是 9
    x_check = torch.tensor([[[[1., 9.], [4., 3.]]]])   # [1,1,2,2]
    out_check = pool(x_check)
    assert out_check.item() == 9.0, \
        f"期望 max=9,实际 {out_check.item()}"
    print("测试 2 通过")
