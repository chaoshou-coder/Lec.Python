"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 继承 + 多态 + 文件操作]
[预计完成时间: 20 分钟]

题目描述:
定义一个基类 FileHandler,包含 read() 和 write(data) 方法;
定义子类 TextFileHandler,重写 read() 和 write() 用于读写 txt 文件;
定义子类 JsonFileHandler,重写 read() 和 write() 用于读写 json 文件。

示例:
    >>> th = TextFileHandler("/tmp/test.txt")
    >>> th.write("你好")
    >>> print(th.read())
    你好
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import tempfile, os

    # 测试 1: TextFileHandler
    tmp = tempfile.mktemp(suffix=".txt")
    th = TextFileHandler(tmp)
    th.write("你好世界")
    print(f"读取文本: {th.read()}")

    # 测试 2: JsonFileHandler
    tmp2 = tempfile.mktemp(suffix=".json")
    jh = JsonFileHandler(tmp2)
    jh.write({"name": "小明", "age": 18})
    print(f"读取 JSON: {jh.read()}")

    # 测试 3: 写入空内容
    tmp3 = tempfile.mktemp(suffix=".txt")
    th2 = TextFileHandler(tmp3)
    th2.write("")
    print(f"读取空内容: '{th2.read()}'")

    # 清理临时文件
    for f in [tmp, tmp2, tmp3]:
        if os.path.exists(f):
            os.remove(f)
