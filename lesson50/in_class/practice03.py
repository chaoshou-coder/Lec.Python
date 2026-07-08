"""
[难度: ⭐⭐⭐]
[所属知识点: 数据去重]
[预计完成时间: 15 分钟]

题目描述:
    编写 dedup(books) 函数,输入一个包含书籍字典的列表,
    按 title 字段去重(保留第一次出现的条目)。
    打印去重前后的数量。
    关键约束:**不能遍历时删除原列表元素**,
    应新建一个列表存储结果。

示例:
    >>> books = [
    ...     {"title": "A Light in the Attic"},
    ...     {"title": "Tipping the Velvet"},
    ...     {"title": "A Light in the Attic"},
    ... ]
    >>> dedup(books)
    去重前: 3 条
    去重后: 2 条
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有重复的情况
    print("--- 测试 1:含重复数据 ---")
    books1 = [
        {"title": "A Light in the Attic", "price": 51.77},
        {"title": "Tipping the Velvet", "price": 53.74},
        {"title": "A Light in the Attic", "price": 51.77},
        {"title": "Soumission", "price": 50.10},
    ]
    seen = set()
    result1 = []
    for b in books1:
        if b["title"] not in seen:
            seen.add(b["title"])
            result1.append(b)
    print(f"去重前: {len(books1)} 条")
    print(f"去重后: {len(result1)} 条")
    assert len(result1) == 3, f"期望 3,实际 {len(result1)}"
    print("测试 1 通过")

    # 测试 2: 无重复 + 空列表
    print("\n--- 测试 2:无重复 + 空列表 ---")
    books2 = [
        {"title": "Book A", "price": 10.0},
        {"title": "Book B", "price": 20.0},
    ]
    seen2 = set()
    result2 = []
    for b in books2:
        if b["title"] not in seen2:
            seen2.add(b["title"])
            result2.append(b)
    assert len(result2) == 2
    print("无重复列表去重后: 2 条,通过")

    books3 = []
    seen3 = set()
    result3 = []
    for b in books3:
        if b["title"] not in seen3:
            seen3.add(b["title"])
            result3.append(b)
    assert len(result3) == 0
    print("空列表去重后: 0 条,通过")
