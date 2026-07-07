"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: sort(key=lambda x: ...)]
[预计完成时间: 25 分钟]

题目描述:
    输入 N 个学生数据(姓名 + 成绩),计算平均分、最高分、最低分,
    按成绩降序输出。用 sort + lambda 实现排序。

示例:
    >>> students = [("张三", 85), ("李四", 92), ("王五", 78)]
    平均分: 85.0
    最高分: 92
    最低分: 78
    排序: [('李四', 92), ('张三', 85), ('王五', 78)]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
students = [("张三", 85), ("李四", 92), ("王五", 78)]
# 平均分
avg = sum(s[1] for s in students) / len(students)
# 最高最低分
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
highest = students_sorted[0][1]
lowest = students_sorted[-1][1]
print(f"平均分: {avg}")
print(f"最高分: {highest}")
print(f"最低分: {lowest}")
print(f"降序: {students_sorted}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常数据
    data1 = [("张三", 85), ("李四", 92), ("王5", 78)]
    d1 = sorted(data1, key=lambda x: x[1], reverse=True)
    print(f"测试1 排序: {d1}")

    # 测试 2: 一个元素
    data2 = [("唯一", 100)]
    print(f"测试2 平均分: {data2[0][1]}")

    # 测试 3: 成绩相同
    data3 = [("A", 80), ("B", 80)]
    print(f"测试3 排序: {sorted(data3, key=lambda x: x[1], reverse=True)}")
