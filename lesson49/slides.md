# Day49 · 数据存储 + 并发爬取

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day44-48 爬虫全流程(requests / lxml / 解析 / 反爬绕过)
> 关键问题: 单线程爬 1000 本书要 5 分钟,如何压到 30 秒?数据存
> CSV、SQLite、MongoDB 各适合什么场景?本节用
> books.toscrape.com 做**万级采集实战**,打通"爬 + 存 + 并发"闭环。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `requests.get` 拿到的
  是什么类型?`etree.HTML` 接收什么输入?反爬三件套
  (UA / 延时 / Session)各防什么?目的: 唤醒"同步单页爬取"
  记忆,为"并发 + 存储"升级埋伏笔。
- **赏玩 demo**(3 分钟): 跑两段脚本 —— A 段"单线程串行"
  爬 books.toscrape.com 前 20 页(计时 ~8 秒);B 段"asyncio
  + aiohttp 并发"爬同样的 20 页(计时 ~1 秒)。让学员感受
  **4~8x 提速** —— 今天目标:让每个人都能写出 B 段并持久化。

---

## 1. 第一讲(25 分钟) —— 存储方案三选一

### 知识点 1.1 三种存储方案速览

```python
# CSV —— 边爬边追加,内存只留一行
import csv
with open("books.csv", "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["A Light in the Attic", "51.77", "Three"])

# JSON —— 读-改-写模式追加
import json
def append_json(path, rec):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except FileNotFoundError:
        data = []
    data.append(rec)
    json.dump(data, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

# SQLite —— title 设 UNIQUE,自然去重
import sqlite3
conn = sqlite3.connect("books.db")
conn.execute("""CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY, title TEXT UNIQUE,
    price REAL, rating INTEGER)""")
conn.execute("INSERT OR IGNORE INTO books VALUES(?,?,?,?)",
             (None, "A Light in the Attic", 51.77, 3))
conn.commit(); conn.close()
```

> 🔴 教学红线(万级数据全存内存再写): 全部 `list.append`
> 再一次 `json.dump` —— 中途崩全丢。正确做法:边爬边落盘。

> 对比表:

| 方案 | 优势 | 劣势 | 适用场景 |
|---|---|---|---|
| CSV | 人类可读、Excel 直开 | 无类型、无索引 | 快速出图、小报表 |
| JSON | 嵌套友好 | 追加慢、占内存 | API 消费、配置文件 |
| SQLite | 去重、索引、SQL | 需 SQL 知识 | 万级以上、去重查重 |

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 爬 books.toscrape.com
  第 1 页,把 20 本书写入 `books.csv`(⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 爬前 5 页共 100 本书,
  用 SQLite `INSERT OR IGNORE` 去重,验证重复跑两次
  `SELECT COUNT(*)` 不变(⭐⭐⭐,15 分钟)

> 巡场重点: 看学员 `open` 是否带 `encoding="utf-8"` ——
> 中文书必乱码;看 `.db` 路径是否用相对路径,避免权限错。

---

## 3. 第二讲(25 分钟) —— asyncio + aiohttp 异步爬虫

### 知识点 3.1 同步 vs 异步:一张图看懂差异

| 特性 | requests(同步) | aiohttp(异步) |
|---|---|---|
| 模型 | 阻塞 → 等 IO → 下一请求 | 发请求 → 切走 → 回来收 |
| 100 个请求 | 逐个等待 ~80 秒 | 并发 ~3 秒 |
| 适用 | 简单脚本 | 高并发采集 |

### 知识点 3.2 aiohttp 最小可跑示例

```python
import asyncio
import aiohttp

async def fetch(session, url):
    """单个 GET,返回 HTML 文本"""
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = [f"https://books.toscrape.com/catalogue/page-{i}.html"
            for i in range(1, 6)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        htmls = await asyncio.gather(*tasks)   # 并发执行
    print(f"共拿到 {len(htmls)} 页")

asyncio.run(main())
```

> 口诀:**`async def` 声明、`await` 等结果、`asyncio.run` 启动**
> —— 三件套缺一不可。

### 知识点 3.3 解析 + 存储一体化

```python
from lxml import etree

async def fetch_and_save(session, url, cur):
    html = await fetch(session, url)
    tree = etree.HTML(html)
    for book in tree.xpath('//article[@class="product_pod"]'):
        title = book.xpath('.//h3/a/@title')[0]
        price = book.xpath('.//p[@class="price_color"]/text()')[0]
        cur.execute(
            "INSERT OR IGNORE INTO books(title, price) VALUES (?,?)",
            (title, price)
        )
```

> 🔴 教学红线(异步代码里混用 `requests`): `requests.get`
> 是**阻塞调用**,放在 `async def` 里会**卡住整个
> event loop**,并发直接退化成串行。正确做法:**所有
> IO 都用 `aiohttp`**,或把阻塞调用包到
> `loop.run_in_executor` 里。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 把上节课单线程脚本改
  写成 aiohttp 并发版,对比 50 页耗时(⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 故意在 `async def`
  里调用 `requests.get`,观察耗时退化,再改回 aiohttp 验证
  (⭐⭐⭐,10 分钟)

> 巡场重点: 看学员是否在 `async def` 里写 `time.sleep`
> —— 应改成 `await asyncio.sleep`,否则同样阻塞 loop。

---

## 5. 第三讲(25 分钟) —— 线程池并发下载

### 知识点 5.1 concurrent.futures 线程池

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_one(url):
    """单个下载(阻塞 IO),供线程池调度"""
    import requests
    resp = requests.get(url, timeout=10)
    return resp.content

urls = [f"https://books.toscrape.com/catalogue/page-{i}.html"
        for i in range(1, 51)]

# max_workers=8 表示最多 8 个线程并发
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = {pool.submit(download_one, u): u for u in urls}
    for f in as_completed(futures):
        html = f.result()
        # 解析 + 存储逻辑...
```

> 口诀:**`ThreadPoolExecutor` 是"请 8 个员工同时干活" ——
> 主线程只管派活 + 收结果**。

### 知识点 5.2 异步 vs 线程池 + SQLite 加锁

```python
import sqlite3

# check_same_thread=False 允许多线程共享连接
conn = sqlite3.connect("books.db", check_same_thread=False)
# 但写入仍需串行化,用 threading.Lock 包裹
import threading
write_lock = threading.Lock()

def safe_insert(record):
    with write_lock:
        conn.execute(
            "INSERT OR IGNORE INTO books(title) VALUES (?)",
            (record,)
        )
        conn.commit()
```

> 🔴 教学红线(SQLite 多线程写入不加锁): 同时 commit 会抛
> `database is locked`。正确做法:全局 `Lock` 串行化,或
> 每线程独立 `connect`。
>
> 选型口诀:**新项目用 asyncio,老代码改造用线程池**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 用 ThreadPoolExecutor
  并发下载 100 本书的图片,`max_workers` 分别设 1/4/16
  ,对比耗时,找最优并发数(⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 故意多线程不加锁
  写 SQLite,复现 `database is locked`,再用 Lock 修复
  (⭐⭐⭐⭐,10 分钟)

> 巡场重点: 看学员 `max_workers` 是否设太高(>32 会被
> 目标站点反爬 ban IP) —— 生产环境建议 4~16。

---

## 7. 小项目:万级数据采集(45 分钟)

- 项目: `mini_project/project01.py` —— books.toscrape.com
  全部 1000 本书(50 页)完整采集
  - 并发: asyncio + aiohttp,并发度 16
  - 解析: lxml 抽 title / price / rating / availability
  - 存储: SQLite + `INSERT OR IGNORE` 去重
  - 日志: 每 50 本打印进度,异常页记入 `fail.log`
  - 目标: 总耗时 < 60 秒,`SELECT COUNT(*) = 1000`
    跑两次 count 不变(⭐⭐⭐⭐)

> 口诀:**"爬 1000 本书要 1 分钟,不丢一本,不重一条" —— 这
> 是 AI 就绪工程师的基本功验收**。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 异步函数里混用 `requests`,并发退化成串行
  2. 万级数据堆内存最后一次性写崩,应边爬边落盘
  3. SQLite 多线程写不加锁,`database is locked` 频发
- **作业说明**: 课后 `homework/task01.py`(aiohttp 并发爬
  books.toscrape.com 并存 SQLite)、`task02.py`(对比
  asyncio vs ThreadPoolExecutor 在 500 页上的耗时差异),
  下节课前 10 分钟复盘。

---

## 易错点

1. **异步函数里调阻塞 IO**: `requests.get` / `time.sleep`
   会卡住 event loop,所有并发变串行。
2. **万级数据全存内存**: 中途崩=全丢 —— 应边爬边写。
3. **`asyncio.run` 只能调一次** —— Jupyter 里用
   `await main()` 代替。
4. **`session` 必须复用**: 每次 `ClientSession()` 会
   耗尽 fd —— 整个工程共享一个 session。
5. **`gather` vs `wait`**: `gather` 保序、`wait` 不保序
   且支持 timeout / FIRST_COMPLETED。
6. **SQLite 多线程写**: 加 `Lock` 或每线程独立连接。
7. **`max_workers` 并非越大越好**: 过多会触发反爬 ——
   实战 4~16。
8. **忘记 `await`**: 返回协程对象而非结果,后续报
   `TypeError: 'coroutine' object is not subscriptable`。

## 延伸题

- **(分布式爬虫 + Redis 去重, ⭐⭐⭐⭐)**: 用 Redis SET
  做全局 URL 去重,多台机器共享爬取进度 —— 工业级爬虫
  入门。
- **(断点续爬, ⭐⭐⭐)**: 把已爬 URL 记入 SQLite,重启
  脚本自动跳过已完成页 —— 处理中途崩溃的必备能力。
- **(限速令牌桶, ⭐⭐⭐⭐)**: 实现 token bucket 算法,
  把并发请求速率控制在不触发反爬的阈值 —— 实战优雅采集。
- **(asyncio + aiohttp + 进度条, ⭐⭐⭐)**: 用 `tqdm.asyncio`
  给异步采集加实时进度条 + 预估剩余时间 —— 工程化体验
  提升。
- **(数据存储到 MongoDB, ⭐⭐⭐)**: 用 `pymongo` 把
  1000 本书写入 MongoDB,体验 schema-free 的灵活插入
  —— 非关系型存储入门。
