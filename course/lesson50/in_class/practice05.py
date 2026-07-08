"""
[难度: ⭐⭐⭐]
[所属知识点: 数据集质量评估]
[预计完成时间: 15 分钟]

题目描述:
    编写 evaluate(dataset) 函数,对数据集做质量评估:
      (1) 打印总条数
      (2) 统计情感分布(positive/neutral/negative
          各自数量和百分比)
         评分 >=4 → positive, <=2 → negative, 否则 neutral
      (3) 随机抽检 5 条,打印 [sentiment] 《title》
    当某类占比 >80% 时,打印"⚠️ 严重不平衡"。

示例:
    >>> evaluate(dataset)
    总条数: 100
    positive: 45 (45.0%)
    neutral: 30 (30.0%)
    negative: 25 (25.0%)
    抽检样本:
    1. [positive] 《A Light in the Attic》
    ...

    >>> 不平衡情况:
    ⚠️ 严重不平衡!positive 占 85%
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 均衡数据集
    print("--- 测试 1:均衡数据 ---")
    dataset1 = (
        [{"title": f"book_{i}", "rating": 5,
          "sentiment": "positive"} for i in range(40)]
        + [{"title": f"book_{i}", "rating": 3,
            "sentiment": "neutral"} for i in range(40, 70)]
        + [{"title": f"book_{i}", "rating": 1,
            "sentiment": "negative"} for i in range(70, 100)]
    )
    stats = {"positive": 0, "neutral": 0, "negative": 0}
    for d in dataset1:
        stats[d["sentiment"]] += 1
    total = len(dataset1)
    print(f"总条数: {total}")
    for k, v in stats.items():
        print(f"  {k}: {v} ({v/total*100:.1f}%)")
    assert total == 100
    assert stats["positive"] == 40
    print("测试 1 通过")

    # 测试 2: 不平衡数据集
    print("\n--- 测试 2:不平衡数据 ---")
    dataset2 = (
        [{"title": f"book_{i}", "sentiment": "positive"}
         for i in range(85)]
        + [{"title": f"book_{i}", "sentiment": "negative"}
           for i in range(85, 100)]
    )
    stats2 = {"positive": 0, "neutral": 0, "negative": 0}
    for d in dataset2:
        stats2[d["sentiment"]] += 1
    total2 = len(dataset2)
    max_ratio = max(stats2.values()) / total2
    print(f"总条数: {total2},最大类占比: {max_ratio:.0%}")
    if max_ratio > 0.8:
        print("⚠️ 严重不平衡!")
    assert max_ratio > 0.8
    print("测试 2 通过")
