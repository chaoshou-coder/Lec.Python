# Day45 · HTML 解析 + 正则

- **时长**: 360 分钟(6 小时)
- **前置**: Day 44 已掌握 requests, 能发送 HTTP 请求拿到网页源码
- **目标网站**: books.toscrape.com / quotes.toscrape.com
- **核心问题**: 拿到网页源码后, 如何精准提取想要的数据?

---

## 0. 引入(5 分钟)

> 上节课我们拿到了网页源码, 但源码是"一整坨"HTML。
> 今天的任务: **从 HTML 里把数据"挖"出来**。
> 爬虫链路的第三步: 请求 → 解析 → 存储。

- 展示真实源码截图, 引出两种武器: **HTML 解析器** 和 **正则**

> 🔴 红线: **能解析 HTML 就用解析器, 正则只能作为最后手段**。

---

## 1. 第一讲(30 分钟) —— HTML 结构与 DOM 树直觉

### 知识点 1.1 HTML 基本结构

```html
<html>
<head><title>页面标题</title></head>
<body>
  <div class="main">
    <h1 id="title">欢迎</h1>
    <p class="content">段落文字</p>
  </div>
</body>
</html>
```

- `<tag>`: 标签, 成对出现; `class` / `id`: 属性
- 层级: 父 / 子 / 兄弟节点
- 树形思维: html → body → div.main → h1#title

> 口诀: "HTML 是家族树, 标签是节点, 属性是名片"

### 知识点 1.2 开发者工具

- Chrome F12 → 检查元素; 右键 Copy → selector / XPath
- 🔴 红线: 必须学会用开发者工具"看到"结构。

---

## 2. 第二讲(45 分钟) —— BeautifulSoup 入门

### 知识点 2.1 安装与初始化

```python
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
resp = requests.get(url)
resp.encoding = resp.apparent_encoding  # 🔴 否则中文乱码

soup = BeautifulSoup(resp.text, "html.parser")
```

> 🔴 红线: 编码不对 → 中文乱码, 常用 utf-8。

### 知识点 2.2 find 与 find_all

```python
first_h3 = soup.find("h3")        # 单个 Tag
all_h3 = soup.find_all("h3")      # 列表, 需遍历

for h3 in all_h3:
    print(h3.text)                # 🔴 对 find_all 直接 .text 报错
```

> 🔴 红线: find 返回 Tag, find_all 返回列表, 别混用!

### 知识点 2.3 class / id / 属性查找

```python
items = soup.find_all("li", class_="product_pod")  # class_
header = soup.find("header", id="masthead")
links = soup.find_all("a", href=True)              # 属性存在
```

---

## 3. 第三讲(45 分钟) —— CSS 选择器进阶

### 知识点 3.1 select 和 select_one

```python
titles = soup.select("h3 a")              # 后代, 返回列表
products = soup.select("li.product_pod")  # 标签.class
first_title = soup.select_one("h3 a")     # 单个
```

### 知识点 3.2 常用写法

```python
soup.select("div")                # 标签
soup.select(".price_color")       # class
soup.select("#header")            # id
soup.select("div.product h3")     # 后代
soup.select("a > span")           # 直接子
soup.select("a[href]")            # 属性存在
soup.select("a[href$=html]")      # 属性结尾
```

### 知识点 3.3 实战: 提取商品价格

```python
books = soup.select("li.product_pod")
for book in books[:5]:
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    print(f"书名: {title} | 价格: {price}")
```

> 巡场: 是否先 `select()` 拿到列表再循环;
> `select_one` 后是否取属性 `["title"]`; f-string 拼接。

---

## 4. 第四讲(45 分钟) —— lxml 与 XPath 入门

### 知识点 4.1 XPath 语法示例

```xpath
//div[@class='main']/h1          # 相对路径 + 属性
//h3/a/@title                    # 取 a 的 title 属性
//p[@class='price']/text()       # 取文本
```

### 知识点 4.2 lxml 使用

```python
from lxml import etree

tree = etree.HTML(resp.text)
titles = tree.xpath("//h3/a/@title")
prices = tree.xpath("//p[@class='price_color']/text()")

for title, price in zip(titles[:5], prices[:5]):
    print(f"{title}: {price}")
```

> BS4 适合快速开发, XPath 适合精准定位, 选一个主力。

---

## 5. 第五讲(60 分钟) —— 正则表达式

### 知识点 5.1 常用元字符

| 符号 | 含义 |
|------|------|
| `.` | 任意字符(除换行) |
| `*` / `+` / `?` | 0+ / 1+ / 0或1 次 |
| `\d` `\w` `\s` | 数字 / 单词 / 空白 |
| `^` `$` | 行首 / 行尾 |
| `[abc]` | 字符集 |
| `{n,m}` | 重复次数 |

### 知识点 5.2 re 模块

```python
import re

text = "价格: ¥39.9, 库存: 100 件"
m = re.search(r"\d+\.\d", text)   # 第一个匹配
print(m.group())                   # 39.9

nums = re.findall(r"\d+", text)   # 所有匹配
print(nums)                        # ['39', '9', '100']

clean = re.sub(r"[^\w]", "_", text)  # 替换
```

### 知识点 5.3 贪婪 vs 非贪婪

```python
html = "<div>第一段</div><div>第二段</div>"
re.findall(r"<div>(.*?)</div>", html)  # ['第一段', '第二段']
```

> 🔴 红线: 正则边界 → 贪婪 vs 非贪婪。
> "加了问号就佛系, 没有问号吃到饱"

---

## 6. 第六讲(60 分钟) —— 综合实战

### 知识点 6.1 提取书籍价格

```python
import re
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
resp = requests.get(url)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")

books = soup.select("li.product_pod")
result = []
for book in books:
    title = book.select_one("h3 a")["title"]
    price_text = book.select_one("p.price_color").text
    price_num = re.search(r"[\d.]+", price_text).group()
    result.append({"title": title, "price": float(price_num)})

top5 = sorted(result, key=lambda x: x["price"], reverse=True)[:5]
for b in top5:
    print(f"¥{b['price']:6.2f}  {b['title']}")
```

### 知识点 6.2 正则提取引用文本

```python
url = "http://quotes.toscrape.com"
resp = requests.get(url)
resp.encoding = "utf-8"

quotes = re.findall(
    r'<span class="text" itemprop="text">(.*?)</span>',
    resp.text
)
for q in quotes:
    clean = re.sub(r"[“""]", "", q)
    print(clean)
```

> 巡场: r"" 原始字符串; 提取后清洗 HTML 实体。

---

## 7. 当堂练 520(60 分钟)

- **练习 1**: 用 BS4 提取所有书名 → `in_class/practice01.py`
- **练习 2**: 用 XPath 提取价格最高前 3 → `in_class/practice02.py`
- **练习 3**: 用正则提取邮箱或金额 → `in_class/practice03.py`
- **练习 4**: 综合: 书名 + 评分 + 价格写 CSV → `in_class/practice04.py`

> 巡场: encoding / find vs find_all / r""。

---

## 8. 总结(5 分钟)

| 场景 | 工具 |
|------|------|
| 按标签 / class | BS4 + select |
| 精准路径 | lxml + XPath |
| 复杂模式 | re 正则 |

- 爬虫三件套: **requests + BS4/正则 + csv/json**
- 编码第一个坑, 记得 `resp.encoding`
- 能解析就用解析器, 正则留到最后

---

## 易错点

1. **编码乱码**: 忘记 encoding
2. **find / find_all 混淆**: 对 find_all 结果直接 .text
3. **正则贪婪**: `.*` 吃一整行, 用 `.*?`
4. **没加 r""**: `\d` 写成 `r"\d"`, 否则 Python 先转义
5. **空值崩溃**: find 返回 None, 直接 .text 报错

---

## 延伸题

1. 分页抓取前 5 页, 找出性价比最高的书(评分 / 价格)
2. 反爬初探: 加 User-Agent 头模拟浏览器
3. **挑战**: 封装可复用模块, 输入 URL + 选择器, 输出列表
