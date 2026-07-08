"""
[难度: ⭐⭐]
[所属知识点: API 认证 Basic Auth]
[预计完成时间: 10 分钟]

题目描述:
访问 httpbin.org/basic-auth/user/passwd,
使用 requests 的 auth 参数进行 Basic Auth 认证,
打印响应状态码和 JSON 中的 authenticated 字段,
体会 HTTP Basic Authentication 的工作原理。

示例:
    >>> 正确认证 → 状态码 200, {"authenticated": true, "user": "user"}
    >>> 错误认证 → 状态码 0,   无响应内容
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/passwd"

# 使用 auth 参数进行 Basic Auth 认证
resp = requests.get(url, auth=HTTPBasicAuth("user", "passwd"))
print("状态码:", resp.status_code)
print("响应 JSON:", resp.json())
print("认证结果:", resp.json().get("authenticated"))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正确凭证应返回 200 和 authenticated=True
    r1 = requests.get(url, auth=HTTPBasicAuth("user", "passwd"))
    assert r1.status_code == 200
    assert r1.json()["authenticated"] is True
    assert r1.json()["user"] == "user"
    print("测试 1 通过: 正确凭证认证成功")

    # 测试 2: 错误凭证应返回 401
    r2 = requests.get(url, auth=HTTPBasicAuth("user", "wrong"))
    assert r2.status_code == 401
    print("测试 2 通过: 错误凭证返回 401")

    # 测试 3: 无认证访问也应返回 401
    r3 = requests.get(url)
    assert r3.status_code == 401
    print("测试 3 通过: 无认证返回 401")
