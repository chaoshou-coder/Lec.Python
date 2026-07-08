"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 综合-完整书籍信息爬取]
[预计完成时间: 20 分钟]

题目描述:
用 Playwright 打开 books.toscrape.com,
对页面执行 JS 滚动(scrollTo)确保所有书籍元素加载,
抓取当前页所有书籍的书名和价格,
打印前 5 本书的书名与价格。

示例:
    >>> main()
    第 1 本: A Light in the Attic —— £51.77
    第 2 本: Tipping the Velvet —— £53.74
    第 3 本: Soumission —— £50.10
    第 4 本: Sharp Objects —— £47.82
    第 5 本: Sapiens —— £54.23
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://books.toscrape.com")
        page.wait_for_load_state("networkidle")
        # 用 JS 滚动到底部触发懒加载
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)
        books = page.query_selector_all("article.product_pod")
        data = []
        for b in books:
            title = b.query_selector("h3 a")
            price = b.query_selector(".price_color")
            t = title.get_attribute("title") if title else ""
            pr = price.inner_text() if price else ""
            data.append((t, pr))
        for i, (name, price) in enumerate(data[:5], 1):
            print(f"第 {i} 本: {name} —— {price}")
        browser.close()
        return data


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 应抓取到 20 本书(首页数量)
    result = main()
    assert len(result) == 20, (
        f"期望 20 本,实际 {len(result)} 本"
    )

    # 测试 2: 前 5 本信息均应完整(书名 + 价格)
    for i, (name, price) in enumerate(result[:5]):
        assert name and price.startswith("£"), (
            f"第 {i+1} 本书信息不完整: {name}/{price}"
        )
    print("全部测试通过")
