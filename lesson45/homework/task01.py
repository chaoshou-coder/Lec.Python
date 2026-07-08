"""
[难度: ⭐⭐⭐]
[所属知识点: 多条件查找]
[预计完成时间: 15 分钟]

题目描述:
获取 quotes.toscrape.com 首页第一条名言区块,
同时查找作者与标签信息,打印:
- 名言文本
- 作者名( small class="author" )
- 所有标签( div class="tags" 下的 a 标签,逗号分隔)
练习在同一区块内多维度提取不同字段。

示例:
    >>> print_first_quote_detail()
    # 名言: "The world as we have created it..."
    # 作者: Albert Einstein
    # 标签: change,deep-thoughts,thinking,world

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def print_first_quote_detail():
    """打印第一条名言的文本、作者和标签"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看第一条详情
    print("=== 测试 1: 第一条名言详情 ===")
    print_first_quote_detail()

    # 测试 2: 手动验证 quote 区块内部结构
    print("\n=== 测试 2: 验证区块结构 ===")
    url = "http://quotes.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    quote = soup.find("div", class_="quote")
    print(f"作者: {quote.find('small', class_='author').text}")
    tags = [a.text for a in quote.find_all("a", class_="tag")]
    print(f"标签数: {len(tags)}")
    print(f"标签: {', '.join(tags)}")
