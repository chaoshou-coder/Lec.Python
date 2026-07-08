"""
[难度: ⭐⭐]
[所属知识点: 完整爬取单页并存储]
[预计完成时间: 10 分钟]

题目描述:
使用 requests + BeautifulSoup 爬取 books.toscrape.com
首页(第 1 页)所有书名,再用 sqlite3 存入 books 表,
最后查询并打印总条数。

要求:
  - 表结构: id INTEGER PRIMARY KEY, title TEXT
  - 建表语句使用 CREATE TABLE IF NOT EXISTS
  - 插入使用参数化查询防注入
  - 最后 SELECT COUNT(*) 打印总数

示例:
    >>> run()
    爬取完成,共 20 本书
    已存入 books 表
    查询总数: 20 条
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

    # 测试 1: 创建表并插入模拟数据
    print("--- 测试 1: 插入并统计 ---")
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books "
        "(id INTEGER PRIMARY KEY, title TEXT)"
    )
    fake_titles = [
        "A Light in the Attic",
        "Tipping the Velvet",
        "Soumission",
    ]
    for t in fake_titles:
        cur.execute("INSERT INTO books (title) VALUES (?)", (t,))
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM books")
    count = cur.fetchone()[0]
    print(f"已存入 books 表,共 {count} 条")
    assert count == 3

    # 测试 2: 再次插入,总数累加
    print("\n--- 测试 2: 累加插入 ---")
    more = ["Sharp Objects", "Sapiens"]
    for t in more:
        cur.execute("INSERT INTO books (title) VALUES (?)", (t,))
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM books")
    count = cur.fetchone()[0]
    print(f"再次存入后总数: {count} 条")
    assert count == 5
    conn.close()
