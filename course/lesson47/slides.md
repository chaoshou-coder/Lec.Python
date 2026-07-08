# Day47 · Scrapy 框架

> **时长**: 6 小时 (讲授 + 实操)
> **前置**: Day 44-46 HTTP 请求 / BeautifulSoup 解析 / Selenium 动态页面
> **核心问题**: 如何从"手写一个爬虫"升级到"框架化批量爬取",
> 让 Scrapy 替你管理调度、并发、清洗和存储 ?

---

## 0. 引入 (5 分钟)

前一阶段我们用 `requests + bs4` 能抓单页, 一旦遇到:
- 翻页 100 页 + 每本书详情
- 需要并发、去重、断点续爬
- 需要Pipeline 清洗 → CSV / MySQL / MongoDB

代码量就爆炸。Scrapy 是 Python 爬虫的事实标准框架,
今日靶场: **books.toscrape.com 全站 500 本书**。

> 🎯 学习目标: 独立搭建 Scrapy 项目, 完成翻页 + 详情 + 存储

---

## 1. 第 1 讲 (30 分钟) —— Scrapy 架构全景

### 知识点 1.1 五大核心组件与安装

数据流: Spider → Engine → Scheduler → Downloader → Spider → Pipeline

- **Spider**: 写 parse, 产出 Request / Item
- **Scheduler**: 调度队列 + dupefilter 去重
- **Downloader**: 受 CONCURRENT_REQUESTS 控制
- **Pipeline**: 串行清洗 / 存储 (可多条)

```bash
pip install scrapy
scrapy startproject bookscraper && cd bookscraper
scrapy genspider books books.toscrape.com
```

核心文件: `items.py` / `pipelines.py` / `settings.py` / `spiders/books.py`

> 🔴 红色底线: settings.py 是全局行为总开关, 改错一处全局受影响

---

## 2. 第 2 讲 (45 分钟) —— 编写 Spider

### 知识点 2.1 Spider 类与 parse

```python
import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            url = book.css("h3 a::attr(href)").get()
            yield response.follow(url, callback=self.parse_detail)
```

> 🔴 红线: parse 必须 **yield**, 只 return Item 则翻页就断了

### 知识点 2.2 翻页: 下一页跟进

```python
def parse(self, response):
    for book in response.css("article.product_pod"):
        url = book.css("h3 a::attr(href)").get()
        yield response.follow(url, callback=self.parse_detail)
    next_page = response.css("li.next a::attr(href)").get()
    if next_page:
        yield response.follow(next_page, callback=self.parse)
```

### 知识点 2.3 详情页 + 运行

```python
def parse_detail(self, response):
    yield {
        "title": response.css("h1::text").get(),
        "price": response.css("p.price_color::text").get(),
        "stock": response.css(".availability::text").re_first(r"\d+"),
        "url": response.url,
    }
```

```bash
scrapy crawl books -o books.csv        # 导出
scrapy crawl books --loglevel=WARNING  # 安静模式
```

> 巡场重点: 先跑一次看翻页动画, 再讲限流

---

## 3. 第 3 讲 (45 分钟) —— Item + Pipeline

### 知识点 3.1 Item 结构化

```python
import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()

# spiders/books.py
from ..items import BookItem
def parse_detail(self, response):
    item = BookItem()
    item["title"] = response.css("h1::text").get()
    item["price"] = response.css("p.price_color::text").get()
    item["stock"] = response.css(".availability::text").re_first(r"\d+")
    item["url"] = response.url
    yield item
```

> 🔴 红线: 不要 Item / dict 混用! 混用则 Pipeline isinstance 判断全失效

### 知识点 3.2 Pipeline: 清洗 + 存储

```python
class PriceCleanPipeline:
    def process_item(self, item, spider):
        if item.get("price"):
            item["price"] = float(item["price"].replace("£", ""))
        return item

class StockIntPipeline:
    def process_item(self, item, spider):
        if item.get("stock"):
            item["stock"] = int(item["stock"])
        return item
```

settings.py `ITEM_PIPELINES` 启用, 编号越小越先执行

> 💡 口诀: "Pipeline 像流水线, 编号小的先上车"

---

## 4. 第 4 讲 (45 分钟) —— 去重 + 并发

默认启用 `RFPDupeFilter`, 无需配置。

### 知识点 4.2 并发与限流 (settings.py)

> 🔴 红线: 新手最常忘记! 默认 16 并发 0 延迟会被站点封禁

```python
CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 1.0
CONCURRENT_REQUESTS_PER_DOMAIN = 4
ROBOTSTXT_OBEY = True            # 必开
```

> 💡 口诀: "并发开小, delay 留一秒, robots 必遵守"

---

## 5. 当堂练 1 (30 分钟)

- `practice01.py` → 创建项目骨架, 看到 `scrapy.cfg`
- `practice02.py` → Spider 抓首页 12 本书 title
- `practice03.py` → parse 翻页下一次, 只翻两页

> 巡场重点: 检查学生是否 yield 而不是 return

---

## 6. 第 5 讲 (50 分钟) —— 全站爬取实战

### 知识点 5.1 完整 Spider 代码

```python
# bookscraper/spiders/books.py
import scrapy
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    custom_settings = {
        "CONCURRENT_REQUESTS": 8,
        "DOWNLOAD_DELAY": 0.8,
        "FEEDS": {"books.jsonl": {"format": "jsonlines", "overwrite": True}},
        "ITEM_PIPELINES": {
            "bookscraper.pipelines.PriceCleanPipeline": 300,
            "bookscraper.pipelines.StockIntPipeline": 400,
        },
    }

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield response.follow(
                book.css("h3 a::attr(href)").get(),
                callback=self.parse_detail)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        item = BookItem()
        item["title"] = response.css("h1::text").get()
        item["price"] = response.css("p.price_color::text").get()
        item["stock"] = response.css(".availability::text").re_first(r"\d+")
        item["url"] = response.url
        yield item
```

### 知识点 5.2 FEEDS 与断点续爬

```python
# settings.py —— FEEDS 替代 -o (Scrapy 2.1+)
FEEDS = {
    "output/books.jsonl": {
        "format": "jsonlines",
        "overwrite": True,
        "encoding": "utf-8",
    },
}
```

```bash
# 断点续爬 JOBDIR: Ctrl+C 后再跑同一命令自动续
scrapy crawl books -s JOBDIR=crawls/books
```

> 巡场重点: 让学生跑全站 500 本书, 观察 Runtime 与 Error counts

---

## 7. 当堂练 2 + 3 (80 分钟)

**当堂练 2 (40 分钟):**
- `practice04.py` → dict 改写为 BookItem
- `practice05.py` → PriceCleanPipeline, 验证 price 为 float

**当堂练 3 (40 分钟):**
- `practice06.py` → 全站爬取, 输出 books.jsonl
- 要求: 至少 100 本, stock 与 price 均为数值类型

> 巡场重点: pipeline 编号从小到大; FEEDS 与 -o 不要同时用

---

## 8. 总结 (5 分钟)

- **架构**: Engine → Spider → Scheduler → Downloader → Pipeline
- **Spider 写作**: parse **yield** Request / Item, 分页靠 follow
- **Item vs Dict**: 一律 Item, Pipeline 内 isinstance 过滤
- **Pipeline**: process_item 必须 return item, 编号决定顺序
- **礼貌限流**: CONCURRENT_REQUESTS + DOWNLOAD_DELAY
- **断点续爬**: `-s JOBDIR=...` 一句搞定

> 💡 一句话: "Spider 管爬, Item 管形, Pipeline 管洗, settings 管速"

---

## 易错点

1. **parse return 列表不是 yield**: yield 是生成器, return 只返回一次
2. **忘记 response.follow**: 硬编码 URL 导致相对路径拼接错
3. **process_item 未 return item**: 后续 Pipeline 拿到 None
4. **settings 改了但忘加 ITEM_PIPELINES**: 管道不生效
5. **scrapy crawl 写成 scrapy runspider**: runspider 用于单文件
6. **FEEDS 写成 FEED (少 S)**: 拼写错误静默失败, 输出为空
7. **Item 字段大小写不一致**: title / Title 是不同键

---

## 延伸题

1. Pipeline 加入 SQLAlchemy 存储到 SQLite (50 行)
2. `LinkExtractor` + `CrawlSpider` 规则化翻页
3. DownloaderMiddleware 加随机 UserAgent
4. 部署到 `scrapyd` 并用 `curl` 远程调度
5. Scrapy 与 Playwright-Scrapy 在 SPA 页面性能对比
