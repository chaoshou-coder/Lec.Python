"""
[难度: ⭐⭐]
[所属知识点: 获取动态内容]
[预计完成时间: 10 分钟]

题目描述:
用 Playwright 打开 quotes.toscrape.com,
等待名言加载完成后,获取页面所有名言文本列表,
并打印名言条数。

示例:
    >>> main()
    共抓取到 10 条名言
    第一条: "The world as we have created it is..."
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        page.wait_for_load_state("networkidle")
        quotes = page.query_selector_all(".quote .text")
        texts = [q.inner_text() for q in quotes]
        print(f"共抓取到 {len(texts)} 条名言")
        if texts:
            print(f"第一条: {texts[0][:50]}...")
        browser.close()
        return texts


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 第一页应抓取到 10 条名言
    result = main()
    assert len(result) == 10, f"期望 10 条,实际 {len(result)} 条"

    # 测试 2: 每条名言应为非空字符串
    for i, t in enumerate(result):
        assert isinstance(t, str) and len(t) > 0, (
            f"第 {i+1} 条名言无效"
        )
    print("全部测试通过")
