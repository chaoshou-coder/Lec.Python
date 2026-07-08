"""
[难度: ⭐⭐]
[所属知识点: 响应内容与编码]
[预计完成时间: 10 分钟]

题目描述:
    访问 books.toscrape.com 首页,获取响应的 HTML 文本内容,
    打印前 200 个字符,并手动设置正确的编码(utf-8)以便
    中文或特殊字符正常显示。

示例:
    >>> resp = requests.get(url)
    >>> resp.encoding = 'utf-8'
    >>> print(resp.text[:200])
    <!DOCTYPE html>
    ...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = 'http://books.toscrape.com/'
response = requests.get(url)
# 设置编码,确保中文正常显示
response.encoding = 'utf-8'
# 打印前 200 个字符
print('前 200 个字符:')
print(response.text[:200])

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 内容长度应大于 0
    r = requests.get('http://books.toscrape.com/')
    r.encoding = 'utf-8'
    assert len(r.text) > 0, '响应内容不能为空'
    print('测试 1 通过:内容长度 =', len(r.text))

    # 测试 2: 前 200 字符中应包含 <html 标签
    head = r.text[:200].lower()
    assert '<html' in head or '<!doctype' in head, \
        '应包含 HTML 声明或标签'
    print('测试 2 通过:内容是合法 HTML')
