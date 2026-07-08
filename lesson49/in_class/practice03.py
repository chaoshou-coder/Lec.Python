"""
[难度: ⭐⭐]
[所属知识点: SQLite 数据库存储]
[预计完成时间: 10 分钟]

题目描述:
使用 sqlite3 模块创建数据库 quotes.db,
创建表 quotes(字段: text, author),
插入至少 3 条名言数据,
然后查询并打印所有记录。

示例:
    >>> 运行后终端输出:
    (1, 'The world...', 'Albert Einstein')
    (2, 'It is...', 'J.K. Rowling')
    (3, 'The person...', 'Albert Einstein')
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查数据库文件存在且表结构正确
    import sqlite3, os
    if os.path.exists("quotes.db"):
        conn = sqlite3.connect("quotes.db")
        cursor = conn.execute(
            "SELECT sql FROM sqlite_master "
            "WHERE type='table' AND name='quotes'"
        )
        table_sql = cursor.fetchone()
        assert table_sql is not None, "quotes 表不存在"
        print(f"表创建语句: {table_sql[0]}")
        conn.close()
    else:
        print("quotes.db 数据库文件未生成")

    # 测试 2: 验证数据条数不少于 3 条
    if os.path.exists("quotes.db"):
        conn = sqlite3.connect("quotes.db")
        cursor = conn.execute("SELECT COUNT(*) FROM quotes")
        count = cursor.fetchone()[0]
        print(f"quotes 表共 {count} 条记录")
        assert count >= 3, f"记录数不足 3 条: {count}"

        # 打印所有记录
        cursor = conn.execute("SELECT * FROM quotes")
        for row in cursor.fetchall():
            print(row)
        conn.close()
