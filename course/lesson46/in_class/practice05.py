"""
[难度: ⭐⭐⭐]
[所属知识点: 表单交互]
[预计完成时间: 15 分钟]

题目描述:
打开 quotes.toscrape.com/login 页面,
填写用户名 "admin" 和密码 "admin",
点击登录按钮,等待跳转后打印登录成功页面标题。
(该网站登录不会真校验,提交后进入新页面)

示例:
    >>> main()
    登录后页面标题: <title>Quotes to Scrape</title>
    URL 含 token 参数: True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/login")
        page.wait_for_selector("#username")
        page.fill("#username", "admin")
        page.fill("#password", "admin")
        page.click("input[type='submit']")
        page.wait_for_load_state("networkidle")
        title = page.title()
        url = page.url
        print(f"登录后页面标题: {title}")
        print(f"URL 含 token: {'token' in url}")
        browser.close()
        return title, url


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 登录后页面标题应非空
    title, url = main()
    assert isinstance(title, str) and len(title) > 0, (
        "标题为空,登录可能失败"
    )

    # 测试 2: 登录后 URL 应包含 csrf token 参数
    assert "token" in url.lower(), (
        f"URL 中未发现 token 参数: {url}"
    )
    print("全部测试通过")
