"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 动态加载全部数据]
[预计完成时间: 20 分钟]

题目描述:
用 Playwright 连续翻页直到没有 "Next" 按钮
(quotes.toscrape.com 共 10 页),
收集所有名言到一个列表,打印总数和最后一条。

示例:
    >>> main()
    全部 10 页共抓取 100 条名言
    最后一条名言: "The world as we have created..."
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from playwright.sync_api import sync_playwright  # noqa: E402


def scrape_all_quotes(page):
    all_texts = []
    page_num = 0
    while True:
        page_num += 1
        page.wait_for_selector(".quote")
        quotes = page.query_selector_all(".quote .text")
        for q in quotes:
            all_texts.append(q.inner_text())
        print(f"第 {page_num  } 页抓取 {len(quotes)} 条")
        next_btn = page.query_selector("li.next a")
        if not next_btn:
            break
        next_btn.click()
    return all_texts


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        result = scrape_all_quotes(page)
        print(f"全部共抓取 {len(result)} 条名言")
        if result:
            print(f"最后一条名言: {result[-1][:60]}...")
        browser.close()
        return result


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 全部 10 页应共 100 条名言
    result = main()
    assert len(result) == 100, (
        f"期望 100 条,实际 {len(result)} 条"
    )

    # 测试 2: 最后一条名言应为非空字符串
    last = result[-1]
    assert isinstance(last, str) and len(last) > 0, (
        "最后一条名言内容无效"
    )
    print("全部测试通过")
