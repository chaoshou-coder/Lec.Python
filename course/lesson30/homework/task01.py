"""
[难度: ⭐⭐⭐⭐]
[所属知识点: nn.BatchNorm2d + train/eval 行为差异]
[预计完成时间: 20 分钟]

题目描述:
在 CNN 中加入 nn.BatchNorm2d,验证 train 与 eval 模式下 BN 层的行为差异。
场景:你发现 BN 层训练时更新 running_mean,推理时固定 running_mean,
导师让你"写一段代码证明这件事"。

要求:
1. 构造一个输入全为 5.0 的 tensor,过 BN 层,观察输出是否归一化
2. train 模式下多次前向传播,观察 running_mean 是否变化
3. eval 模式下输出直接用 running 统计量(不更新)

提示:
    BN(x) = γ * (x - μ) / √(σ²+ε) + β
    train 时 μ/σ² 来自当前 batch,并滑动更新 running_mean
    eval 时 μ/σ² 来自 running_mean

示例:
    >>> 初始 running_mean ≈ 0
    >>> 训练若干步后 running_mean 接近 5.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn

# BN 层:通道数 = 3
bn = nn.BatchNorm2d(num_features=3)

# 全 5.0 输入: batch=2, channel=3, 4×4
x = torch.ones(2, 3, 4, 4) * 5.0

print("初始 running_mean:", bn.running_mean)

# train 模式:做 10 次前向传播(模拟训练)
bn.train()
for i in range(10):
    out = bn(x)

print("10 步训练后 running_mean:", bn.running_mean)
print("最近一次输出均值(应接近 β=0):",
      out.mean().item())

# eval 模式:直接推理
bn.eval()
with torch.no_grad():
    out_eval = bn(x)

print("eval 模式输出均值:", out_eval.mean().item())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 训练后 running_mean 接近 5.0
    assert (bn.running_mean > 3.0).all(), \
        f"running_mean 应接近 5,实际 {bn.running_mean}"
    print("测试 1 通过")

    # 测试 2: eval 模式下 BN 不再更新 running_mean
    before_eval_mean = bn.running_mean.clone()
    bn.eval()
    _ = bn(x)
    after_eval_mean = bn.running_mean.clone()
    assert torch.equal(before_eval_mean, after_eval_mean), \
        "eval 模式不应更新 running_mean"
    print("测试 2 通过")
