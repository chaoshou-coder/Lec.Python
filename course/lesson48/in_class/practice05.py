"""
[难度: ⭐⭐⭐]
[知识点: 限速与 time.sleep]
[预计完成时间: 15 分钟]

题目描述:
循环请求 httpbin.org/get 共 5 次,
每次请求之间间隔 2 秒(time.sleep),
每次打印请求序号和状态码,
演示礼貌爬虫(Crawler Etiquette)的基本做法,
避免高频率请求触发服务端限速(429)。

示例:
    >>> 请求 1/5 → 状态码 200
    >>> 等待 2 秒...
    >>> 请求 2/5 → 状态码 200
    >>> ...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import time
import requests

url = "https://httpbin.org/get"
total = 5
interval = 2

for i in range(1, total + 1):
    resp = requests.get(url)
    print(f"请求 {i}/{total} → 状态码: {resp.status_code}")
    # 最后一次请求后无需等待
    if i < total:
        print(f"  等待 {interval} 秒...")
        time.sleep(interval)

print("全部请求完成")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 单次请求 httpbin.org/get 应返回 200
    r = requests.get(url)
    assert r.status_code == 200
    print("测试 1 通过: 单次请求返回 200")

    # 测试 2: 循环 2 次(带间隔)应全部成功
    success_count = 0
    for i in range(2):
        r = requests.get(url)
        if r.status_code == 200:
            success_count += 1
        if i < 1:
            time.sleep(1)
    assert success_count == 2
    print("测试 2 通过: 2 次间隔请求全部成功")
