"""
[难度: ⭐⭐⭐]
[所属知识点: Pipeline 数据处理]
[预计完成时间: 15 分钟]

题目描述:
  编写一个 QuotePipeline 类,在 process_item
  中将 text 字段首字母大写,并打印
  "正在处理:作者名"。包含完整 pipeline 代码
  (open_spider、process_item、close_spider)。
  需要在 settings.py 中注册才能生效。

示例:
    >>> scrapy crawl quotes
    正在处理: Albert Einstein
    正在处理: J.K. Rowling
    # 每条 item 的 text 首字母已大写
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 process_item 返回了 item
    # 测试 2: 验证 text 字段首字母为大写
    # 测试 3: 验证调用了 print 输出作者名
    pass
