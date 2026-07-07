"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 类 + JSON + 异常 + 多用户]
[预计完成时间: 30 分钟]

题目描述:
在题 4 基础上,加入用户管理:
1. 读者注册(用户名, 密码)
2. 读者登录(验证用户名密码)
3. 登录后才能借书(记录借阅者)
4. 支持多读者借阅不同图书
5. 用户数据也持久化到 JSON

示例:
    >>> system = LibrarySystemV2("/tmp/lib_v2.json")
    >>> system.register("小明", "123456")
    >>> system.login("小明", "123456")
    True
    >>> system.add_book("Python入门", "张三")
    >>> system.borrow_book("Python入门")
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

    data_path = "/tmp/test_lib_v2.json"

    # 测试 1: 注册
    system = LibrarySystemV2(data_path)
    system.register("小明", "123456")
    system.register("小红", "abcdef")

    # 测试 2: 登录
    print(f"登录小明: {system.login('小明', '123456')}")
    print(f"密码错误: {system.login('小明', 'wrong')}")

    # 测试 3: 添加图书(无需登录)
    system.add_book("Python入门", "张三")
    system.add_book("算法导论", "李四")

    # 测试 4: 借书(需登录)
    system.borrow_book("Python入门")
    system.list_books()

    # 测试 5: 切换用户借书
    system.login("小红", "abcdef")
    system.borrow_book("算法导论")
    system.list_books()

    # 测试 6: 未登录借书
    system.logout()
    try:
        system.borrow_book("Python入门")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 7: 重复注册
    try:
        system.register("小明", "newpass")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 8: 持久化
    system.save()
    system2 = LibrarySystemV2(data_path)
    system2.load()
    print(f"加载后用户数: {len(system2.users)}")

    # 清理
    if os.path.exists(data_path):
        os.remove(data_path)
