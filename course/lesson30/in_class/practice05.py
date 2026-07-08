"""
[难度: ⭐⭐⭐]
[所属知识点: Dropout + model.train()/eval()]
[预计完成时间: 15 分钟]

题目描述:
实现一个含 Dropout 的 CNN 分类网络,让学员体验 train() 与 eval()
模式下输出差异。场景:你在验收一个分类器,同事说"为什么推理时
和训练时输出不一样?"你需要用代码证明 Dropout 的行为差异。

网络结构:
    Conv(1→16, k=3) → ReLU → MaxPool(2)
    → Conv(16→32, k=3) → ReLU → MaxPool(2)
    → Flatten → FC(32*6*6 → 128) → Dropout(0.5) → FC(128→10)

提示:
    输入 28×28,经过 Conv(k=3)→pool(2)→Conv(k=3)→pool(2) 后
    第一次: (28-3+1)=26, /2=13
    第二次: (13-3+1)=11, /2=5 (向下取整)
    所以 flatten 后 = 32*5*5 = 800

示例:
    >>> train 模式和 eval 模式下两次输出是否相同(应不同)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn


class DropoutCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3),  # 28→26
            nn.ReLU(),
            nn.MaxPool2d(2),                  # 26→13
            nn.Conv2d(16, 32, kernel_size=3), # 13→11
            nn.ReLU(),
            nn.MaxPool2d(2),                  # 11→5
        )
        self.classifier = nn.Sequential(
            nn.Linear(32 * 5 * 5, 128),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(128, 10),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)


model = DropoutCNN()
x = torch.randn(2, 1, 28, 28)

# train 模式:Dropout 激活
model.train()
out_train1 = model(x)

# eval 模式:Dropout 关闭
model.eval()
with torch.no_grad():
    out_eval = model(x)

print("train 模式输出 shape:", out_train1.shape)
print("eval 模式输出 shape:", out_eval.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape 正确
    assert out_train1.shape == torch.Size([2, 10])
    assert out_eval.shape == torch.Size([2, 10])
    print("测试 1 通过")

    # 测试 2: train 与 eval 模式下输出不同(Dropout 随机)
    model.train()
    out_a = model(x)
    out_b = model(x)
    # 两次 train 推理由于 Dropout 随机性,通常不相同
    assert not torch.allclose(out_a, out_b, atol=1e-5), \
        "两次 train 推理应该不同(Dropout)"
    print("测试 2 通过")
