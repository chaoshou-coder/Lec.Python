"""
[难度: ⭐⭐⭐]
[所属知识点: 多页爬取]
[预计完成时间: 15 分钟]

题目描述:
用 Playwright 翻页爬取 quotes.toscrape.com 前 3 页,
每页收集所有名言到一个列表,
最后打印总条数以及第 3 页第一条名言。

示例:
    >>> main()
    前 3 页共抓取 30 条名言
    第 3 页第一条: "It is not a lack of love,
    but a lack of friendship..."
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from playwright.sync_api import sync_playwright  # noqa: E402


def scrape_quotes(page, max_pages=3):
    all_texts = []
    for _ in range(max_pages):
        page.wait_for_selector(".quote")
        quotes = page.query_selector_all(".quote .text")
        for q in quotes:
            all_texts.append(q.inner_text())
        next_btn = page.query_selector("li.next a")
        if next_btn:
            next_btn.click()
        else:
            break
    return all_texts


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        result = scrape_quotes(page, max_pages=3)
        print(f"前 3 页共抓取 {len(result)} 条名言")
        if len(result) >= 21:
            print(f"第 3 页第一条: {result[20][:60]}...")
        browser.close()
        return result


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 前 3 页应共抓取 30 条名言
    result = main()
    assert len(result) == 30, (
        f"期望 30 条,实际 {len(result)} 条"
    )

    # 测试 2: 全部名言应互不相同(无明显重复)
    unique = set(result)
    assert len(unique) == len(result), (
        f"存在重复名言: {len(result) - len(unique)} 条"
    )
    print("全部测试通过")
