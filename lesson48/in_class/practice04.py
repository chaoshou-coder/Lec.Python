"""
[难度: ⭐⭐]
[所属知识点: API Token 认证]
[预计完成时间: 10 分钟]

题目描述:
访问 httpbin.org/bearer,在请求头中添加
Authorization: Bearer <token>,其中 token 值为
"my_secret_token_123",打印状态码和响应内容,
体会 Bearer Token 认证的工作方式。

示例:
    >>> 正确 Token → 状态码 200, {"authenticated": true,
                         "token": "my_secret_token_123"}
    >>> 错误 Token → 状态码 401, 无响应内容
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = "https://httpbin.org/bearer"
token = "my_secret_token_123"

# 在 headers 中添加 Authorization: Bearer <token>
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get(url, headers=headers)
print("状态码:", resp.status_code)
print("响应内容:", resp.json())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正确 Token 应返回 200 和 authenticated=True
    h1 = {"Authorization": "Bearer my_secret_token_123"}
    r1 = requests.get(url, headers=h1)
    assert r1.status_code == 200
    assert r1.json()["authenticated"] is True
    assert r1.json()["token"] == "my_secret_token_123"
    print("测试 1 通过: 正确 Token 认证成功")

    # 测试 2: 错误 Token 应返回 401
    h2 = {"Authorization": "Bearer wrong_token"}
    r2 = requests.get(url, headers=h2)
    assert r2.status_code == 401
    print("测试 2 通过: 错误 Token 返回 401")

    # 测试 3: 无 Token 请求应返回 401
    r3 = requests.get(url)
    assert r3.status_code == 401
    print("测试 3 通过: 无 Token 返回 401")
