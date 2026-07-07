"""
[难度: ⭐⭐⭐]
[所属知识点: JSON + 函数 + 排序 + CSV]
[预计完成时间: 20 分钟]

题目描述:
实现一个函数 process_students(path),读取 JSON 文件(学生列表),
过滤出成绩 ≥ 60 的学生,按成绩降序排序,导出为 CSV 文件。
JSON 格式: [{"name": "小明", "score": 85}, ...]
CSV 格式: name,score (含表头)。

示例:
    # 假设 students.json 内容如上
    >>> process_students("students.json")
    # 生成 students_pass.csv,内容为及格学生
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import json, os

    # 准备测试数据
    test_data = [
        {"name": "小明", "score": 85},
        {"name": "小红", "score": 55},
        {"name": "小刚", "score": 92},
        {"name": "小丽", "score": 60},
        {"name": "小强", "score": 48},
    ]
    test_path = "/tmp/test_students.json"
    with open(test_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)

    # 测试 1: 正常处理
    result = process_students(test_path)
    print(f"及格人数: {result}")

    # 测试 2: 验证 CSV 文件生成
    csv_path = test_path.replace(".json", "_pass.csv")
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            print(f.read())

    # 测试 3: 全部不及格
    fail_data = [{"name": "a", "score": 30}, {"name": "b", "score": 20}]
    with open(test_path, "w", encoding="utf-8") as f:
        json.dump(fail_data, f, ensure_ascii=False)
    result2 = process_students(test_path)
    print(f"全部不及格人数: {result2}")

    # 清理
    for p in [test_path, csv_path]:
        if os.path.exists(p):
            os.remove(p)
