# Day48 · API + 反爬应对

| 项目 | 内容 |
|------|------|
| 时长 | 6 小时（讲授 4h + 练习 2h） |
| 前置 | Day 44 requests 基础 / Day 45 页面解析 |
| 关键问题 | 如何合法、稳定地获取远程数据？ |

---

## 0. 引入(5 分钟)

> 场景: 你打开 F12 → Network → 刷新页面,
> 看到成百上千条请求, 真正数据往往藏在某条 API 里。
> 直接读 API 比解析 HTML 稳定十倍, 但也更容易被封。

今天三件事:
1. 像浏览器一样"调用"API(认证/分页/限流)
2. 用 Network 面板"逆向"找到 API
3. 被反爬时优雅应对, 而不是硬刚

> 🔴 教学红线: 忘记设置 User-Agent → 被直接封禁!

---

## 1. 第1讲(45 分钟) —— REST API 调用基础

### 知识点 1.1 GET 与参数

```python
import requests

# GitHub 公开 API, 按 stars 搜 Python 仓库
url = "https://api.github.com/search/repositories"
params = {
    "q": "language:python",   # 搜索关键词
    "sort": "stars",          # 按星标排序
    "order": "desc",
    "page": 1,
    "per_page": 3
}
resp = requests.get(url, params=params)
# requests 会把 params 拼到 URL 后 ?q=language:python...
print("最终请求 URL:", resp.url)
print("状态码:", resp.status_code)
data = resp.json()
for item in data["items"][:3]:
    print(item["full_name"], "⭐", item["stargazers_count"])
```

> 教学笔记: 让学生观察 resp.url,
> 理解 params 是被"编码"到 URL 里的。

### 知识点 1.2 API Key 认证

```python
import requests
import os

# 环境变量取 key, 不硬编码!(export WEATHER_KEY=xxx)
API_KEY = os.environ.get("WEATHER_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"
resp = requests.get(url, params={
    "q": "Beijing",
    "appid": API_KEY,         # 方式1: query 参数
    "units": "metric"
})
print(resp.json())
```

> 记忆口诀: "钥匙随身带, 不写代码里" — 环境变量 > .env > 硬编码。

### 知识点 1.3 分页与限流

```python
import requests
import time

def fetch_all_pages(base_url, max_pages=5):
    """分页拉取, 遇 429 指数退避"""
    results = []
    for page in range(1, max_pages + 1):
        resp = requests.get(base_url, params={"page": page})
        if resp.status_code == 429:
            wait = 2 ** page
            print(f"触发限流, 等 {wait}s")
            time.sleep(wait)
            continue
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data:
            break
        results.extend(data)
        time.sleep(0.5)            # 礼貌限速
    return results
```

> 🔴 教学红线: 没有 sleep + 退避,
> 10 秒内就能把 IP 送进黑名单。

---

## 2. 第2讲(45 分钟) —— API 逆向工程

### 知识点 2.1 Network 面板抓包步骤

1. F12 → Network 标签
2. 勾选 **Fetch/XHR** 只看数据请求
3. 刷新 / 做目标动作(翻页、搜索)
4. 点请求 → Headers 看 URL + Method + 参数
5. 点 Response 看数据结构
6. 右键 Copy as cURL → 转 requests 代码

### 知识点 2.2 实战: 找真实列表接口

```python
import requests
from bs4 import BeautifulSoup

url = ("https://books.toscrape.com/catalogue"
       "/category/books/mystery_3/index.html")
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(resp.text, "html.parser")
books = soup.select("h3 > a")
for b in books[:5]:
    print(b["title"], "→", b["href"])
```

> 巡场重点: 让学生自己打开 Network 面板,
> 找"下一页"请求 URL 的规律(通常 page=N)。

---

## 3. 第3讲(45 分钟) —— 反爬三板斧

### 知识点 3.1 User-Agent 池

```python
import random

UA_POOL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0)",
]

def random_ua():
    return {"User-Agent": random.choice(UA_POOL)}

resp = requests.get("https://httpbin.org/headers",
                    headers=random_ua())
print(resp.json())
```

> 推荐 `fake_useragent`: `UserAgent().random` 实时拉取。

### 知识点 3.2 代理 IP 轮换

```python
proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
resp = requests.get("https://httpbin.org/ip",
                    proxies=proxies, timeout=10)
print("当前出口 IP:", resp.json()["origin"])
```

### 知识点 3.3 限速 + 指数退避

```python
def polite_get(url, retries=3, base_delay=1):
    for i in range(retries):
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp
        if resp.status_code == 429:
            delay = base_delay * (2 ** i)   # 1/2/4 秒
            print(f"429 限流 → 等待 {delay}s")
            time.sleep(delay)
    raise Exception(f"重试 {retries} 次仍失败")
```

> 记忆口诀: "UA 随机, 代理轮, 限速兜底三件套。"

---

## 4. 第4讲(30 分钟) —— CAPTCHA 与 robots.txt

### 知识点 4.1 CAPTCHA 认知

人机验证(图形/滑块/点选)。
- **课程原则**: 不破解, 了解即可。
- 商业解法: 2Captcha / Anti-Captcha 打码平台。
- 规避思路: 降频、复用 Cookie、无头浏览器。

> 🔴 教学红线: 破解 CAPTCHA 在某些地区
> 违反《计算机欺诈与滥用法》, 请务必守法。

### 知识点 4.2 robots.txt 与伦理

```python
from urllib.robotparser import RobotFileParser

def can_fetch(url):
    rp = RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)

print("允许抓 Google 搜索?",
      can_fetch("https://www.google.com/search"))
print("允许抓 Wikipedia?",
      can_fetch("https://www.wikipedia.org/wiki/Python"))
```

> 记忆口诀: "robots.txt 是门铃, 不按就闯是侵权。"

---

## 5. 当堂练 1(30 分钟)

调用 GitHub 仓库搜索 API, 按关键词搜,
按星标降序取前 5, 打印 full_name + stars。

文件: `in_class/practice01.py`

---

## 6. 当堂练 2(30 分钟)

爬取 books.toscrape.com Mystery 分类全部书名,
要求: 随机 UA + 每请求休息 1s + 重试 3 次。

文件: `in_class/practice02.py`

---

## 7. 当堂练 3(30 分钟)

读取任意 robots.txt, 判断 3 个 URL 是否允许抓取,
输出并口头说明哪些站点限制严格。

文件: `in_class/practice03.py`

---

## 8. 总结(5 分钟)

| 主题 | 一句话 |
|------|--------|
| REST API | GET 带参数, JSON 接数据, 分页退避是标配 |
| 逆向抓包 | F12 看 XHR, 找 URL 规律, Copy cURL 复用 |
| 反爬三板斧 | UA 随机 / 代理轮 / 限速退避 |
| 伦理底线 | 先看 robots.txt, 不破解 CAPTCHA, 不恶意高频 |

> 下节预告: Day 49 把抓到的数据用 ORM 存入数据库。

---

## 易错点

1. `resp.json()` 前没检查 `status_code`,
   空响应抛 `JSONDecodeError`。
2. 中文参数没转义, 应用 `params=` 传 dict。
3. 循环里忘写 `time.sleep()`, 触发 429 就晚了。
4. API Key 硬编码传 GitHub → 立即失效 + 邮件告警。
5. 证书失败时 `verify=False` 关掉校验,
   正确做法是指定证书路径。

## 延伸题

1. 写装饰器 `@rate_limit(calls=2)`,
   限制被装饰函数每秒最多调用 N 次。
2. 用 `fake_useragent` 实现 UA 池自动刷新,
   每小时更新一次, 过期重新拉取。
3. 研究 GitHub OAuth 认证, 用 Personal Access Token
   调一个需登录接口, 对比认证前后速率限制(60 vs 5000/h)。
