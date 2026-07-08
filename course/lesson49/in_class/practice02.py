"""
[难度: ⭐⭐]
[所属知识点: 数据保存到 CSV]
[预计完成时间: 10 分钟]

题目描述:
通过 requests 爬取 quotes.toscrape.com 首页,
提取所有名言的文本和作者,
使用 csv.DictWriter 写入 quotes.csv 文件,
表头为 text 和 author, 编码为 UTF-8。

示例:
    >>> 运行后生成 quotes.csv
    >>> 文件内容形如:
    text,author
    "The world...",Albert Einstein
    "It is...",J.K. Rowling
    "The person...",Albert Einstein
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查 quotes.csv 文件是否存在且非空
    import os, csv
    if os.path.exists("quotes.csv"):
        with open("quotes.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        print(f"共写入 {len(rows)} 条名言到 quotes.csv")
        for row in rows[:3]:
            print(f"  - {row['author']}: {row['text'][:30]}...")
    else:
        print("quotes.csv 文件未生成")

    # 测试 2: 验证表头字段正确
    if os.path.exists("quotes.csv"):
        with open("quotes.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
        assert header == ["text", "author"], \
            f"表头不正确: {header}"
        print("表头校验通过")
