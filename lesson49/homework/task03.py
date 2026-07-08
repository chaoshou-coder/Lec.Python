"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 异步爬取 + SQLite 存储一体化]
[预计完成时间: 20 分钟]

题目描述:
    用 aiohttp 并发爬取 books.toscrape.com 前 3 页,
    解析每本书的书名(title)和价格(price),
    把数据异步写入 SQLite books 表(使用
    loop.run_in_executor 将阻塞的 SQLite 写入序列化),
    最后 SELECT COUNT(*) 验证总数。(期望约 60 条)

    表结构: books(id INTEGER PRIMARY KEY,
                 title TEXT, price REAL)
    注意: SQLite 写入必须串行化(A 线程写时 B 线程等),
    否则会触发 "database is locked"。

示例:
    >>> 运行后终端输出:
    爬取 3 页完成
    成功写入数据库 60 条
    SELECT COUNT(*) = 60
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
    import asyncio

    # 测试 1: 验证建表语句
    print("--- 测试 1:建表 ---")
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE books("
        "id INTEGER PRIMARY KEY, "
        "title TEXT, price REAL)"
    )
    print("建表成功")
    conn.close()

    # 测试 2: 模拟异步 + run_in_executor 写入
    print("\n--- 测试 2:模拟异步写入 ---")

    async def fake_main():
        """模拟异步爬取并用 executor 写库"""
        conn = sqlite3.connect(
            ":memory:", check_same_thread=False
        )
        conn.execute(
            "CREATE TABLE books("
            "id INTEGER PRIMARY KEY, "
            "title TEXT, price REAL)"
        )
        loop = asyncio.get_running_loop()

        def do_insert(title, price):
            conn.execute(
                "INSERT INTO books(title, price) "
                "VALUES (?, ?)",
                (title, price)
            )
            conn.commit()

        # 模拟 5 本书的写入
        for i in range(5):
            await loop.run_in_executor(
                None, do_insert, f"book_{i}", 10.0 + i
            )

        cur = conn.execute("SELECT COUNT(*) FROM books")
        count = cur.fetchone()[0]
        conn.close()
        return count

    result = asyncio.run(fake_main())
    print(f"异步写入后总数: {result}")
    assert result == 5, f"期望 5,实际 {result}"
    print("测试 2 通过")
