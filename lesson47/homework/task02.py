"""
[难度: ⭐⭐⭐⭐]
[所属知识点: CrawlSpider 全栈爬取]
[预计完成时间: 20 分钟]

题目描述:
  用 CrawlSpider 爬取 books.toscrape.com
  所有书名和价格,通过 Rule 自动翻页,
  用 BookItem 存储结果,在 close_spider
  中打印总共爬取数量。练习 CrawlSpider、
  Item、Pipeline 的完整协作流程。

示例:
    >>> scrapy crawl books
    {'title': 'A Light in the Attic',
     'price': '£51.77'}
    {'title': 'Tipping the Velvet',
     'price': '£53.74'}
    # …共 50 页
    总共爬取书籍数量: 1000
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 BookItem 有 title 和 price 字段
    # 测试 2: 验证 Spider 能翻页爬取多页
    # 测试 3: 验证 close_spider 打印总数
    pass
