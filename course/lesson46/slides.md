# Day46 · 动态页面(Selenium/Playwright)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day45 已掌握静态页面解析(requests + BeautifulSoup)
> 关键问题:静态解析拿不到 JS 渲染后的内容。
> 本节用 Playwright 驱动真实浏览器,学会等待策略,
> 从"看源代码"升级为"看用户看到的"。

---

## 0. 引入(5 分钟)

- **演示对比**(3 分钟): 同一商品页面,requests 拿到空白容器;
  Playwright 拿到完整价格 —— 引出"动态渲染"概念。
- **口答**(2 分钟): "JS 什么时候执行?"
  "requests 能不能执行 JS?" 验证前置认知。

---

## 1. 第一讲(25 分钟) —— 为什么需要动态渲染

### 知识点 1.1 静态 vs 动态:三句话

1. SSR: HTML 里直接有数据,`requests` 够用。
2. CSR / SPA: 浏览器执行 JS 后才填入数据,`requests` 只能拿到空壳。
3. 混 SSR + CSR: 初始有骨架,滚动/点击时异步加载更多内容。

```python
# 反例: 这段代码拿不到 SPA 里的真实价格
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://quotes.toscrape.com/js/")
soup = BeautifulSoup(resp.text, "html.parser")
print(soup.select(".quote"))   # [] —— 内容由 JS 生成
```

> 🔴 教学红线: 动态页面用 requests 拿到空内容。
> **HTML 没目标数据先怀疑 JS 渲染**,别先怪解析代码。

### 知识点 1.2 现代工具选型:Playwright vs Selenium

| 维度 | Selenium | Playwright |
|---|---|---|
| 出品 | 2004 年 | 2020 年,Microsoft |
| 自动等 | 需手写 WebDriverWait | 内置 auto-wait |
| 多浏览器 | 需各浏览器驱动 | 一行 `playwright install` |
| 推荐场景 | 老项目维护 | 新项目首选 |

```bash
pip install playwright
playwright install   # 下载 Chromium / Firefox / WebKit
```

> 口诀:**新坑 Playwright,旧坑 Selenium;auto-wait 是真香**。

### 知识点 1.3 最小可用脚本

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # headless=True 不在屏幕上弹浏览器窗口
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")
    html = page.content()      # 直接取渲染后的 HTML
    print(len(html))           # > 0,已有 quote 内容
    browser.close()
```

> 🔴 教学红线: headless 模式**必须设置** ——
> 否则每次执行弹窗口,资源浪费且容易被反爬识别。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 用 Playwright 打开
  `quotes.toscrape.com/js/`,抓 `.quote .text` 打印前 5 条 (⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 对比同一个 URL,
  分别用 requests 和 Playwright 抓取,输出两者 HTML 长度差 (⭐⭐,15 分钟)

> 巡场重点: 学员常忘装 `playwright install` 就运行,
> 报 `Executable doesn't exist` —— 课前一次强调。

---

## 3. 第二讲(30 分钟) —— 等待策略:隐式、显式、等待元素

### 知识点 3.1 隐式等待

最笨方法: 强制等 N 毫秒,**不要用**,仅调试时用。

```python
page.wait_for_timeout(3000)    # 硬等 3 秒,不推荐写进正式脚本
```

### 知识点 3.2 显式等待 `wait_for_selector`

核心 API: 等到**某个选择器**出现(或消失、或可见)才继续。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")
    # 等待至少一个 .quote 出现,超时 10 秒报错
    page.wait_for_selector(".quote", timeout=10000)
    quotes = page.query_selector_all(".quote")
    print(f"抓到 {len(quotes)} 条名言")
    browser.close()
```

> 🔴 教学红线: **没等元素加载就抓取 = 拿到空内容**。
> 新人 80% 的"抓不到数据"原因在这里。

### 知识点 3.3 等待状态枚举

| API | 等的是 | 典型场景 |
|---|---|---|
| `wait_for_selector(s)` | 选择器在 DOM 中出现 | 初始渲染 |
| `wait_for_selector(s, state="visible")` | 元素可见 | lazy-load |
| `wait_for_selector(s, state="hidden")` | 元素消失 | loading 动画 |
| `wait_for_load_state("networkidle")` | 网络空闲 | AJAX 完成 |

> 口诀:**goto → wait → query,三步缺一步都是空**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 打开有 loading 的页面,
  用 `wait_for_selector(state="hidden")` 等 loading 消失后抓 (⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 故意**不写** wait 直接 goto 后抓,
  再补上 wait 对比 (⭐⭐,10 分钟)

> 巡场重点: 练习 4 是"犯一次错再修"训练,学员常见心态"代码能跑就行"
> —— 强调"能拿到空 list 也是'能跑',但产出是垃圾"。

---

## 5. 第三讲(30 分钟) —— 实战:SPA / 无限滚动

### 知识点 5.1 SPA 单页应用:点"下一页"抓完整数据

SPA 翻页时地址栏 URL 不变,只是 JS 局部刷新。
要点:每次翻页后**重新等待元素出现**,再抓再翻页。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://spa-scraping-practice.example.com")

    all_items = []
    for _ in range(5):                # 翻 5 页
        # 等本页数据渲染完
        page.wait_for_selector(".item")

        # 抓当前页所有条目
        items = page.query_selector_all(".item")
        for item in items:
            title = item.query_selector(".title").inner_text()
            all_items.append(title)

        # 点"下一页"按钮
        next_btn = page.query_selector("button.next")
        if next_btn:
            next_btn.click()
            # 等旧内容消失再出现新内容,避免抓到过渡态 DOM
            page.wait_for_load_state("networkidle")

    print(f"共抓 {len(all_items)} 条")
    browser.close()
```

> 口诀:**翻页三步: 抓当前 → 点下一页 → 等加载**。

### 知识点 5.2 无限滚动页面:模拟滚动 + 等新增

无限滚动页面在 `scroll` 事件后自动追加新内容。
关键:滚动后等 DOM 节点数**真的增加**了才继续。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://infinite-scroll.example.com")

    last_count = 0
    for _ in range(5):                # 滚 5 次
        # 滚到底
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        # 等新增内容出现(用轮询检查 DOM 节点数)
        page.wait_for_timeout(1500)

        # 统计当前条目数
        cur = page.locator(".card").count()
        if cur == last_count:           # 没有新增 → 到底了
            print("已到页面底部,终止")
            break
        last_count = cur
        print(f"当前抓到 {cur} 条")

    browser.close()
```

> 🔴 教学红线: 无限滚动**不要写死循环** ——
> 必须设终止条件(条数不再增加 / 已翻 N 页),否则脚本跑飞。

### 知识点 5.3 query_selector 要点补充

`query_selector_all` 返回 `ElementHandle` 列表,常用方法:

```python
el.query_selector(".title").inner_text()   # 文本
el.get_attribute("href")                   # 属性
el.click()                                 # 点击
el.fill("hello")                           # 输入框填写
```

> 口诀:`inner_text` 拿文字,`get_attribute` 拿链接,`click / fill` 做交互。

## 6. 当堂练 3(30 分钟)

- 练习 5: `in_class/practice05.py` —— 打开 `quotes.toscrape.com/js/`,
  抓**全部**名言(点"Next"翻页直到消失) (⭐⭐⭐⭐,20 分钟)
- 练习 6: `in_class/practice06.py` —— 模拟登录:填写用户名/密码,
  点提交,抓跳转后标题验证登录成功 (⭐⭐⭐,10 分钟)

> 巡场重点: 练习 5 翻到最后一页仍点"Next"会抛 `Element not found`
> —— 先 `if not next_btn: break` 保护。

---

## 7. 第四讲(20 分钟) —— 进阶技巧

### 知识点 7.1 拦截网络请求

有时数据根本不在 DOM 里,而是通过 XHR / Fetch 返回的 JSON。
直接**拦截 API 响应**比解析 DOM 更稳。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    api_data = []

    # 拦截所有响应回调
    def on_response(response):
        if "api/items" in response.url:
            api_data.append(response.json())

    page.on("response", on_response)
    page.goto("https://spa-scraping-practice.example.com")
    page.wait_for_load_state("networkidle")

    print(f"拦截到 {len(api_data)} 个 API 响应")
    browser.close()
```

> 直觉:**拦截 API = 从'翻菜单'变成'进后厨直接拿食材'**,
> 结构更干净,速度更快。

### 知识点 7.2 截图与 PDF

```python
# 全页截图
page.screenshot(path="screenshot.png", full_page=True)

# 转 PDF(仅 Chromium 支持)
page.pdf(path="page.pdf", format="A4")
```

> 口诀:截图用 `screenshot`,PDF 用 `pdf`,**只 Chromium 支持 PDF**。

## 8. 总结(5 分钟)

- **本日核心**: 静态抓不到就换 Playwright →
  **先 goto,再 wait,最后 query**三步循环。
- **作业说明**: 课后 `homework/task01.py`(抓 Spa 翻页帖子的标题+点赞数)、
  `homework/task02.py`(抓无限滚动页面的前 100 条),下节课前 10 分钟复盘。

---

## 易错点

1. **忘装浏览器二进制**: `pip install playwright` 后必须 `playwright install`,
   否则报 `Executable doesn't exist`。
2. **headless 忘设**: 每次执行弹一个窗口,在服务器上直接报错。
3. **没等就抓**: goto 后立刻解析拿到空 DOM,必须 `wait_for_selector`。
4. **无限滚动写死循环**: 必须设终止条件(条数不变或到上限)。
5. **翻页到最后点不存在的按钮**: 先判定存在再 click,
   否则抛 `Element not found`。
6. **误把 requests 当万能**: 看到 HTML 没数据先怀疑 JS 渲染,
   别先怪解析代码。
7. **SPA 翻页抓过渡态**: 点完下一页要
   `wait_for_load_state("networkidle")` 再抓。
8. **没关浏览器**: 用 `with` 上下文管理,或显式 `browser.close()`。

## 延伸题

- **(分布式 Playwright, ⭐⭐⭐⭐)**: 用 `ThreadPoolExecutor`
  并发抓 10 个页面,对比串行 vs 并行耗时 —— 并发工程入门。
- **(反检测对抗, ⭐⭐⭐⭐⭐)**: headless 下隐藏
  `navigator.webdriver = true`,绕过 Cloudflare 测试,讨论爬虫法律/伦理边界。
- **(完整数据 pipeline, ⭐⭐⭐)**: 今天抓的数据用 pandas 清洗,
  存入 SQLite,再 EDA 报告 —— 全链路复习。
- **(收费 API 替代爬虫, ⭐⭐⭐)**: 调研付费 API(SerpAPI / ScrapingBee),
  对比"自维护爬虫"vs"买 API"的 TCO 思维训练。
