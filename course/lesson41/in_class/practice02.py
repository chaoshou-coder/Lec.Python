"""
[难度: ⭐⭐]
[所属知识点: RLHF vs DPO 概念对比]
[预计完成时间: 10 分钟]

写 compare_rlhf_dpo()，用 dict 对比两种方法：
- 需要 RM / 训练稳定性 / 参数量 / 实现难度
用 f-string 打印对齐表格。

教学注释：DPO 跳过了 RM 训练和 PPO 采样，
所以实现更简单、训练更稳定。

示例:
    >>> compare_rlhf_dpo()
    维度       | RLHF         | DPO
    ----------------------------------------
    需要 RM    | 是           | 否
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 表格包含 4 行
    # rows = compare_rlhf_dpo()
    # assert len(rows) == 4
    # print("测试 1 通过: 4 个对比维度")

    # 测试 2: DPO 不需要 RM
    # rm_row = [r for r in rows if "RM" in r][0]
    # assert "否" in rm_row
    # print("测试 2 通过: DPO 不需要 RM")
    pass
