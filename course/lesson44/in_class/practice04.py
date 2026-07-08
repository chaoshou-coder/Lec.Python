"""
[难度: ⭐⭐]
[知识点: URL 参数 params]
[预计完成时间: 10 分钟]

题目描述:
    使用 requests 的 params 参数请求
    http://books.toscrape.com/catalogue/page-2.html,
    让 requests 自动拼接参数。打印最终请求的完整 URL,
    验证参数是否被正确编码。

示例:
    >>> params = {'page': 2}
    >>> resp = requests.get(url, params=params)
    >>> print(resp.url)
    http://books.toscrape.com/...?page=2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = 'http://books.toscrape.com/catalogue/page-1.html'
# 定义 URL 参数
params = {'page': '2', 'sort': 'price'}
response = requests.get(url, params=params)
print('最终请求的完整 URL:')
print(response.url)
print('状态码:', response.status_code)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: params 被拼接到 URL 中
    p = {'page': '2'}
    r = requests.get(
        'http://books.toscrape.com/catalogue/page-1.html',
        params=p
    )
    assert 'page=2' in r.url, \
        f"URL 中应包含 page=2, 实际: {r.url}"
    print('测试 1 通过:URL =', r.url)

    # 测试 2: 多参数场景
    p2 = {'page': '3', 'sort': 'title'}
    r2 = requests.get(
        'http://books.toscrape.com/catalogue/page-1.html',
        params=p2
    )
    assert 'page=3' in r2.url and 'sort=title' in r2.url, \
        f"URL 应包含 page=3 与 sort=title, 实际: {r2.url}"
    print('测试 2 通过:URL =', r2.url)
