"""
[难度: ⭐⭐]
[所属知识点: yield 返回 Item]
[预计完成时间: 10 分钟]

题目描述:
  修改 Spider,在 parse 中为每条名言 yield 一个 dict,
  包含 text 和 author 两个字段。
  使用 response.css 配合 ::text 伪类提取文本,
  用 .get() 方法获取字符串。

示例:
    >>> scrapy crawl quotes
    {'text': 'The world as we have created it...',
     'author': 'Albert Einstein'}
    {'text': 'It is our choices, Harry...',
     'author': 'J.K. Rowling'}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证每条结果包含 text 和 author
    # 测试 2: 验证 text 字段非空字符串
    # 测试 3: 验证 author 字段非空字符串
    pass
