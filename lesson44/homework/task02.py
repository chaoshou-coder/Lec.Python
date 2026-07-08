"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 综合练习- headers + Session]
[预计完成时间: 20 分钟]

题目描述:
    模拟登录场景:使用 requests.Session() 创建会话,
    设置自定义 User-Agent,先访问登录页(用 httpbin),
    再访问主页(httpbin.org/get),从响应中验证
    User-Agent 是否被正确传递到每次请求中。

示例:
    >>> sess = requests.Session()
    >>> sess.headers.update({'User-Agent':'MySpider/1.0'})
    >>> r = sess.get('http://httpbin.org/get')
    >>> print(r.json()['headers']['User-Agent'])
    MySpider/1.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

# 创建 Session 并设置自定义 headers
session = requests.Session()
my_ua = 'MySpider/1.0 (Learning Crawler)'
session.headers.update({'User-Agent': my_ua})

# 第一次请求:访问一个页面
r1 = session.get('http://httpbin.org/get')
print('第 1 次请求 User-Agent:',
      r1.json()['headers']['User-Agent'])

# 第二次请求:再访问一次,验证 header 沿用
r2 = session.get('http://httpbin.org/get?page=2')
print('第 2 次请求 User-Agent:',
      r2.json()['headers']['User-Agent'])

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两次请求的 UA 都与设置的一致
    s = requests.Session()
    s.headers.update({'User-Agent': 'TestUA/2.0'})
    x1 = s.get('http://httpbin.org/get')
    x2 = s.get('http://httpbin.org/get?arg=1')
    ua1 = x1.json()['headers']['User-Agent']
    ua2 = x2.json()['headers']['User-Agent']
    assert ua1 == 'TestUA/2.0', f"第1次UA错误: {ua1}"
    assert ua2 == 'TestUA/2.0', f"第2次UA错误: {ua2}"
    print('测试 1 通过:两次 UA 都已正确传递')

    # 测试 2: Session 中自定义 header 覆盖默认值
    s2 = requests.Session()
    s2.headers.update({'User-Agent': 'Override/3.0'})
    r = s2.get('http://httpbin.org/get')
    assert 'Override/3.0' in r.text, \
        '响应正文中应包含自定义 UA'
    print('测试 2 通过:自定义 UA 覆盖成功')
