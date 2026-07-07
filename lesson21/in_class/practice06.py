"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: Day01-20 大综合 + 统计]
[预计完成时间: 30 分钟]

题目描述:
在题 5 基础上,加入统计功能:
1. 借阅排行榜(按借阅次数降序)
2. 热门图书 Top N
3. 导出统计报告到 CSV(包含图书名、借阅次数、当前状态)

示例:
    >>> system = LibrarySystemV3("/tmp/lib_v3.json")
    >>> # ... 添加图书、借阅等操作后
    >>> system.borrow_ranking()
    [{'title': 'Python入门', 'count': 5}, ...]
    >>> system.export_report("/tmp/report.csv")
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

    data_path = "/tmp/test_lib_v3.json"
    report_path = "/tmp/test_report.csv"

    system = LibrarySystemV3(data_path)

    # 准备数据
    system.register("小明", "123")
    system.register("小红", "456")
    system.add_book("Python入门", "张三")
    system.add_book("算法导论", "李四")
    system.add_book("红楼梦", "曹雪芹")

    # 模拟多次借阅
    system.login("小明", "123")
    system.borrow_book("Python入门")
    system.return_book("Python入门")
    system.borrow_book("红楼梦")
    system.return_book("红楼梦")

    system.login("小红", "456")
    system.borrow_book("Python入门")
    system.return_book("Python入门")
    system.borrow_book("Python入门")
    system.return_book("Python入门")
    system.borrow_book("算法导论")
    system.return_book("算法导论")

    # 测试 1: 借阅排行榜
    ranking = system.borrow_ranking()
    print("借阅排行榜:")
    for item in ranking:
        print(f"  {item}")

    # 测试 2: 热门图书 Top 2
    hot = system.hot_books(2)
    print(f"热门 Top 2: {hot}")

    # 测试 3: 导出统计报告
    system.export_report(report_path)
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            print("报告内容:")
            print(f.read())

    # 测试 4: 持久化
    system.save()
    system2 = LibrarySystemV3(data_path)
    system2.load()
    print(f"加载后图书数: {len(system2.books)}")

    # 清理
    for p in [data_path, report_path]:
        if os.path.exists(p):
            os.remove(p)
