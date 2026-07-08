"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 综合解析 - 书籍信息提取]
[预计完成时间: 20 分钟]

题目描述:
获取 books.toscrape.com 首页所有书籍信息,
每本书提取:
- 书名( h3 > a 的 title 属性 )
- 价格( p.price_color 的文本 )
- 星级( p.star-rating 的第二个 class 名,如 "Three" )
每本书打印一行,练习对真实列表页做综合字段抽取。

示例:
    >>> scrape_books()
    # A Light in the Attic | £51.77 | Three
    # Tipping the Velvet | £53.74 | One
    # ...

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def scrape_books():
    """提取并打印首页所有书籍的书名、价格、星级"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看所有书籍
    print("=== 测试 1: 首页书籍列表 ===")
    scrape_books()

    # 测试 2: 手动验证单本书结构
    print("\n=== 测试 2: 验证单本书字段 ===")
    url = "http://books.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    book = soup.find("article", class_="product_pod")
    title = book.h3.a.get("title")
    price = book.find("p", class_="price_color").text
    star = book.find("p", class_="star-rating").get("class")[1]
    print(f"书名: {title}")
    print(f"价格: {price}")
    print(f"星级: {star}")
