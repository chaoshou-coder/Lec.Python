"""
[难度: ⭐⭐⭐]
[所属知识点: 实例方法 + 布尔]
[预计完成时间: 15 分钟]

题目描述:
在 Student 类中添加实例方法 is_adult(),返回 True 如果 age ≥ 18,
否则返回 False。

示例:
    >>> s1 = Student("小明", 20)
    >>> s1.is_adult()
    True
    >>> s2 = Student("小红", 15)
    >>> s2.is_adult()
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 成年人
    s1 = Student("小明", 20)
    print(s1.is_adult())

    # 测试 2: 未成年人
    s2 = Student("小红", 15)
    print(s2.is_adult())

    # 测试 3: 刚好 18 岁(边界)
    s3 = Student("小刚", 18)
    print(s3.is_adult())
