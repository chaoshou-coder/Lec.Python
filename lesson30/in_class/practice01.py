"""
[难度: ⭐]
[所属知识点: nn.Conv2d]
[预计完成时间: 5 分钟]

题目描述:
用 nn.Conv2d 对一张随机灰度图像做卷积,打印输出张量的 shape。
场景:你刚入职 AI 组,导师让你"先搭一个最小 Conv2d 跑通",
熟悉 in_channels / out_channels / kernel_size 三个参数。

尺寸公式:
    H_out = (H_in + 2*padding - kernel_size) // stride + 1

示例:
    >>> out.shape
    torch.Size([1, 8, 26, 26])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn

# 一张灰度图: batch=1, channel=1, 高 28, 宽 28
x = torch.randn(1, 1, 28, 28)

# 1 通道输入,8 个卷积核,核大小 3×3
conv = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3)

out = conv(x)

print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认参数 28x28 输入,期望输出 [1, 8, 26, 26]
    assert out.shape == torch.Size([1, 8, 26, 26]), \
        f"期望 [1,8,26,26],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: 修改 kernel_size=5,期望输出 [1, 8, 24, 24]
    conv5 = nn.Conv2d(1, 8, kernel_size=5)
    out2 = conv5(x)
    assert out2.shape == torch.Size([1, 8, 24, 24]), \
        f"期望 [1,8,24,24],实际 {out2.shape}"
    print("测试 2 通过")
