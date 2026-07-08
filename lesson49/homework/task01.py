"""
[难度: ⭐⭐]
[所属知识点: CSV 存储]
[预计完成时间: 10 分钟]

题目描述:
    通过 requests 爬取 quotes.toscrape.com 首页,
    用 BeautifulSoup 提取所有名言的文本(text)和作者(author),
    使用 csv.DictWriter 写入 quotes_homework.csv 文件,
    表头为 text 和 author,编码为 UTF-8。

示例:
    >>> 运行后生成 quotes_homework.csv
    >>> 文件内容形如:
    text,author
    "The world as we have created it is...",
      Albert Einstein
    "It is our choices, Harry...",
      J.K. Rowling
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查文件是否存在且非空
    import os
    if os.path.exists("quotes_homework.csv"):
        with open("quotes_homework.csv", "r",
                  encoding="utf-8") as f:
            lines = f.readlines()
        print(f"文件共 {len(lines)} 行(含表头)")
        assert len(lines) > 1, "文件无数据"
        print("文件内容前 3 行:")
        for line in lines[:3]:
            print(f"  {line.strip()[:60]}")
    else:
        print("quotes_homework.csv 文件未生成")

    # 测试 2: 验证表头正确且数据条数 >= 10
    import csv
    if os.path.exists("quotes_homework.csv"):
        with open("quotes_homework.csv", "r",
                  encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert reader.fieldnames == ["text", "author"], \
            f"表头不正确: {reader.fieldnames}"
        print(f"表头校验通过,共 {len(rows)} 条数据")
        assert len(rows) >= 10, \
            f"数据不足 10 条: {len(rows)}"
