"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 对齐方法选型 / 场景推荐]
[预计完成时间: 20 分钟]

写 AlignmentReport 类，给定 5 个应用场景，
每个场景推荐 RLHF 或 DPO 并给理由，最后打印报告表格。

场景示例：
1. 内容审核 (需要精细打分 → RLHF)
2. 客服话术 (数据量大简单偏好 → DPO)
3. 代码生成 (稳定性要求高 → DPO)
4. 医学回答 (高风险需 RM 把关 → RLHF)
5. 创意写作 (快速迭代 → DPO)

示例:
    >>> report = AlignmentReport()
    >>> report.generate()
    场景     | 推荐 | 理由
    --------------------------------
    内容审核 | RLHF | 需精细打分
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 生成 5 个场景
    # report = AlignmentReport()
    # table = report.generate()
    # assert len(table) == 5
    # print("测试 1 通过: 5 个场景")

    # 测试 2: 每个推荐都在候选中
    # for row in table:
    #     assert row['method'] in ('RLHF', 'DPO')
    #     assert len(row['reason']) > 0
    # print("测试 2 通过: 推荐全部合法")
    pass
