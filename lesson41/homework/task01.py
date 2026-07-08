"""
[难度: ⭐⭐]
[所属知识点: RLHF 训练成本估算]
[预计完成时间: 10 分钟]

写 estimate_rlhf_cost(steps, rm_size=7)，估算 RLHF
训练时间（秒）。简易公式：
- 每步耗时 = 0.5 * 7 + 0.2 * rm_size 秒
- 总时间 = steps * 每步耗时

教学点：RLHF 比 SFT 贵数倍，DPO 则省掉 RM，
所以成本是方案选型的重要依据。

示例:
    >>> cost = estimate_rlhf_cost(10000, rm_size=7)
    >>> print(f"约 {cost:.0f} 秒")
    约 55000 秒
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: steps=10000
    # cost = estimate_rlhf_cost(10000, 7)
    # assert cost > 0
    # print("测试 1 通过: 约", cost, "秒")

    # 测试 2: 更大 RM 更贵
    # cost_small = estimate_rlhf_cost(1000, 1)
    # cost_big = estimate_rlhf_cost(1000, 13)
    # assert cost_big > cost_small
    # print("测试 2 通过: 大 RM 更贵")
    pass
