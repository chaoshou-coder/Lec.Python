"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: Day01-20 大综合]
[预计完成时间: 30 分钟]

题目描述:
实现一个控制台图书管理系统,支持以下功能:
1. 添加图书(title, author)
2. 删除图书(title)
3. 查询图书(title)
4. 借阅图书(title, borrower)
5. 归还图书(title)
6. 列出所有图书
7. 数据持久化到 JSON
8. 导出借阅记录到 CSV

要求:使用类封装,处理各种异常情况。

示例:
    >>> system = LibrarySystem("/tmp/lib.json")
    >>> system.add_book("Python入门", "张三")
    >>> system.borrow_book("Python入门", "小明")
    >>> system.export_borrow_records("/tmp/records.csv")
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import os

    data_path = "/tmp/test_lib_system.json"
    csv_path = "/tmp/test_borrow_records.csv"

    # 测试 1: 添加图书
    system = LibrarySystem(data_path)
    system.add_book("Python入门", "张三")
    system.add_book("算法导论", "李四")
    system.add_book("红楼梦", "曹雪芹")
    system.list_books()

    # 测试 2: 借阅图书
    system.borrow_book("Python入门", "小明")
    system.borrow_book("算法导论", "小红")
    system.list_books()

    # 测试 3: 查询图书
    print(system.find_book("Python入门"))

    # 测试 4: 归还图书
    system.return_book("Python入门")
    system.list_books()

    # 测试 5: 导出借阅记录
    system.export_borrow_records(csv_path)
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            print(f.read())

    # 测试 6: 删除图书
    system.remove_book("红楼梦")
    system.list_books()

    # 测试 7: 持久化
    system.save()
    system2 = LibrarySystem(data_path)
    system2.load()
    print(f"加载后图书数: {len(system2.books)}")

    # 清理
    for p in [data_path, csv_path]:
        if os.path.exists(p):
            os.remove(p)
