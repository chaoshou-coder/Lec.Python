"""
[难度: ⭐⭐]
[所属知识点: Item 定义]
[预计完成时间: 10 分钟]

题目描述:
  定义一个 QuoteItem 类(继承 scrapy.Item),
  有 text 和 author 两个 Field。
  在 Spider 的 parse 方法中实例化 QuoteItem,
  赋值后 yield。使用 Item 可让 Pipeline 更规范地
  处理结构化数据。

示例:
    >>> scrapy crawl quotes
    {'text': 'The world as we have created it...',
     'author': 'Albert Einstein'}
    # 输出类型为 QuoteItem 实例
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 QuoteItem 是 scrapy.Item 的子类
    # 测试 2: 验证 QuoteItem 有 text 和 author 字段
    # 测试 3: 验证 parse yield 的是 QuoteItem 实例
    pass
