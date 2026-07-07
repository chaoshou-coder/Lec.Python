"""
[难度: ⭐⭐⭐]
[所属知识点: __str__]
[预计完成时间: 15 分钟]

题目描述:
在 Student 类中添加 __str__ 方法,返回 "Student(XX, YY)",
其中 XX 是 name,YY 是 age。

示例:
    >>> s = Student("小明", 18)
    >>> print(s)
    Student(小明, 18)
    >>> str(s)
    'Student(小明, 18)'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    s1 = Student("小明", 18)
    print(s1)

    # 测试 2: 使用 str() 转换
    s2 = Student("小红", 20)
    result = str(s2)
    print(result)

    # 测试 3: 年龄为 0
    s3 = Student("宝宝", 0)
    print(s3)
