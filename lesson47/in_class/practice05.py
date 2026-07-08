"""
[难度: ⭐⭐⭐]
[所属知识点: Rule 与 LinkExtractor 翻页]
[预计完成时间: 15 分钟]

题目描述:
  使用 CrawlSpider + Rule(LinkExtractor(
  restrict_css=".next a")),自动翻页爬取
  quotes.toscrape.com 所有页面的名言。
  无需手动拼接下一页 URL,Rule 会自动跟随
  符合选择器的链接继续爬取。

示例:
    >>> scrapy crawl quotes
    # 第 1 页 10 条
    {'text': '...', 'author': '...'}
    # 第 2 页 10 条(自动翻页)
    {'text': '...', 'author': '...'}
    # …共 10 页 100 条
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 Spider 继承自 CrawlSpider
    # 测试 2: 验证 Rule 使用了 LinkExtractor
    # 测试 3: 验证能爬取多页(>1页)数据
    pass
