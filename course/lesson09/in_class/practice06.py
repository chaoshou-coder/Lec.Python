"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 函数 + 二维列表 + CRUD]
[预计完成时间: 25 分钟]

题目描述:
    用二维列表存储学生信息(学号/姓名/成绩),用函数实现:
    - add_student(lst, sid, name, score) 添加学生
    - find_student(lst, sid) 按学号查询,返回信息或 None
    - remove_student(lst, sid) 按学号删除
    并给出示例调用示例。
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def add_student(lst, sid, name, score):
    lst.append([sid, name, score])
    print(f"已添加: {sid} {name} {score}")


def find_student(lst, sid):
    for s in lst:
        if s[0] == sid:
            return s
    return None


def remove_student(lst, sid):
    for s in lst:
        if s[0] == sid:
            lst.remove(s)
            print(f"已删除学号 {sid}")
            return True
    print(f"未找到学号 {sid}")
    return False


# 示例调用
students = []
add_student(students, "001", "张三", 90)
add_student(students, "002", "李四", 85)
print("查找 001:", find_student(students, "001"))
remove_student(students, "002")
print("当前学生:", students)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 添加和查询
    data = []
    add_student(data, "A1", "王五", 78)
    found = find_student(data, "A1")
    print(f"测试1 查找: {found}")

    # 测试 2: 删除不存在
    ok = remove_student(data, "Z9")
    print(f"测试2 删除不存在的返回值: {ok}")

    # 测试 3: 查找不存在
    print(f"测试3 查找不存在: {find_student(data, 'X0')}")
