"""
[难度: ⭐]
[所属知识点: requests GET 请求]
[预计完成时间: 5 分钟]

题目描述:
    欢迎来到爬虫世界的第一步!使用 requests.get() 向
    http://books.toscrape.com/ 发送一个 GET 请求,
    并打印响应的状态码(200 表示成功)。

示例:
    >>> resp = requests.get('http://books.toscrape.com/')
    >>> print(resp.status码)
    200
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

# 提示:用 requests.get(url) 发送请求,用 .status_code 获取状态码
url = 'http://books.toscrape.com/'
response = requests.get(url)
print('状态码:', response.status_code)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 首页请求成功,状态码为 200
    r1 = requests.get('http://books.toscrape.com/')
    assert r1.status_code == 200, f"期望 200, 实际 {r1.status_code}"
    print('测试 1 通过:首页状态码 =', r1.status_code)

    # 测试 2: 另一个分类页请求成功
    r2 = requests.get(
        'http://books.toscrape.com/catalogue/category/'
        'books_1/index.html'
    )
    assert r2.status_code == 200, f"期望 200, 实际 {r2.status_code}"
    print('测试 2 通过:分类页状态码 =', r2.status_code)
