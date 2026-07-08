# Day44 · HTTP 协议 + requests

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Python 函数/OOP/文件/异常已掌握;Day43 了解 socket/TCP
> 关键问题: 浏览器是怎么和服务器"说话"的?为什么刷太多会被封?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): TCP 先握手像打电话;UDP 直接扔像发明信片。
  为"应用层 HTTP"铺路。
- **赏玩 demo**(3 分钟): 浏览器打开 `books.toscrape.com`,F12 切
  Network,点一本书,看到"状态码 200、响应是 HTML"。引出主题。

---

## 1. 第一讲(15 分钟) —— HTTP 请求方法与状态码

### 知识点 1.1 GET vs POST

**GET**: 取数据,参数挂 URL 后 `?key=value`,像"点菜"。
**POST**: 提交数据,参数藏 body 里,像"交信封"。

| 方法 | 用途 | 参数位置 | 幂等 |
|------|------|----------|------|
| GET  | 查询 | URL     | 是   |
| POST | 提交 | body    | 否   |

### 知识点 1.2 状态码

**200** OK / **301/302** 重定向 / **404** Not Found / **403** Forbidden
/ **429** Too Many / **500** Server Error

```python
import requests

resp = requests.get("http://books.toscrape.com/")
print(resp.status_code)  # 200
```

> 🔴 教学红线: 看到 `200` ≠"数据拿到了"。可能返回反爬页/验证码。
> 原则:**先 print 再解析**。

### 知识点 1.3 排错起点

200 但空 → 参数错了;404 → URL 拼错;403/429 → 被反爬;500 → 服务器炸

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` — 请求 `httpbin.org/status`
  下的 200/404/500,打印状态码(⭐,5 分钟)
- 练习 2: `in_class/practice02.py` — 抓 books.toscrape.com 第 1/2/3
  页,打印状态码 + HTML 长度(⭐⭐,10 分钟)

> 巡场重点: 学员把 `resp` 当字符串切片;提示:**resp 是 Response
>  对象**,要 `.text` 才是字符串。

---

## 3. 第二讲(15 分钟) —— 请求头 Headers

### 知识点 3.1 四个关键 Header

```python
headers = {
    "User-Agent": "Mozilla/5.0 Chrome/120.0",
    "Referer": "http://books.toscrape.com/",
    "Cookie": "session=abc123",
    "Authorization": "Bearer eyJhbGciOi...",
}
resp = requests.get(url, headers=headers)
```

- **User-Agent**: 不设置 → 默认 `python-requests/2.x`,被识为爬虫 → 403。
- **Referer**: 从哪个页面跳转(防盗链)。**Cookie**: 登录凭证。
- **Authorization**: 带 Token 访问受保护资源。

### 知识点 3.2 User-Agent 是生命线

```python
# ❌ 裸请求,秒被识别 → 可能 403
resp = requests.get("http://books.toscrape.com/")

# ✅ 带 UA,恢复正常 → 200
resp = requests.get(
    "http://books.toscrape.com/",
    headers={"User-Agent": "Mozilla/5.0"}
)
```

> 🔴 教学红线:**永远不要裸写 requests.get(url)**。养成加
> `headers={"User-Agent": ...}` 的习惯,否则明天就 403。

## 4. 当堂练 2(20 分钟)

- 练习 3: `in_class/practice03.py` — 对比用 UA / 不用 UA 同一 URL
  的状态码差异(⭐⭐,10 分钟)
- 练习 4: `in_class/practice04.py` — 请求 `httpbin.org/headers`,
  查看服务器实际收到的请求头(⭐⭐,10 分钟)

> 巡场重点: 学员把 headers 拼错成 header;提示:**参数名是
>  `headers`(复数)**。

---

## 5. 第三讲(15 分钟) —— 参数传递与响应处理

### 知识点 5.1 三种参数

```python
resp = requests.get(
    "http://httpbin.org/get",
    params={"q": "python", "page": 1}
)
print(resp.url)  # .../get?q=python&page=1

resp = requests.post(
    "http://httpbin.org/post",
    data={"username": "abc", "password": "123"}
)

resp = requests.post(
    "http://httpbin.org/post",
    json={"name": "lec", "score": 95}
)
```

> 口诀:**params 拼 URL,data 是表单,json 是 API**。

### 知识点 5.2 响应处理四件套

- **`status_code`**: 先判断 / **`text`**: 字符串
- **`json()`**: JSON 转 dict / **`content`**: 字节(图片)

```python
resp = requests.get("http://httpbin.org/json")
if resp.status_code != 200:
    print("请求失败"); exit()

data = resp.json()
print(data["slideshow"]["title"])
html = resp.text     # 自动按 apparent_encoding 解码
```

> 🔴 教学红线:**中文乱码**常因没设编码。需手动:
> `resp.encoding = resp.apparent_encoding`。

### 知识点 5.3 下载二进制

```python
resp = requests.get(
    "http://books.toscrape.com/media/cache/cover.jpg",
    headers={"User-Agent": "Mozilla/5.0"}
)
with open("cover.jpg", "wb") as f:
    f.write(resp.content)  # content 不是 text
```

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` — 请求 `httpbin.org/get` 带
  `params={"lang": "zh"}`,打印最终 URL(⭐⭐,10 分钟)
- 练习 6: `in_class/practice06.py` — 抓 books.toscrape.com 首页,
  查看 HTML 长度,并解决中文乱码(⭐⭐⭐,15 分钟)

> 巡场重点: 中文站常遇乱码;提示:`resp.encoding = "utf-8"`。

---

## 7. 第四讲(15 分钟) —— Session 保持会话与限速

### 知识点 7.1 为什么需要 Session

```python
s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0"})
s.get("http://example.com/login", data={"u": "a", "p": "b"})
s.get("http://example.com/profile")  # 带 Cookie,200
```

> Session = "虚拟浏览器",跨请求保持一致状态。

### 知识点 7.2 限速与指数退避

```python
import time

for page in range(1, 21):
    resp = requests.get(
        f"http://books.toscrape.com/catalogue/page-{page}.html",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    print(page, resp.status_code)
    time.sleep(1)  # 每秒最多 1 次

def fetch(url, max_retry=3):
    for attempt in range(max_retry):
        resp = requests.get(
            url, headers={"User-Agent": "Mozilla/5.0"}
        )
        if resp.status_code == 200:
            return resp
        if resp.status_code == 429:
            wait = 2 ** attempt  # 1, 2, 4 秒
            print(f"429 → sleep {wait}s")
            time.sleep(wait)
    return None
```

> 🔴 教学红线:**每页 sleep(1)** 是爬虫入门铁律。遇 429 指数退避
> (sleep 2ⁿ 秒),后续学随机间隔(让请求看起来像人类)。

## 8. 当堂练 4(25 分钟)

- 练习 7: `in_class/practice07.py` — 用 Session 请求
  `httpbin.org/cookies/set/sessioncookie/123456789`,再访问
  `/cookies`,打印返回的 Cookie(⭐⭐⭐,15 分钟)
- 练习 8: `in_class/practice08.py` — 用 `for` + `sleep(1)` 抓
  books.toscrape.com 前 5 页(⭐⭐⭐,10 分钟)

> 巡场重点: 学员抓 5 页总是忘记 sleep;提示:**写爬虫先写 sleep**。

---

## 9. 综合实战(45 分钟)

**抓 books.toscrape.com 前 3 本书的标题 + 价格 + 评分**:

```python
import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0"})

resp = s.get("http://books.toscrape.com/")
resp.encoding = "utf-8"

soup = BeautifulSoup(resp.text, "html.parser")
books = soup.select("article.product_pod")[:3]

result = []
for b in books:
    title = b.h3.a["title"]
    price = b.select_one(".price_color").text
    rating = b.select_one(".star-rating")["class"][1]
    result.append({"title": title, "price": price, "rating": rating})

import json
print(json.dumps(result, ensure_ascii=False, indent=2))
```

---

## 10. 总结(5 分钟)
- **本日错 4 件事**:
  1. 裸写 `requests.get(url)` 不带 UA → 秒 403
  2. 高频请求无 sleep → 429
  3. 把 `resp` 当字符串 / 把 `header` 拼成单数
  4. 中文乱码没改 encoding
- **作业**: `homework/task01.py`(Session 抓 books.toscrape.com 前 3
  页书名存 JSON)、`homework/task02.py`(实现指数退避函数)。

---
## 易错点

1. **忘记 UA**: 默认 `python-requests/2.x` 一眼被识;**必须加 headers**。
2. **params/data 混用**: GET 用 params,POST 用 data/json,别搞反。
3. **乱码**: 中文站显式设 `resp.encoding = "utf-8"`。
4. **session 误用**: 跨请求保持 Cookie 才需要 Session。
5. **429 退避**: 遇 429 不是越快越好,是指数退避(1→2→4 秒)。
6. **图片用 `.text`**: 二进制必须用 `resp.content`。
## 延伸题

- **指数退避(⭐⭐⭐)**: 测试 `fetch()` 重试节奏;加随机抖动避"惊群"。
- **多页限速实验(⭐⭐⭐⭐)**: 对比 sleep(1)/sleep(0.5)/无 sleep 成功率,
  用 `time.perf_counter()` 统计耗时。
- **Session 登录全流程(⭐⭐⭐⭐)**: 模拟"登录 → 访问个人信息 → 退出",
  理解 Cookie 生命周期。
