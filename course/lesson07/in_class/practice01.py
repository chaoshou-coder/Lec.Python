"""
[难度: ⭐⭐]
[所属知识点: 文件读取 read / readline / readlines]
[预计完成时间: 8 分钟]

题目描述:
  老师已经在当前目录创建了一个 "diary.txt" 文件,内容是三行
  日记。请你用 with 语句打开文件,分别演示三种读取方式:
  先 read() 全部读出,再 readline() 读一行,再 readlines()
  读成列表。每次读取前用 open 重新打开(否则指针已在末尾)。

要求:
  - 使用 with open(...) as f: 的写法
  - 必须写 encoding="utf-8"
  - 三种读取结果各 print 一次,并加注释说明

示例:
    >>> 运行程序
    [read() 结果]
    2026-07-01 晴 今天学了 Python

    [readline() 结果]
    2026-07-01 晴 今天学了 Python

    [readlines() 结果]
    ['2026-07-01 晴 今天学了 Python\n', ...]
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
    tmp = "test_diary.txt"
    # 创建测试文件
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("2026-07-01 晴 今天学了 Python\n")
        f.write("2026-07-02 阴 练习了循环\n")
        f.write("2026-07-03 晴 写了小项目\n")

    # 测试 1: read() 返回字符串
    with open(tmp, "r", encoding="utf-8") as f:
        content = f.read()
    assert isinstance(content, str), "read() 应返回字符串"
    assert "今天学了 Python" in content

    # 测试 2: readline() 返回一行
    with open(tmp, "r", encoding="utf-8") as f:
        line = f.readline()
    assert isinstance(line, str), "readline() 应返回字符串"
    assert line.endswith("\n"), "readline() 保留换行符"

    # 测试 3: readlines() 返回列表
    with open(tmp, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert isinstance(lines, list), "readlines() 应返回列表"
    assert len(lines) == 3, f"应有 3 行,实际 {len(lines)}"

    os.remove(tmp)
    print("practice01 测试通过 ✓")
