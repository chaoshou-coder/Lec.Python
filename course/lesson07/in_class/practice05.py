"""
[难度: ⭐⭐⭐]
[所属知识点: 基础异常处理 try / except FileNotFoundError
 / ValueError]
[预计完成时间: 12 分钟]

题目描述:
  写一个"安全打开文件"的程序:尝试读取用户指定的文件。
  如果文件不存在,捕获 FileNotFoundError 并提示"文件不存在";
  如果文件存在但内容不是数字,捕获 ValueError 并提示"内容
  无法转为数字";如果成功,打印该数字的平方。

要求:
  - 用 try / except 分别捕获两种异常
  - 不要裸写 except:,必须指定类型
  - 用 else 分支在无异常时打印结果

示例:
    >>> 运行程序(文件不存在时)
    文件不存在,请检查路径

    >>> 运行程序(文件内容是 abc 时)
    内容无法转为数字

    >>> 运行程序(文件内容是 5 时)
    5 的平方是 25
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

    # 测试 1: FileNotFoundError
    # 模拟:open 一个不存在的文件应抛 FileNotFoundError
    caught = False
    try:
        with open("no_such_file.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        caught = True
    assert caught, "应捕获 FileNotFoundError"

    # 测试 2: ValueError(文件存在但内容不是数字)
    tmp = "test_bad.txt"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("abc")
    caught = False
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            num = float(f.read())
    except ValueError:
        caught = True
    assert caught, "应捕获 ValueError"
    os.remove(tmp)

    # 测试 3: 正常情况(文件内容是数字)
    tmp = "test_good.txt"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("5")
    result = None
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            num = float(f.read())
    except (FileNotFoundError, ValueError):
        pass
    else:
        result = num ** 2
    assert result == 25, f"5 的平方应为 25,实际 {result}"
    os.remove(tmp)

    print("practice05 测试通过 ✓")
