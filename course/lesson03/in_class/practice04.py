"""
[难度: ⭐⭐⭐]
[所属知识点: rfind() 与切片]
[预计完成时间: 15 分钟]

题目描述:
  输入一个文件路径,提取文件名(不含后缀)和后缀名(含点)。
  例如:输入 "/tmp/data/a.txt",应提取文件名 "a" 和后缀名 ".txt"。
  要求使用 rfind() 定位最后一个 / 和最后一个 . 的位置,
  再用切片分别提取。

示例:
    >>> "/tmp/data/a.txt" → 文件名 "a",后缀名 ".txt"
    >>> "/home/user/readme.md" → 文件名 "readme",后缀名 ".md"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
path = "/tmp/data/a.txt"
slash_index = path.rfind("/")
dot_index = path.rfind(".")
filename = path[slash_index + 1:dot_index]
extname = path[dot_index:]

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 常规路径
    path_1 = "/tmp/data/a.txt"
    s_1 = path_1.rfind("/")
    d_1 = path_1.rfind(".")
    name_1 = path_1[s_1 + 1:d_1]
    ext_1 = path_1[d_1:]
    print(f"文件名: {name_1},后缀名: {ext_1}")
    assert name_1 == "a"
    assert ext_1 == ".txt"

    # 测试 2: 多级目录路径
    path_2 = "/home/user/readme.md"
    s_2 = path_2.rfind("/")
    d_2 = path_2.rfind(".")
    name_2 = path_2[s_2 + 1:d_2]
    ext_2 = path_2[d_2:]
    print(f"文件名: {name_2},后缀名: {ext_2}")
    assert name_2 == "readme"
    assert ext_2 == ".md"

    # 测试 3: 无目录,只有文件名
    path_3 = "report.pdf"
    s_3 = path_3.rfind("/")
    d_3 = path_3.rfind(".")
    name_3 = path_3[s_3 + 1:d_3]
    ext_3 = path_3[d_3:]
    print(f"文件名: {name_3},后缀名: {ext_3}")
    assert name_3 == "report"
    assert ext_3 == ".pdf"

    print("所有测试通过!")
