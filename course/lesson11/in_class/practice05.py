"""
[难度: ⭐⭐⭐⭐]
[所属知识点: lambda + sort(key=...)]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 sort_students(students, key='name'),
    根据 key 对学生列表(字典构成的列表)排序,默认按姓名。

示例:
    >>> students = [
    ...     {"name": "张三", "score": 85},
    ...     {"name": "李四", "score": 92},
    ... ]
    >>> sort_students(students, key='score')
    [{'name': '张三', 'score': 85}, {'name': '李四', 'score': 92}]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def sort_students(students, key='name'):
    return sorted(students, key=lambda s: s[key])


# 示例调用
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
print("按姓名:", sort_students(students))
print("按成绩:", sort_students(students, key='score'))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 按姓名排序
    data = [
        {"name": "Charlie", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 20},
    ]
    print(f"测试1 按name: {sort_students(data)}")

    # 测试 2: 按年龄排序
    print(f"测试2 按age: {sort_students(data, key='age')}")

    # 测试 3: 空列表
    print(f"测试3 空列表: {sort_students([])}")
