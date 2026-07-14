"""
[难度: ⭐⭐⭐]
[所属知识点: 文件写入 write / writelines]
[预计完成时间: 12 分钟]

题目描述:
  请你用 with 语句创建一个 "score.txt" 文件,写入一个班级的
  成绩单。先用 write() 逐行写入 3 个学生的信息,然后再用
  writelines() 追加 2 个转学生的信息。最终文件应有 5 行。

要求:
  - 每行格式: "姓名,分数\n"(注意 write 不会自动加换行)
  - 前 3 行用 write() 写入(模式 'w')
  - 后 2 行用 writelines() 追加(模式 'a')
  - 最后用 readlines() 读出并 print 行数,确认是 5 行

示例:
    >>> 运行程序
    共写入 5 行
    第 1 行: 小明,95
    第 2 行: 小红,88
    第 3 行: 小刚,72
    第 4 行: 小丽,91
    第 5 行: 小强,86
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
    tmp = "test_score.txt"

    # 测试 1: write() 写入 3 行
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("小明,95\n")
        f.write("小红,88\n")
        f.write("小刚,72\n")

    # 测试 2: writelines() 追加 2 行
    lines = ["小丽,91\n", "小强,86\n"]
    with open(tmp, "a", encoding="utf-8") as f:
        f.writelines(lines)

    # 测试 3: 读取验证共 5 行
    with open(tmp, "r", encoding="utf-8") as f:
        result = f.readlines()
    assert len(result) == 5, f"应有 5 行,实际 {len(result)}"
    assert result[0].strip() == "小明,95"
    assert result[4].strip() == "小强,86"

    # 测试 4: writelines 不带换行会粘在一起
    with open(tmp, "w", encoding="utf-8") as f:
        f.writelines(["A", "B"])  # 没换行
    with open(tmp, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "AB", "writelines 不自动加换行"

    os.remove(tmp)
    print("practice02 测试通过 ✓")
