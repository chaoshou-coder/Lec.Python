"""
[难度: ⭐⭐⭐]
[所属知识点: 页面快照与截图]
[预计完成时间: 15 分钟]

题目描述:
打开 books.toscrape.com,等待页面加载完成,
对当前页面截图保存为 books_screenshot.png,
打印截图文件的保存路径(绝对路径)。

示例:
    >>> main()
    截图已保存至: /Users/xxx/books_screenshot.png
    文件大小: 15234 bytes
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import os  # noqa: E402

from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    save_path = os.path.join(os.getcwd(), "books_screenshot.png")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://books.toscrape.com")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=save_path, full_page=True)
        print(f"截图已保存至: {save_path}")
        size = os.path.getsize(save_path)
        print(f"文件大小: {size} bytes")
        browser.close()
    return save_path


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 截图文件应存在于工作目录
    path = main()
    assert os.path.exists(path), (
        f"截图文件不存在: {path}"
    )

    # 测试 2: 文件大小应大于 10KB(正常渲染页面)
    file_size = os.path.getsize(path)
    assert file_size > 10000, (
        f"截图文件过小: {file_size} bytes"
    )
    print("全部测试通过")
