"""
[难度: ⭐⭐⭐]
[所属知识点: JSON 反序列化 json.load / json.loads]
[预计完成时间: 12 分钟]

题目描述:
  你已经有一个 JSON 文件 "student.json",内容是一个学生字典
  (包含 name、age、scores 字段)。请用 json.load 读入并打印
  学生的平均分。然后再用 json.loads 解析一个 JSON 字符串,
  提取其中的 "city" 字段。

要求:
  - json.load 用于读文件,json.loads 用于读字符串
  - 平均分 = sum(scores) / len(scores),保留 1 位小数
  - 打印格式: "姓名 XX,平均分 YY" 和 "城市: ZZ"

示例:
    >>> 运行程序
    姓名 小明,平均分 89.0
    城市: 北京
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
    tmp = "test_student.json"

    # 创建测试 JSON 文件
    data = {"name": "小明", "age": 18, "scores": [90, 85, 92]}
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    # 测试 1: json.load 读文件
    with open(tmp, "r", encoding="utf-8") as f:
        obj = json.load(f)
    assert obj["name"] == "小明"
    avg = sum(obj["scores"]) / len(obj["scores"])
    assert avg == 89.0, f"平均分应为 89.0,实际 {avg}"

    # 测试 2: json.loads 解析字符串
    s = '{"city": "北京", "temp": 28}'
    parsed = json.loads(s)
    assert parsed["city"] == "北京"

    # 测试 3: json.loads 解析含中文的字符串
    s2 = '{"city": "上海"}'
    parsed2 = json.loads(s2)
    assert parsed2["city"] == "上海"

    os.remove(tmp)
    print("practice03 测试通过 ✓")
