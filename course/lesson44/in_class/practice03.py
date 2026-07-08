"""
[难度: ⭐⭐]
[所属知识点: 请求头 headers]
[预计完成时间: 10 分钟]

题目描述:
    很多网站会拦截"裸"请求(没有 User-Agent 的请求),
    返回 403 或空内容。自定义一个 User-Agent headers,
    访问 http://books.toscrape.com/ 并打印所使用的
    User-Agent 以及最终状态码。(牢记:爬虫不带 headers 容易被屏蔽!)

示例:
    >>> headers = {'User-Agent': 'Mozilla/5.0 ...'}
    >>> resp = requests.get(url, headers=headers)
    >>> print(headers['User-Agent'])
    Mozilla/5.0 ...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = 'http://books.toscrape.com/'
# 自定义请求头,伪装成浏览器访问
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}
response = requests.get(url, headers=headers)
print('使用的 User-Agent:', headers['User-Agent'])
print('状态码:', response.status_code)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 带 headers 应能成功请求
    h = {
        'User-Agent': 'Mozilla/5.0 (TestBot/1.0)'
    }
    r = requests.get(
        'http://books.toscrape.com/', headers=h
    )
    assert r.status_code == 200, f"期望 200, 实际 {r.status_code}"
    print('测试 1 通过:带 headers 状态码 =', r.status_code)

    # 测试 2: headers 确实被发送(r.request.headers 包含)
    sent_ua = r.request.headers.get('User-Agent', '')
    assert sent_ua == 'Mozilla/5.0 (TestBot/1.0)', \
        'User-Agent 未正确发送'
    print('测试 2 通过:User-Agent 已发送 =', sent_ua)
