"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 异常处理综合 — 自定义异常 +
 try / except / else / finally]
[预计完成时间: 25 分钟]

题目描述:
  实现一个"安全除法器",要求:
  1. 自定义异常 NegativeError(继承 Exception),当除数为
     负数时抛出
  2. 自定义异常 ZeroDivError(继承 Exception),当除数为 0
     时抛出(不用内置 ZeroDivisionError)
  3. 主流程用 try / except / else / finally 包裹:
     - try: 读取文件 "nums.txt",每行两个数 a b,计算 a/b
     - except FileNotFoundError: 提示"文件不存在"
     - except (NegativeError, ZeroDivError) as e: 提示 e
     - else: 全部计算完成时打印"全部计算成功"
     - finally: 打印"程序结束,资源已清理"

要求:
  - 自定义异常类要有 __init__ 接收消息
  - 不要裸 except:,必须指定类型
  - 文件操作使用 with + encoding="utf-8"

示例:
    >>> nums.txt 内容:
    10 2
    8 -1
    5 0

    >>> 运行程序
    第 1 行: 10 / 2 = 5.0
    第 2 行: 除数不能为负数
    第 3 行: 除数不能为零
    程序结束,资源已清理
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

    # 定义自定义异常(学员需自己写)
    class NegativeError(Exception):
        def __init__(self, msg="除数不能为负数"):
            self.msg = msg
            super().__init__(self.msg)

    class ZeroDivError(Exception):
        def __init__(self, msg="除数不能为零"):
            self.msg = msg
            super().__init__(self.msg)

    # 测试 1: 自定义异常可抛出并捕获
    caught = False
    try:
        raise NegativeError()
    except NegativeError as e:
        caught = True
        assert str(e) == "除数不能为负数"
    assert caught

    # 测试 2: ZeroDivError
    caught = False
    try:
        raise ZeroDivError()
    except ZeroDivError as e:
        caught = True
        assert str(e) == "除数不能为零"
    assert caught

    # 测试 3: 正常计算流程
    tmp = "test_nums.txt"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("10 2\n7 3\n")
    results = []
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            for line in f:
                a, b = line.strip().split()
                a, b = int(a), int(b)
                if b < 0:
                    raise NegativeError()
                if b == 0:
                    raise ZeroDivError()
                results.append(a / b)
    except FileNotFoundError:
        print("文件不存在")
    except (NegativeError, ZeroDivError) as e:
        print(e)
    else:
        assert results == [5.0, 7 / 3], "正常计算结果"
    finally:
        pass  # 清理
    os.remove(tmp)

    # 测试 4: 除数为负 → 抛 NegativeError
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("10 -2\n")
    caught = False
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            for line in f:
                a, b = line.strip().split()
                a, b = int(a), int(b)
                if b < 0:
                    raise NegativeError()
    except NegativeError:
        caught = True
    assert caught, "应捕获 NegativeError"
    os.remove(tmp)

    # 测试 5: 除数为 0 → 抛 ZeroDivError
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("10 0\n")
    caught = False
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            for line in f:
                a, b = line.strip().split()
                a, b = int(a), int(b)
                if b == 0:
                    raise ZeroDivError()
    except ZeroDivError:
        caught = True
    assert caught, "应捕获 ZeroDivError"
    os.remove(tmp)

    print("task03 测试通过 ✓")
