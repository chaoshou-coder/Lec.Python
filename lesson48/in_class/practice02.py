"""
[难度: ⭐⭐]
[所属知识点: User-Agent 池随机轮换]
[预计完成时间: 10 分钟]

题目描述:
定义一个包含 5 个不同浏览器 User-Agent 的列表,
每次请求时随机选择一个 User-Agent,访问
httpbin.org/user-agent 验证随机效果(共请求 3 次),
体会 User-Agent 池如何降低被封禁的风险。

示例:
    >>> 第 1 次请求 UA → "Mozilla/5.0 (Windows NT 10.0; ...)"
    >>> 第 2 次请求 UA → "Mozilla/5.0 (Macintosh; Intel ...)"
    >>> 第 3 次请求 UA → "Mozilla/5.0 (X11; Linux ...)"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import random
import requests

# 定义 User-Agent 池(5 个不同浏览器 UA)
ua_pool = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) "
    "Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 Mobile/15E148",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 Edg/120.0.0.0",
]

url = "https://httpbin.org/user-agent"

# 循环 3 次,每次随机选择一个 UA 发送请求
for i in range(1, 4):
    chosen_ua = random.choice(ua_pool)
    headers = {"User-Agent": chosen_ua}
    resp = requests.get(url, headers=headers)
    print(f"第 {i} 次请求 UA: {resp.json()['user-agent']}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 从池中随机选择 UA 应属于池子之一
    ua = random.choice(ua_pool)
    assert ua in ua_pool
    print("测试 1 通过: 随机选择的 UA 属于 UA 池")

    # 测试 2: 使用随机 UA 发送请求应返回 200
    r = requests.get(url, headers={"User-Agent": random.choice(ua_pool)})
    assert r.status_code == 200
    assert r.json()["user-agent"] in ua_pool
    print("测试 2 通过: 随机 UA 请求成功且返回匹配的 UA")

    # 测试 3: UA 池长度为 5
    assert len(ua_pool) == 5
    print("测试 3 通过: UA 池包含 5 个不同 UA")
