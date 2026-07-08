"""
[难度: ⭐]
[所属知识点: 数据保存到 JSON 文件]
[预计完成时间: 5 分钟]

题目描述:
通过 requests 爬取 quotes.toscrape.com 首页,
提取前 3 条名言的文本和作者,
将每条数据存为 {"text":"...", "author":"..."} 格式,
最后将列表写入 quotes.json 文件(UTF-8 编码)。

示例:
    >>> 运行后生成 quotes.json
    >>> 内容形如:
    [
        {"text": "The world...", "author": "Albert Einstein"},
        {"text": "It is...", "author": "J.K. Rowling"},
        {"text": "The person...", "author": "Albert Einstein"}
    ]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查 quotes.json 文件是否生成
    import os, json
    if os.path.exists("quotes.json"):
        with open("quotes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"共写入 {len(data)} 条名言")
        for item in data:
            print(f"  - {item['author']}: {item['text'][:30]}...")
    else:
        print("quotes.json 文件未生成")

    # 测试 2: 验证每条数据包含 text 和 author 字段
    if os.path.exists("quotes.json"):
        with open("quotes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            assert "text" in item and "author" in item, \
                "缺少必要字段 text 或 author"
        print("所有数据字段校验通过")
