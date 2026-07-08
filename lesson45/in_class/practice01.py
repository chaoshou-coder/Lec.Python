"""
[难度: ⭐]
[所属知识点: BeautifulSoup 基本解析]
[预计完成时间: 5 分钟]

题目描述:
用 requests 获取 quotes.toscrape.com 首页,
用 BeautifulSoup 解析并打印页面 <title> 标签的文本。
这是学习网页解析的第一步:请求页面 → 解析 → 提取标题。

示例:
    >>> get_title()  # 输出: ```
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests
from bs4 import BeautifulSoup


def get_title():
    """获取并打印 quotes.toscrape.com 首页的 title 文本"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查函数能正常执行并打印内容
    print("=== 测试 1: 调用 get_title() ===")
    get_title()

    # 测试 2: 验证 requests + BeautifulSoup 解析流程正确
    print("\n=== 测试 2: 手动验证 title 标签 ===")
    resp = requests.get("http://quotes.toscrape.com/")
    soup = BeautifulSoup(resp.text, "html.parser")
    print("title.text =", soup.title.text.strip())
    print("title.name =", soup.title.name)
