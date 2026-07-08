"""
[难度: ⭐⭐⭐]
[所属知识点: 指数退避重试]
[预计完成时间: 15 分钟]

题目描述:
访问 httpbin.org/status/500(模拟服务端错误),
实现指数退避重试策略:第 1 次等 1 秒,
第 2 次等 2 秒,第 3 次等 4 秒。
最多重试 3 次,打印每次重试的等待时间和最终状态。
体会指数退避如何在高频请求场景下避免雪崩。

示例:
    >>> 第 1 次请求状态码: 500, 等待 1 秒后重试
    >>> 第 2 次请求状态码: 500, 等待 2 秒后重试
    >>> 第 3 次请求状态码: 500, 等待 4 秒后重试
    >>> 重试次数耗尽,最终状态码: 500,总共耗时 7 秒
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import time
import requests

url = "https://httpbin.org/status/500"
max_retries = 3
base_wait = 1  # 基础等待时间(秒)

total_wait = 0

for attempt in range(1, max_retries + 1):
    resp = requests.get(url)
    print(f"第 {attempt} 次请求状态码: {resp.status_code}")
    if resp.status_code == 200:
        print("请求成功!")
        break
    # 计算指数退避等待时间: 1, 2, 4, ...
    wait_time = base_wait * (2 ** (attempt - 1))
    total_wait += wait_time
    print(f"  等待 {wait_time} 秒后重试...")
    time.sleep(wait_time)
else:
    print(f"重试次数耗尽,最终状态码: {resp.status_code},"
          f"总共等待: {total_wait} 秒")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 指数退避等待时间序列为 [1, 2, 4]
    waits = [1 * (2 ** (i - 1)) for i in range(1, 4)]
    assert waits == [1, 2, 4], f"等待序列应为 [1, 2 4], 实际 {waits}"
    print("测试 1 通过: 等待序列为 [1, 2, 4]")

    # 测试 2: 请求 /status/500 应返回 500
    r = requests.get("https://httpbin.org/status/500")
    assert r.status_code == 500
    print("测试 2 通过: /status/500 返回 500")

    # 测试 3: 请求 /status/200 应返回 200(成功场景)
    r2 = requests.get("https://httpbin.org/status/200")
    assert r2.status_code == 200
    print("测试 3 通过: /status/200 返回 200")
