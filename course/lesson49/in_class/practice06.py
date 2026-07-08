"""
[难度: ⭐⭐⭐⭐]
[所属知识点: SQLite 多线程写入加锁]
[预计完成时间: 20 分钟]

题目描述:
    用 ThreadPoolExecutor 并发向 SQLite 数据库写入数据,
    故意不加锁复现 "database is locked" 错误(或写入冲突),
    再用 threading.Lock 修复。记录成功写入的条数。

    要求:
      - 创建 books.db,表 books(id INTEGER PRIMARY KEY, title)
      - 用 4 个线程各写 5 条数据
      - 修复后成功写入 20 条
      - 最后 SELECT COUNT(*) 验证

示例:
    >>> 运行后终端输出:
    --- 不加锁测试 ---
    出现错误:database is locked / 写入冲突
    --- 加锁修复后 ---
    成功写入 20 条
    数据库中总数: 20
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import sqlite3
    import os

    # 测试 1: 验证建表 + 单线程写入正常
    print("--- 测试 1:单线程写入 ---")
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE books("
        "id INTEGER PRIMARY KEY, title TEXT)"
    )
    for i in range(5):
        conn.execute(
            "INSERT INTO books(title) VALUES (?)",
            (f"book_{i}",)
        )
    conn.commit()
    count = conn.execute(
        "SELECT COUNT(*) FROM books"
    ).fetchone()[0]
    print(f"单线程写入 {count} 条")
    assert count == 5
    conn.close()
    print("测试 1 通过")

    # 测试 2: 验证加锁写法能正确工作
    print("\n--- 测试 2:加锁写入 ---")
    conn2 = sqlite3.connect(
        ":memory:", check_same_thread=False
    )
    conn2.execute(
        "CREATE TABLE books("
        "id INTEGER PRIMARY KEY, title TEXT)"
    )
    import threading
    write_lock = threading.Lock()

    def safe_insert(n):
        with write_lock:
            conn2.execute(
                "INSERT INTO books(title) VALUES (?)",
                (f"book_{n}",)
            )
            conn2.commit()

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as pool:
        pool.map(safe_insert, range(20))

    count2 = conn2.execute(
        "SELECT COUNT(*) FROM books"
    ).fetchone()[0]
    print(f"加锁写入后总数: {count2}")
    assert count2 == 20, f"期望 20,实际 {count2}"
    conn2.close()
    print("测试 2 通过")
