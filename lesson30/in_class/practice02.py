"""
[难度: ⭐⭐]
[所属知识点: CNN flatten 尺寸计算(★红灯:尺寸写错)]
[预计完成时间: 10 分钟]

题目描述:
下面这段代码想搭一个 2 层 CNN 做 MNIST 分类,但运行时崩溃。
错误原因:flatten 时全连接层 in_features 写错了数字。
任务:
1. 用公式 H_out = (H_in + 2p - k) // s + 1 手算最终 feature map 尺寸
2. 把正确的 in_features 填入 nn.Linear,让代码跑通

网络结构: 1x28x28 → Conv(1→16, k=5) → MaxPool(2)
         → Conv(16→32, k=5) → MaxPool(2) → Linear → 10 类

示例:
    >>> 正确运行后输出 shape
    torch.Size([1, 10])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn


class BuggyCNN(nn.Module):
    """flatten 尺寸写错的 CNN,请修复 in_features"""

    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5),    # 28→24
            nn.ReLU(),
            nn.MaxPool2d(2),                    # 24→12
            nn.Conv2d(16, 32, kernel_size=5),   # 12→8
            nn.ReLU(),
            nn.MaxPool2d(2),                    # 8→4
        )
        # 学员填写正确 in_features = 32 * 4 * 4 = 512
        self.classifier = nn.Linear(512, 10)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)


# 模型推理
model = BuggyCNN()
x = torch.randn(1, 1, 28, 28)
out = model(x)
print("输出 shape:", out.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 单张图片前向传播
    assert out.shape == torch.Size([1, 10]), \
        f"期望 [1,10],实际 {out.shape}"
    print("测试 1 通过")

    # 测试 2: batch=4 前向传播
    x_batch = torch.randn(4, 1, 28, 28)
    out_batch = model(x_batch)
    assert out_batch.shape == torch.Size([4, 10]), \
        f"期望 [4,10],实际 {out_batch.shape}"
    print("测试 2 通过")
