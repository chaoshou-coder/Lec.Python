"""
[难度: ⭐]
[所属知识点: Playwright 启动浏览器]
[预计完成时间: 5 分钟]

题目描述:
使用 Playwright 的 Chromium 无头浏览器打开
quotes.toscrape.com,获取页面 title 并打印,
完成后正确关闭浏览器资源。

示例:
    >>> main()
    页面标题: <title>Quotes to Scrape</title>
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
        title = page.title()
        print(f"页面标题: {title}")
        browser.close()
        return title


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证标题包含核心关键词
    result = main()
    assert "Scrape" in result or "Quotes" in result, (
        f"标题不符合预期: {result}"
    )

    # 测试 2: 单独启动一次确认能正常退出
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        pg.goto("https://quotes.toscrape.com")
        assert pg.title() is not None
        b.close()
    print("全部测试通过")
