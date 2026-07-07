"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 单元测试 + 综合]
[预计完成时间: 45 分钟]

题目描述:
完善图书管理系统(参考 practice04),添加单元测试,
至少包含 5 个测试用例,覆盖以下场景:
1. 添加图书成功
2. 借阅不存在的图书(异常)
3. 重复借阅同一本书(异常)
4. 归还图书成功
5. 删除图书成功

使用 unittest 模块编写测试。

示例:
    # 运行测试
    $ python -m unittest test_library.py
    .....
    Ran 5 tests in 0.001s
    OK
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import unittest

    class TestLibrarySystem(unittest.TestCase):
        def setUp(self):
            """每个测试前创建新系统"""
            from practice04 import LibrarySystem
            self.system = LibrarySystem("/tmp/test_unit.json")

        def test_add_book(self):
            """测试添加图书"""
            pass

        def test_borrow_nonexistent(self):
            """测试借阅不存在的图书"""
            pass

        def test_duplicate_borrow(self):
            """测试重复借阅"""
            pass

        def test_return_book(self):
            """测试归还图书"""
            pass

        def test_remove_book(self):
            """测试删除图书"""
            pass

    # 运行测试
    unittest.main(verbosity=2)
