"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 综合练习- params + 数据处理]
[预计完成时间: 20 分钟]

题目描述:
    爬取 books.toscrape.com 的前 3 页
    (page-1.html, page-2.html, page-3.html),
    从每个页面的 HTML 中提取 <title> 标签内容,
    打印页码与对应的标题。
    提示:title 位于 <title>...</title> 之间。

示例:
    >>> # page-1
    页码:1,  title: Books to Scrape
    >>> # page-2
    页码:2,  title: Books to Scrape
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

base = 'http://books.toscrape.com/catalogue/page-{}.html'
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/537.36'
    )
}

for page in range(1, 4):
    url = base.format(page)
    resp = requests.get(url, headers=headers)
    html = resp.text
    # 提取 <title> 标签内容
    start = html.find('<title>') + len('<title>')
    end = html.find('</title>')
    title = html[start:end].strip()
    print(f'页码:{page},  title: {title}')

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 3 个页面都应成功提取 title
    h = {'User-Agent': 'Mozilla/5.0 (TestBot)'}
    titles = []
    for p in range(1, 4):
        url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(p)
        r = requests.get(url, headers=h)
        assert r.status_code == 200, f"{url} 失败"
        s = r.text.find('<title>') + len('<title>')
        e = r.text.find('</title>')
        t = r.text[s:e].strip()
        titles.append(t)
        print(f'  页码 {p} -> title: {t}')
    assert len(titles) == 3, '应提取到 3 个 title'
    print('测试 1 通过:3 个页面都提取到 title')

    # 测试 2: title 字段非空
    for i, t in enumerate(titles, start=1):
        assert len(t) > 0, f"页码 {i} 的 title 为空"
    print('测试 2 通过:所有 title 均非空')
