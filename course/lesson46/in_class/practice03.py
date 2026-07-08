"""
[难度: ⭐⭐]
[知识点: 等待策略 wait_for_selector]
[预计完成时间: 10 分钟]

题目描述:
打开 quotes.toscrape.com,使用 wait_for_selector(".quote")
等待名言元素出现,然后获取第一条名言文本并返回。
体会显式等待相比 time.sleep 的优势。

示例:
    >>> main()
    第一条名言: "The world as we have created it
    is a process of our thinking..."
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
        page.wait_for_selector(".quote", timeout=10000)
        first = page.query_selector(".quote .text")
        text = first.inner_text() if first else ""
        print(f"第一条名言: {text}")
        browser.close()
        return text


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 返回的第一条名言应为非空字符串
    result = main()
    assert isinstance(result, str) and len(result) > 0, (
        "名言文本为空"
    )

    # 测试 2: 第一条名言应包含已知关键词
    assert "world" in result.lower(), (
        f"第一条名言内容不符合预期: {result[:60]}"
    )
    print("全部测试通过")
