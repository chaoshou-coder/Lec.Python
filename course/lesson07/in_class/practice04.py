"""
[难度: ⭐⭐⭐]
[所属知识点: JSON 序列化 json.dump / json.dumps]
[预计完成时间: 13 分钟]

题目描述:
  你有一个学生字典列表,需要把它保存为 JSON 文件,并且还要
  生成一个 JSON 字符串用于"网络传输"。请分别用 json.dump
  写文件、json.dumps 转字符串两种方式完成。

要求:
  - json.dump 写文件时加 ensure_ascii=False 和 indent=2
  - json.dumps 转字符串时也加 ensure_ascii=False
  - 写完后读回文件,验证内容一致
  - 打印 dumps 返回的字符串,确认是 str 类型

示例:
    >>> 运行程序
    dumps 类型: <class 'str'>
    dumps 内容: [{"name": "小明", "age": 18}, ...]
    文件读回验证通过
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
    tmp = "test_class.json"

    students = [
        {"name": "小明", "age": 18},
        {"name": "小红", "age": 19}
    ]

    # 测试 1: json.dump 写文件
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    # 测试 2: 读回验证
    with open(tmp, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == students, "读回内容应与原数据一致"

    # 测试 3: json.dumps 返回字符串
    s = json.dumps(students, ensure_ascii=False)
    assert isinstance(s, str), "dumps 应返回字符串"
    assert "小明" in s, "ensure_ascii=False 时中文不转义"

    # 测试 4: 对比 ensure_ascii=True 时中文被转义
    s2 = json.dumps(students, ensure_ascii=True)
    assert "\\u" in s2, "ensure_ascii=True 时中文应被转义"

    os.remove(tmp)
    print("practice04 测试通过 ✓")
