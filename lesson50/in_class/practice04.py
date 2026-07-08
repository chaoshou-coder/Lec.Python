"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 数据清洗与格式化]
[预计完成时间: 20 分钟]

题目描述:
    编写 clean(books) 函数,对原始数据做三项清洗:
      (1) 去除 title 为空的条目
      (2) 价格从字符串 "£51.77" 转 float 51.77
      (3) 评分从英文单词转数字(如 "Three" → 3,
         映射: One=1, Two=2, Three=3, Four=4, Five=5)
    打印清洗前后数量。

示例:
    >>> raw = [
    ...     {"title": "A Light", "price": "£51.77",
    ...      "rating": "Three"},
    ...     {"title": "", "price": "£10.00",
    ...      "rating": "One"},
    ... ]
    >>> clean(raw)
    清洗前: 2 条
    清洗后: 1 条
    [{'title': 'A Light', 'price': 51.77, 'rating': 3}]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常清洗
    print("--- 测试 1:正常清洗 ---")
    raw_books = [
        {"title": "A Light", "price": "£51.77",
         "rating": "Three"},
        {"title": "Tipping", "price": "£53.74",
         "rating": "Four"},
        {"title": "", "price": "£10.00",
         "rating": "One"},
    ]
    RATING_MAP = {
        "One": 1, "Two": 2, "Three": 3,
        "Four": 4, "Five": 5,
    }
    cleaned = []
    for b in raw_books:
        if not b["title"]:
            continue
        cleaned.append({
            "title": b["title"],
            "price": float(b["price"].replace("£", "")),
            "rating": RATING_MAP.get(b["rating"], 0),
        })
    print(f"清洗前: {len(raw_books)} 条")
    print(f"清洗后: {len(cleaned)} 条")
    assert len(cleaned) == 2, f"期望 2,实际 {len(cleaned)}"
    assert cleaned[0]["price"] == 51.77
    assert cleaned[0]["rating"] == 3
    print("测试 1 通过")

    # 测试 2: 全部是脏数据
    print("\n--- 测试 2:全部是脏数据 ---")
    dirty_books = [
        {"title": "", "price": "£5.00", "rating": "One"},
        {"title": "", "price": "£8.00", "rating": "Two"},
    }
    cleaned2 = []
    for b in dirty_books:
        if not b["title"]:
            continue
        cleaned2.append(b)
    assert len(cleaned2) == 0
    print("全脏数据清洗后: 0 条,通过")
