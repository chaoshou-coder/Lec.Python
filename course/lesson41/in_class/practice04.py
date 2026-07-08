"""
[难度: ⭐⭐⭐]
[所属知识点: Reward Model / nn.Module]
[预计完成时间: 15 分钟]

写 RewardModelDemo(nn.Module)：
- embed = nn.Embedding(vocab_size=1000, embed_dim=32)
- score = nn.Linear(32, 1)
- forward(input_ids) 返回 reward 张量

教学点：RM 给回答打分，PPO 用这个分数更新模型，
DPO 则绕过了显式 RM。

示例:
    >>> model = RewardModelDemo()
    >>> out = model(torch.randint(0, 1000, (4, 10)))
    >>> out.shape
    torch.Size([4, 1])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape
    # model = RewardModelDemo()
    # out = model(torch.randint(0, 1000, (4, 10)))
    # assert out.shape == (4, 1), f"shape 异常: {out.shape}"
    # print("测试 1 通过: shape =", out.shape)

    # 测试 2: 单样本推理
    # single = model(torch.randint(0, 1000, (1, 8)))
    # assert single.dim() == 2
    # print("测试 2 通过: reward =", single.item())
    pass
