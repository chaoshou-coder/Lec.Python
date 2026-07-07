"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 类 + 异常 + CRUD]
[预计完成时间: 25 分钟]

题目描述:
实现一个类 Library,包含 books 列表,
定义 add_book(title, author) 添加图书,
定义 borrow_book(title) 借书(不存在或已借出抛异常),
定义 return_book(title) 还书(不存在或未借出抛异常),
定义 list_books() 列出所有图书状态。

示例:
    >>> lib = Library()
    >>> lib.add_book("Python入门", "张三")
    >>> lib.borrow_book("Python入门")
    >>> lib.list_books()
    [{'title': 'Python入门', 'author': '张三', 'borrowed': True}]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    lib = Library()

    # 测试 1: 添加图书
    lib.add_book("Python入门", "张三")
    lib.add_book("算法导论", "李四")
    print(lib.list_books())

    # 测试 2: 借书
    lib.borrow_book("Python入门")
    print(f"借出后: {lib.list_books()}")

    # 测试 3: 借不存在的书
    try:
        lib.borrow_book("不存在的书")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 4: 重复借书
    try:
        lib.borrow_book("Python入门")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 5: 还书
    lib.return_book("Python入门")
    print(f"还书后: {lib.list_books()}")

    # 测试 6: 还未借出就还
    try:
        lib.return_book("算法导论")
    except Exception as e:
        print(f"异常: {e}")
