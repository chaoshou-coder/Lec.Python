"""
[难度: ⭐]
[所属知识点: 发送带 User-Agent 的请求]
[预计完成时间: 5 分钟]

题目描述:
访问 httpbin.org/user-agent,先不带 User-Agent 发送请求,
打印返回结果;再带上自定义 User-Agent
("MyCrawler/1.0")发送请求,打印结果并对比差异。
体会网站如何通过 User-Agent 识别爬虫。

示例:
    >>> 不带 UA 请求 → {"user-agent": "python-requests/2.x.x"}
    >>> 带 UA 请求   → {"user-agent": "MyCrawler/1.0"}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = "https://httpbin.org/user-agent"

# 1. 不带自定义 User-Agent 发送请求
resp_default = requests.get(url)
print("默认 User-Agent:", resp_default.json())

# 2. 带自定义 User-Agent 发送请求
headers = {"User-Agent": "MyCrawler/1.0"}
resp_custom = requests.get(url, headers=headers)
print("自定义 User-Agent:", resp_custom.json())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认请求应返回 requests 库的 UA
    r1 = requests.get(url)
    assert r1.status_code == 200
    assert "python-requests" in r1.json()["user-agent"]
    print("测试 1 通过: 默认 UA 包含 python-requests")

    # 测试 2: 自定义 UA 应返回 MyCrawler/1.0
    r2 = requests.get(url, headers={"User-Agent": "MyCrawler/1.0"})
    assert r2.json()["user-agent"] == "MyCrawler/1.0"
    print("测试 2 通过: 自定义 UA 返回 MyCrawler/1.0")
