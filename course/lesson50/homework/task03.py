"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 端到端数据集产出 + README]
[预计完成时间: 20 分钟]

题目描述:
    从 books.toscrape.com 爬取前 3 页共约 60 本书,
    依次完成:
      1. 请求:requests + headers + sleep(礼貌爬取)
      2. 解析:BeautifulSoup 提取书名 / 价格 / 评分
      3. 清洗:去重 + 价格转 float + rating 英文转 int
         评分 >=4 → positive, <=2 → negative, =3 → neutral
      4. 划分:先 dedup 再 split(8:2)
      5. 保存:分别写入 books_train.json 和 books_test.json
         生成 dataset_report.txt(条数、分布)
      6. 固定 random.seed(42) 保证可复现

示例:
    >>> 运行后生成文件:
    books_train.json(约 48 条)
    books_test.json(约 12 条)
    dataset_report.txt:
      总条数: 60
      训练集: 48
      测试集: 12
      positive: 25 (41.7%)
      neutral: 20 (33.3%)
      negative: 15 (25.0%)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import json
    import os

    # 测试 1: 验证 JSON 文件写入和读取
    print("--- 测试 1:JSON 读写 ---")
    sample_data = [
        {"title": "Book A", "rating": 5,
         "sentiment": "positive"},
        {"title": "Book B", "rating": 2,
         "sentiment": "negative"},
    ]
    path = "_test_books_train.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False,
                  indent=2)
    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert len(loaded) == 2
    assert loaded[0]["title"] == "Book A"
    print("JSON 读写通过")
    os.remove(path)

    # 测试 2: 验证 report 格式
    print("\n--- 测试 2:Report 格式 ---")
    stats = {"positive": 25, "neutral": 20, "negative": 15}
    total = sum(stats.values())
    report_lines = [f"总条数: {total}"]
    for k, v in stats.items():
        report_lines.append(
            f"  {k}: {v} ({v/total*100:.1f}%)")
    report_path = "_test_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "总条数: 60" in content
    assert "positive: 25" in content
    print("Report 格式通过")
    print("--- Report 内容 ---")
    print(content)
    os.remove(report_path)
