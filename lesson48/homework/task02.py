"""
[难度: ⭐⭐⭐]
[所属知识点: 指数退避重试]
[预计完成时间: 15 分钟]

题目描述:
编写一个 polite_request(url, max_retries=3) 函数,
当遇到 HTTP 429(Too Many Requests)状态码时,
使用指数退避策略重试,等待时间依次为 1s、2s、4s。
请求成功(状态码 200)时返回 Response 对象,
全部重试失败时抛出自定义异常。

指数退避: 第 n 次重试等待 2^(n-1) 秒,
即第 1 次等 1s,第 2 次等 2s,第 3 次等 4s。
提示: 使用 time.sleep() 实现等待。

测试地址:
    - httpbin.org/status/200  → 立即返回 200
    - httpbin.org/status/429  → 返回 429,触发重试

示例:
    >>> resp = polite_request("https://httpbin.org/status/200")
    >>> resp.status_code
    200

    >>> polite_request("https://httpbin.org/status/429",
    ...                max_retries=2)
    # (等待 1s + 2s 后抛出异常)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 200 请求直接成功,无需重试
    # resp = polite_request("https://httpbin.org/status/200")
    # assert resp.status_code == 200

    # 测试 2: 429 请求在 max_retries=2 时抛异常,
    # 总等待时间约为 1s + 2s = 3s
    # try:
    #     polite_request("https://httpbin.org/status/429",
    #                    max_retries=2)
    #     assert False, "应抛出异常"
    # except Exception as e:
    #     assert "重试" in str(e) or "429" in str(e)

    pass
