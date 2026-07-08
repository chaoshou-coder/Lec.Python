"""
[难度: ⭐⭐]
[知识点: CSS 选择器 select]
[预计完成时间: 10 分钟]

题目描述:
用 select(".quote .text") 获取 quotes.toscrape.com
首页所有名言,用列表推导式提取每条的 text 内容,
打印名言总数和前 3 条名言。
体会 CSS 选择器与 find_all 的等价写法。

示例:
    >>> list_quotes()
    # 总数: 10
    # 第1条: "The world as we have created it..."
    # 第2条: "It is our choices, Harry..."
    # 第3条: "There are only two ways..."

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def list_quotes():
    """用 select 提取所有名言,打印总数和前 3 条"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看完整输出
    print("=== 测试 1: list_quotes() ===")
    list_quotes()

    # 测试 2: 手动验证 select 与 find_all 结果一致
    print("\n=== 测试 2: select vs find_all 对比 ===")
    url = "http://quotes.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    via_select = [tag.text for tag in soup.select(".quote .text")]
    via_find = [
        tag.text for tag in soup.find_all("span", class_="text")
    ]
    print(f"select 数量: {len(via_select)}")
    print(f"find_all 数量: {len(via_find)}")
    print(f"结果一致: {via_select == via_find}")
