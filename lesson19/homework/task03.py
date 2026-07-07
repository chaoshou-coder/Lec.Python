"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 类 + 列表 + 字典 + 方法]
[预计完成时间: 25 分钟]

题目描述:
定义一个类 Library,包含 books 列表(存储书名)和 borrowed 字典(记录借阅关系),
定义 add_book(title) 添加图书,
定义 borrow_book(title, user) 借书(书不存在或已借出抛异常),
定义 return_book(title) 还书(书未借出抛异常),
定义 list_books() 列出所有图书及状态。

示例:
    >>> lib = Library()
    >>> lib.add_book("Python入门")
    >>> lib.borrow_book("Python入门", "小明")
    >>> lib.list_books()
    Python入门 - 已借出(借阅者: 小明)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 添加并借阅图书
    lib = Library()
    lib.add_book("Python入门")
    lib.add_book("算法导论")
    lib.borrow_book("Python入门", "小明")
    lib.list_books()

    # 测试 2: 归还图书
    lib.return_book("Python入门")
    lib.list_books()

    # 测试 3: 借出不存在的书
    try:
        lib.borrow_book("不存在的书", "小红")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 4: 借出已借出的书
    lib.borrow_book("算法导论", "小红")
    try:
        lib.borrow_book("算法导论", "小刚")
    except Exception as e:
        print(f"异常: {e}")
