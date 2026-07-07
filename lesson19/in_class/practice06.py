"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 类 + 方法 + 异常]
[预计完成时间: 25 分钟]

题目描述:
定义一个类 Book,包含属性 title/author/price/is_borrowed,
定义 borrow() 方法借书:如果已借出,抛出 Exception("已被借出");
定义 return_book() 方法还书:如果未借出,抛出 Exception("未被借出")。

示例:
    >>> b = Book("Python入门", "张三", 59.9)
    >>> b.borrow()
    >>> b.borrow()
    Exception: 已被借出
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常借还
    b1 = Book("Python入门", "张三", 59.9)
    b1.borrow()
    print(f"已借出: {b1.is_borrowed}")
    b1.return_book()
    print(f"已借出: {b1.is_borrowed}")

    # 测试 2: 重复借书抛出异常
    b2 = Book("算法导论", "李四", 128.0)
    b2.borrow()
    try:
        b2.borrow()
    except Exception as e:
        print(f"异常: {e}")

    # 测试 3: 还未借出就还书
    b3 = Book("红楼梦", "曹雪芹", 45.0)
    try:
        b3.return_book()
    except Exception as e:
        print(f"异常: {e}")
