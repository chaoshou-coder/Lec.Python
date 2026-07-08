"""
[难度: ⭐⭐⭐]
[所属知识点: 状态码判断与异常处理]
[预计完成时间: 15 分钟]

题目描述:
    编写一个函数 check_url(url),访问指定的 URL,
    用 if 判断状态码:若为 200 则打印"请求成功";
    否则打印"请求失败:状态码"。分别对一个存在的页面
    和一个不存在的页面进行调用验证。

示例:
    >>> check_url('http://books.toscrape.com/')
    请求成功
    >>> check_url('http://books.toscrape.com/notexist.html')
    请求失败:404
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

def check_url(url):
    """访问 url,根据状态码判断请求是否成功"""
    # 提示:设置 headers 以免被拦截
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36'
        )
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        print('请求成功')
    else:
        print(f'请求失败:{resp.status_code}')

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 存在的页面应成功
    print('--- 测试 1:存在的页面 ---')
    check_url('http://books.toscrape.com/')

    # 测试 2: 不存在的页面应失败(404)
    print('--- 测试 2:不存在的页面 ---')
    check_url(
        'http://books.toscrape.com/catalogue/'
        'this_page_does_not_exist.html'
    )
