"""
[难度: ⭐⭐]
[所属知识点: find 与 find_all]
[预计完成时间: 10 分钟]

题目描述:
获取 quotes.toscrape.com 首页,用 find_all 找到所有
class="text" 的 span 标签(即名言内容),
打印第一条和最后一条名言的文本。
体会 find_all 返回列表,可用索引访问。

示例:
    >>> print_first_last_quote()
    # 第一条: "The world as we have created it..."
    # 最后一条: "..."

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def print_first_last_quote():
    """打印首页第一条和最后一条名言"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看输出
    print("=== 测试 1: 打印首末名言 ===")
    print_first_last_quote()

    # 测试 2: 手动验证 find_all 返回数量与索引
    print("\n=== 测试 2: 验证 find_all 结果 ===")
    url = "http://quotes.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    print(f"名言总数: {len(quotes)}")
    print(f"第一条类型: {type(quotes[0]).__name__}")
    print(f"第一条文本: {quotes[0].text[:30]}...")
    print(f"最后一条文本: {quotes[-1].text[:30]}...")
