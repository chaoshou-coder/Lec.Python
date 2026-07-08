"""
[难度: ⭐⭐⭐]
[所属知识点: 完整数据集构建]
[预计完成时间: 15 分钟]

题目描述:
    生成一个 100 条模拟书籍数据集(每条含 title, rating, price),
    其中故意混入:
      - 10 条重复数据(与已有条目 title 相同)
      - 5 条脏数据(title 为空字符串或价格为负数)
    依次调用 dedup → clean → split_dataset,
    输出最终训练集和测试集大小。

示例:
    >>> 运行后输出:
    原始数据: 100 条
    去重后: 90 条
    清洗后: 85 条
    训练集: 68 条
    测试集: 17 条
    训练集 + 测试集 = 85 条(无泄露)
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
    random.seed(42)

    # 测试 1: 模拟数据集各阶段计数
    print("--- 测试 1:各阶段计数 ---")
    raw = [{"title": f"book_{i}", "rating": random.randint(1, 5),
            "price": round(random.uniform(10, 60), 2)}
           for i in range(100)]
    # 混入 10 条重复
    for i in range(10):
        raw.append(raw[i].copy())
    # 混入 5 条脏
    for i in range(5):
        raw.append({"title": "", "rating": 3, "price": -1.0})
    print(f"原始数据: {len(raw)} 条")
    assert len(raw) == 115

    # 去重
    seen = set()
    after_dedup = []
    for b in raw:
        if b["title"] not in seen:
            seen.add(b["title"])
            after_dedup.append(b)
    print(f"去重后: {len(after_dedup)} 条")

    # 清洗
    after_clean = [b for b in after_dedup if b["title"]
                   and b["price"] > 0]
    print(f"清洗后: {len(after_clean)} 条")

    # 划分
    random.seed(42)
    shuffled = after_clean[:]
    random.shuffle(shuffled)
    split_idx = int(len(shuffled) * 0.8)
    train = shuffled[:split_idx]
    test = shuffled[split_idx:]
    print(f"训练集: {len(train)} 条,测试集: {len(test)} 条")
    assert len(train) + len(test) == len(after_clean)
    assert len(set(b["title"] for b in train)
               & set(b["title"] for b in test)) == 0
    print("测试 1 通过:无数据泄露")
