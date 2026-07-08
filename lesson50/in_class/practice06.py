"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整流水线(采集→清洗→评估)]
[预计完成时间: 20 分钟]

题目描述:
    把前面 3 题的功能串成完整流水线:
    1. 生成 20 条模拟原始数据(含 3 条重复 + 2 条脏数据)
    2. dedup 去重 → 打印数量
    3. clean 清洗 → 打印数量
    4. evaluate 评估 → 打印分布
    固定 random.seed(42) 保证可复现。

示例:
    >>> run_pipeline()
    原始数据: 20 条
    去重后: 17 条
    清洗后: 15 条
    总条数: 15
      positive: 6 (40.0%)
      neutral: 5 (33.3%)
      negative: 4 (26.7%)
    流水线完成
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import random

    # 测试 1: 验证随机种子可复现
    print("--- 测试 1:可复现性 ---")
    random.seed(42)
    data1 = [random.randint(1, 100) for _ in range(5)]
    random.seed(42)
    data2 = [random.randint(1, 100) for _ in range(5)]
    assert data1 == data2, "相同种子应产生相同序列"
    print(f"种子 42 产生的序列: {data1}")
    print("可复现性通过")

    # 测试 2: 模拟流水线计数
    print("\n--- 测试 2:流水线计数 ---")
    random.seed(42)
    raw = [{"title": f"book_{i}", "rating": random.randint(1, 5)}
           for i in range(20)]
    # 模拟去重(假设 3 条重复)
    after_dedup = raw[:17]
    # 模拟清洗(假设 2 条脏)
    after_clean = after_dedup[:15]
    print(f"原始数据: {len(raw)} 条")
    print(f"去重后: {len(after_dedup)} 条")
    print(f"清洗后: {len(after_clean)} 条")
    assert len(raw) == 20
    assert len(after_dedup) == 17
    assert len(after_clean) == 15
    print("流水线计数通过")
