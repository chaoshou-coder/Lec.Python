"""
[难度: ⭐⭐⭐]
[所属知识点: Session 会话保持]
[预计完成时间: 15 分钟]

题目描述:
    使用 requests.Session() 创建一个会话对象,连续访问
    books.toscrape.com 首页和一个分类页,打印每次请求的
    状态码,验证 Session 在多次请求之间复用连接、共享
    headers 的特性。

示例:
    >>> sess = requests.Session()
    >>> r1 = sess.get('http://books.toscrape.com/')
    >>> r2 = sess.get('http://books.toscrape.com/.../page-2.html')
    >>> print(r1.status_code, r2.status_code)
    200 200
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

# 创建 Session 对象
session = requests.Session()
# 设置通用的 User-Agent,后续请求都会带上
session.headers.update({
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
})

# 第一次请求:首页
r1 = session.get('http://books.toscrape.com/')
print('首页 状态码:', r1.status_code)

# 第二次请求:分类页
r2 = session.get(
    'http://books.toscrape.com/catalogue/category/'
    'books_1/index.html'
)
print('分类页 状态码:', r2.status_code)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: Session 两次请求都成功
    s = requests.Session()
    a = s.get('http://books.toscrape.com/')
    b = s.get(
        'http://books.toscrape.com/catalogue/category/'
        'books_1/index.html'
    )
    assert a.status_code == 200, f"首页失败: {a.status_code}"
    assert b.status_code == 200, f"分类页失败: {b.status_code}"
    print('测试 1 通过:两次状态码 =', a.status_code, b.status_code)

    # 测试 2: Session 设置的 headers 会被携带
    s2 = requests.Session()
    s2.headers.update({'User-Agent': 'MyBot/1.0'})
    r = s2.get('http://books.toscrape.com/')
    sent = r.request.headers.get('User-Agent', '')
    assert sent == 'MyBot/1.0', \
        f"UA 应为 MyBot/1.0, 实际: {sent}"
    print('测试 2 通过:Session UA 已携带 =', sent)
