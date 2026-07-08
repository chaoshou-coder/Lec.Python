"""
[难度: ⭐]
[所属知识点: 项目规划与数据流设计]
[预计完成时间: 5 分钟]

题目描述:
设计一个爬虫项目的完整数据流:请求 → 解析 → 清洗 → 存储。
给定以下伪代码框架,补全流程,打印每一步的输出示例:
  1. 请求阶段: 访问 URL,返回 HTML 片段
  2. 解析阶段: 从 HTML 中提取书名列表
  3. 清洗阶段: 去除空白字符,价格转为 float
  4. 存储阶段: 打印"已保存 N 条"

示例:
    >>> run()
    请求: GET http://books.toscrape.com/
    -> 回应: <html>... (共 8192 字符)
    解析: 提取书名
    -> ['A Light in the Attic', 'Tipping the Velvet']
    清洗: 价格 "£17.46" -> 17.46
    -> [17.46, 23.99]
    存储: 已保存 2 条
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常流程
    print("--- 测试 1 ---")
    html = "<html><body>"
    "<h3>A Light in the Attic</h3>"
    "<p>£17.46</p></body></html>"
    print(f"请求: GET http://books.toscrape.com/")
    print(f"-> 回应: {html[:20]}... (共 {len(html)} 字符)")
    titles = ["A Light in the Attic", "Tipping the Velvet"]
    print(f"解析: 提取书名 -> {titles}")
    prices = ["£17.46", "£23.99"]
    cleaned = [float(p.replace("£", "")) for p in prices]
    print(f"清洗: 价格 {prices} -> {cleaned}")
    print(f"存储: 已保存 {len(titles)} 条")

    # 测试 2: 空列表
    print("\n--- 测试 2: 空列表 ---")
    empty_titles = []
    print(f"解析: 提取书名 -> {empty_titles}")
    print(f"存储: 已保存 {len(empty_titles)} 条")
