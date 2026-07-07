"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 类 + JSON + CRUD]
[预计完成时间: 25 分钟]

题目描述:
实现一个类 StudentManager,包含 students 列表,
定义 add_student(name, score) 添加学生,
定义 remove_student(name) 按姓名删除,
定义 find_student(name) 按姓名查找,
数据持久化到 JSON 文件(save/load)。

示例:
    >>> sm = StudentManager("/tmp/students.json")
    >>> sm.add_student("小明", 85)
    >>> sm.find_student("小明")
    {'name': '小明', 'score': 85}
    >>> sm.remove_student("小明")
    True
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

    data_path = "/tmp/test_sm.json"

    # 测试 1: 添加和查找
    sm = StudentManager(data_path)
    sm.add_student("小明", 85)
    sm.add_student("小红", 92)
    print(sm.find_student("小明"))

    # 测试 2: 删除
    result = sm.remove_student("小明")
    print(f"删除成功: {result}")
    print(sm.find_student("小明"))

    # 测试 3: 持久化
    sm.save()
    sm2 = StudentManager(data_path)
    sm2.load()
    print(f"加载后学生数: {len(sm2.students)}")

    # 测试 4: 删除不存在的学生
    result2 = sm.remove_student("不存在的")
    print(f"删除不存在: {result2}")

    # 清理
    if os.path.exists(data_path):
        os.remove(data_path)
