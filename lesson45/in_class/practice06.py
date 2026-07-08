"""
[难度: ⭐⭐⭐]
[所属知识点: BeautifulSoup + re 结合]
[预计完成时间: 15 分钟]

题目描述:
获取 quotes.toscrape.com 页面,用
find_all("span", text=re.compile("love"))
找到所有文本中包含 love 的名言,
打印匹配到的数量及每条名言的内容。
体会 re.compile 作为过滤器传入 find_all 的用法。

示例:
    >>> find_love_quotes()
    # 包含 love 的名言共 X 条:
    # 1. "..."
    # 2. "..."

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import re

import requests
from bs4 import BeautifulSoup


def find_love_quotes():
    """找到所有包含 love 的名言并打印"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数查看 love 名言
    print("=== 测试 1: 包含 love 的名言 ===")
    find_love_quotes()

    # 测试 2: 手动验证正则匹配逻辑
    print("\n=== 测试 2: 验证 re.compile 过滤 ===")
    url = "http://quotes.toscrape.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    matched = soup.find_all(
        "span", text=re.compile("love", re.IGNORECASE)
    )
    print(f"匹配数量: {len(matched)}")
    for i, tag in enumerate(matched, 1):
        print(f"  {i}. {tag.text[:40]}...")
