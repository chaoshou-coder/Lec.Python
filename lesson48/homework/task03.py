"""
[难度: ⭐⭐⭐⭐]
[所属知识点: User-Agent 池 + robots.txt 检查]
[预计完成时间: 20 分钟]

题目描述:
创建一个 UA_POOL 列表,包含至少 4 个不同的 User-Agent 字符串,
编写一个 fetch_with_random ua(url) 函数,每次请求随机选取一个 UA。
再用 urllib.robotparser 检查目标网站的 robots.txt,
判断是否允许爬取目标路径。
最后打印实际使用的 User-Agent 和 robots 检查结果。

要求:
    1. UA_POOL 包含 ≥ 4 个真实浏览器 UA 字符串
    2. 每次请求随机选择一个 UA(使用 random.choice)
    3. 使用 urllib.robotparser.RobotFileParser 解析 robots.txt
    4. 打印形如:
       "使用 UA: Mozilla/5.0 ..."
       "robots 允许爬取: True/False"

示例:
    >>> result = fetch_with_random_ua(
    ...     "https://quotes.toscrape.com/page/1/")
    >>> # 输出(示例):
    >>> # 使用 UA: Mozilla/5.0 (Windows NT 10.0; Win64; ...
    >>> # robots 允许爬取: True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: UA_POOL 列表包含至少 4 个 UA
    # assert isinstance(UA_POOL, list) and len(UA_POOL) >= 4

    # 测试 2: fetch_with_random_ua 返回 Response 且状态码 200
    # resp = fetch_with_random_ua(
    #     "https://quotes.toscrape.com/page/1/")
    # assert resp.status_code == 200

    # 测试 3: robots 检查对允许路径返回 True
    # allowed = check_robots(
    #     "https://quotes.toscrape.com/", "/page/1/")
    # assert allowed is True

    pass
