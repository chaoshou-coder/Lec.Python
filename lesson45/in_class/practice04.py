"""
[难度: ⭐⭐]
[所属知识点: 获取元素属性]
[预计完成时间: 10 分钟]

题目描述:
获取 books.toscrape.com 首页,找到第一个 <article> 标签,
打印其内部 h3 > a 的文本(书名)和 href 属性(链接)。
学会通过标签嵌套定位元素,并用 .get("href") 取属性。

示例:
    >>> print_first_book_info()
    # 书名: A Light in the Attic
    # 链接: catalog/a-light-in-the-attic_1000/index.html

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def print_first_book_info():
    """打印首页第一本书的书名和链接"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看输出
    print("=== 测试 1: 第一本书信息 ===")
    print_first_book_info()

    # 测试 2: 手动验证 article > h3 > a 结构
    print("\n=== 测试 2: 验证 article 结构 ===")
    url = "http://books.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    article = soup.find("article")
    h3_a = article.h3.a
    print(f"h3>a 文本: {h3_a.text.strip()}")
    print(f"h3>a href : {h3_a.get('href')}")
    print(f"h3>a title: {h3_a.get('title')}")
