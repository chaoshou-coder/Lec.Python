"""
[难度: ⭐⭐]
[所属知识点: CSS 选择器提取数据]
[预计完成时间: 10 分钟]

题目描述:
  在 Spider 中用
  response.css(".quote .text::text").getall()
  获取所有名言,用
  response.css(".quote .author::text").getall()
  获取作者,再用 zip 函数组合后 yield 每条结果。
  这样可比逐条提取更简洁高效。

示例:
    >>> scrapy crawl quotes
    {'text': 'The world as we have created it...',
     'author': 'Albert Einstein'}
    {'text': 'It is our choices, Harry...',
     'author': 'J.K. Rowling'}
    # 第一页共 10 条
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证第一页提取到 10 条名言
    # 测试 2: 验证每条结果 text 和 author 均非空
    # 测试 3: 验证使用了 zip 函数组合两个列表
    pass
