"""
[难度: ⭐⭐]
[所属知识点: 偏好标注 / chosen-rejected]
[预计完成时间: 10 分钟]

给定 4 个回答字符串的列表，写 annotate_preferences(answers)
模拟标注员打分：以字符串长度作为简易质量 proxy
（越长越详尽），返回 {"chosen": 最长, "rejected": 最短}。

教学点：真实场景中标注员给 chosen/rejected，
DPO 正是用这种成对数据直接训练。

示例:
    >>> ans = ["短回答", "中等长度回答",
    ...        "这是一段非常详尽的长篇回答内容",
    ...        "还行"]
    >>> annotate_preferences(ans)
    {'chosen': '这是一段非常详尽的长篇回答内容',
     'rejected': '短回答'}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本 chosen/rejected
    # ans = ["短", "中等长度", "非常详细的长篇回答", "还行"]
    # r = annotate_preferences(ans)
    # assert r['chosen'] == "非常详细的长篇回答"
    # assert r['rejected'] == "短"
    # print("测试 1 通过:", r)

    # 测试 2: 边界 — 等长时取第一个最长
    # ans2 = ["a" * 5, "b" * 5, "c" * 3]
    # r2 = annotate_preferences(ans2)
    # assert len(r2['chosen']) >= len(r2['rejected'])
    # print("测试 2 通过:", r2)
    pass
