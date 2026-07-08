"""
[难度: ⭐⭐]
[所属知识点: 页面导航与点击]
[预计完成时间: 10 分钟]

题目描述:
打开 quotes.toscrape.com,点击 "Next →" 按钮翻到第 2 页,
等待新页面名言加载后,获取并打印第 2 页的第一条名言。

示例:
    >>> main()
    第2页第一条名言: "It is our choices, Harry, that
    show what we truly are..."
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
        page.wait_for_selector(".quote")
        next_btn = page.query_selector("li.next a")
        if next_btn:
            next_btn.click()
            page.wait_for_selector(".quote")
        first = page.query_selector(".quote .text")
        text = first.inner_text() if first else ""
        print(f"第2页第一条名言: {text}")
        browser.close()
        return text


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 翻页后第一条名言应非空
    result = main()
    assert isinstance(result, str) and len(result) > 0, (
        "未获取到第 2 页名言"
    )

    # 测试 2: 第 2 页第一条名言应不同于第 1 页
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        pg.goto("https://quotes.toscrape.com")
        pg.wait_for_selector(".quote")
        first_pg1 = pg.query_selector(".quote .text").inner_text()
        b.close()
    assert result != first_pg1, (
        "第 2 页名言与第 1 页相同,翻页可能失败"
    )
    print("全部测试通过")
