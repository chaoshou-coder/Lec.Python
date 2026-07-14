"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 日记本持久化 — 读/写 JSON 文件]
[预计完成时间: 20 分钟]

题目描述:
  实现一个"日记本"程序,启动时从 diary.json 读取历史日记
  (每条是一个字符串),让用户输入新日记追加到列表中,输入
  quit 时把所有日记写回文件并退出。

要求:
  - 启动时读 diary.json,文件不存在则用空列表开始
  - 每次输入后立刻写回文件(防止数据丢失)
  - 输入 quit 时打印全部日记再退出
  - 所有文件操作使用 with + encoding="utf-8"
  - json.dump 时加 ensure_ascii=False 和 indent=2

示例:
    >>> 运行程序
    写日记(quit 退出): 今天天气真好
    已保存
    写日记(quit 退出): 学了文件 I/O
    已保存
    写日记(quit 退出): quit
    --- 你的日记 ---
    1. 今天天气真好
    2. 学了文件 I/O
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
    tmp = "test_diary.json"

    # 测试 1: 文件不存在 → 读入空列表
    if os.path.exists(tmp):
        os.remove(tmp)
    # 模拟学员逻辑
    diary = []
    if os.path.exists(tmp):
        with open(tmp, "r", encoding="utf-8") as f:
            diary = json.load(f)
    assert diary == [], "文件不存在时应为空列表"

    # 测试 2: 追加日记并写回
    diary.append("今天天气真好")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(diary, f, ensure_ascii=False, indent=2)
    with open(tmp, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    assert reloaded == ["今天天气真好"], "写回后应能读回"

    # 测试 3: 多次追加
    diary.append("学了文件 I/O")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(diary, f, ensure_ascii=False, indent=2)
    with open(tmp, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    assert len(reloaded) == 2
    assert reloaded[1] == "学了文件 I/O"

    # 测试 4: 中文不被转义
    with open(tmp, "r", encoding="utf-8") as f:
        raw = f.read()
    assert "今天天气真好" in raw, "ensure_ascii=False 中文不转义"

    os.remove(tmp)
    print("task01 测试通过 ✓")
