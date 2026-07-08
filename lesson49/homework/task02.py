"""
[难度: ⭐⭐⭐]
[所属知识点: asyncio + aiohttp 并发爬取多页]
[预计完成时间: 15 分钟]

题目描述:
    用 asyncio + aiohttp 并发爬取 books.toscrape.com
    第 1~5 页,每页解析书名(BeautifulSoup 的 h3>a 选择器),
    把所有页的结果合并到一个列表 titles 中,
    最后打印 "共抓取 N 个书名"。(期望约 100 个)

    要求:
      - async def fetch(session, url) 发送请求
      - asyncio.gather 并发 5 个任务
      - 解析用 soup.select("h3 > a") 取 @title

示例:
    >>> 运行后终端输出:
    共抓取 100 个书名
    前 5 个: ['A Light in the Attic', ...]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 import 导入所需模块
    try:
        import asyncio
        import aiohttp
        from bs4 import BeautifulSoup
        print("模块导入成功: asyncio, aiohttp, "
              "BeautifulSoup")
    except ImportError as e:
        print(f"导入失败: {e}")

    # 测试 2: 用本地 HTML 模拟并发解析逻辑
    print("--- 测试 2:模拟解析逻辑 ---")
    sample_html = (
        '<html><body>'
        '<article class="product_pod">'
        '<h3><a href="x" title="Book A">name</a></h3>'
        '</article>'
        '<article class="product_pod">'
        '<h3><a href="y" title="Book B">name</a></3>'
        '</article>'
        '</body></html>'
    )
    # 上面故意写一个 </h3> 模拟书写错误,
    # 学员的 select 应仍能容错提取
    soup = BeautifulSoup(sample_html, "html.parser")
    books = soup.select("h3 > a")
    titles = [b["title"] for b in books if b.get("title")]
    print(f"提取到 {len(titles)} 个书名: {titles}")
    assert len(titles) >= 1, "应至少提取到 1 个书名"
    print("测试 2 通过")
