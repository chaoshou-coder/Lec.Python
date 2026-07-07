"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 作品展示]
[预计完成时间: 60 分钟]

题目描述:
录制 3 分钟 demo 视频,展示图书管理系统的核心功能。
视频应包含以下内容:
1. 系统启动和欢迎界面
2. 添加若干本图书
3. 查询图书
4. 借阅图书(成功场景)
5. 借阅图书(异常场景 - 已借出)
6. 归还图书
7. 列出所有图书状态
8. 数据持久化演示(重启后数据仍在)

本文件为视频脚本大纲,供录制时参考。

示例(视频脚本大纲):
    [00:00-00:30] 开场介绍
    [00:30-01:00] 添加图书
    [01:00-01:30] 借阅图书
    [01:30-02:00] 异常处理演示
    [02:00-02:30] 归还 + 列出
    [02:30-03:00] 持久化演示 + 总结
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 演示脚本:模拟视频中的操作流程
    import os

    data_path = "/tmp/demo_lib.json"

    print("=" * 40)
    print("图书管理系统 Demo")
    print("=" * 40)

    # 导入系统(假设已完成 practice04)
    try:
        from practice04 import LibrarySystem
    except ImportError:
        print("请先完成 practice04.py")
        exit(1)

    system = LibrarySystem(data_path)

    # 1. 添加图书
    print("\n[步骤 1] 添加图书")
    system.add_book("Python入门", "张三")
    system.add_book("算法导论", "李四")
    system.add_book("红楼梦", "曹雪芹")

    # 2. 列出图书
    print("\n[步骤 2] 列出图书")
    system.list_books()

    # 3. 借阅
    print("\n[步骤 3] 借阅图书")
    system.borrow_book("Python入门", "小明")

    # 4. 异常演示
    print("\n[步骤 4] 异常演示")
    try:
        system.borrow_book("Python入门", "小红")
    except Exception as e:
        print(f"异常: {e}")

    # 5. 归还
    print("\n[步骤 5] 归还图书")
    system.return_book("Python入门")

    # 6. 持久化
    print("\n[步骤 6] 持久化演示")
    system.save()
    system2 = LibrarySystem(data_path)
    system2.load()
    print(f"重启后图书数: {len(system2.books)}")

    # 清理
    if os.path.exists(data_path):
        os.remove(data_path)

    print("\nDemo 结束!")
