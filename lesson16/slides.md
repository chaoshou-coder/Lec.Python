# Day16 · 数据摄取(CSV/JSON/Excel/SQL/API)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day11-15 已掌握 NumPy/Pandas/可视化
> 关键问题: 数据不只是 CSV,还有 JSON、Excel、数据库、API 接口 —— 本节学习"从任何源头把数据读进 Pandas"。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `plt.hist(df["年龄"])` 画的是什么图?(直方图)如果数据不在 DataFrame 里,而在一个 JSON 文件里,要先做什么?(读入 DataFrame)目的: 唤醒可视化记忆,引出"数据来源多样化"的需求。
- **赏玩 demo**(3 分钟): 现场用一条命令 `pd.read_json("api_response.json")` 从 JSON 文件读入数据,再用 `pd.read_sql` 从 SQLite 查询数据 —— 展示"一行代码连接任何数据源"。

---

## 1. 第一讲(15 分钟) —— CSV 与 Excel 读取

### 知识点 1.1 read_csv 参数详解

```python
import pandas as pd

# 基本读取
df = pd.read_csv("data.csv")

# 常用参数一览
df = pd.read_csv(
    "data.csv",
    encoding="utf-8",     # 编码(中文常用 gbk)
    sep=",",              # 分隔符(默认逗号)
    header=0,             # 第几行作为列名(默认第 0 行)
    index_col=0,          # 第几列作为索引
    usecols=["name", "age"],  # 只读指定列
    nrows=100,            # 只读前 100 行
    skiprows=[1, 2],      # 跳过第 1-2 行
    na_values=["N/A", "?"]  # 哪些值视为缺失
)
```

> 🔴 教学红线(编码问题): 中文 Windows 导出的 CSV 常用 GBK 编码,直接读会报 `UnicodeDecodeError`(references.md §3.3)。实战策略: 先试 `utf-8`,再试 `gbk`,或直接用 `encoding="gbk"`。

### 知识点 1.2 read_excel 读取 Excel

```python
# 读取 Excel 文件
df = pd.read_excel("data.xlsx")

# 指定 sheet
df = pd.read_excel("data.xlsx", sheet_name="Sheet2")
df = pd.read_excel("data.xlsx", sheet_name=0)  # 按索引

# 读取多个 sheet(返回字典)
all_sheets = pd.read_excel("data.xlsx",
                           sheet_name=None)
# all_sheets["Sheet1"], all_sheets["Sheet2"]
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用 `read_csv` 读取含中文的 CSV,指定 encoding="gbk",跳过前 2 行(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `read_excel` 读取指定 sheet,只读部分列(⭐⭐,10 分钟)

> 巡场重点: 练习 1 学员常把 `encoding` 写成 `encode` —— 提示:"read 用 encoding,write 用 没有-ing"。

---

## 3. 第二讲(15 分钟) —— JSON 与数据库读取

### 知识点 3.1 read_json 读取 JSON

```python
# 从 JSON 文件读入
df = pd.read_json("data.json")

# 从 JSON 字符串读入
import json
json_str = '''
[{"name": "张三", "age": 20},
 {"name": "李四", "age": 21}]
'''
df = pd.read_json(json_str)
print(df)
#   name  age
# 0  张三   20
# 1  李四   21
```

> JSON 必须是"记录格式"(列表套字典)才能直接读入。嵌套 JSON 需要 `json_normalize` 或手动解析。

### 知识点 3.2 read_sql 读取数据库

```python
import sqlite3
import pandas as pd

# 连接 SQLite 数据库
conn = sqlite3.connect("mydb.db")

# 用 SQL 查询,直接返回 DataFrame
df = pd.read_sql("SELECT * FROM students WHERE age > 20",
                 conn)
print(df)

# 也可以读整张表
df = pd.read_sql_table("students", conn)

# 用完关闭连接
conn.close()
```

> 🔴 教学红线(忘记关闭连接): 虽然 Pandas 读完后不强制关闭连接,但连接是有限资源,用完必须 `conn.close()`(references.md §3.3)。或使用 `with` 上下文管理器自动关闭。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 用 `read_json` 读入 JSON 字符串,提取嵌套字段(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 用 `read_sql` 从 SQLite 查询数据,用 `with` 自动关闭连接(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 4 学员常忘记 `import sqlite3` —— Pandas 只负责读 SQL,连接需要 `sqlite3` 或 `sqlalchemy`。

---

## 5. 第三讲(15 分钟) —— API 数据拉取与数据导出

### 知识点 5.1 从 API 拉取数据

```python
import requests
import pandas as pd

# 调用 API 获取 JSON 数据
response = requests.get(
    "https://api.example.com/users",
    params={"page": 1, "limit": 10},
    headers={"Accept": "application/json"}
)

# 检查状态码
if response.status_code == 200:
    data = response.json()  # 解析为字典
    df = pd.DataFrame(data["results"])
    print(df.head())
else:
    print(f"请求失败: {response.status_code}")
```

> API 三板斧: `requests.get()` 发请求 → `.status_code` 检查 → `.json()` 解析。

### 知识点 5.2 数据导出

```python
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

# 导出为 CSV
df.to_csv("output.csv", index=False, encoding="utf-8")
# index=False 不导出行索引

# 导出为 JSON
df.to_json("output.json", orient="records", force_ascii=False)
# orient="records" 记录格式
# force_ascii=False 不转义中文

# 导出到 SQL
import sqlite3
conn = sqlite3.connect("mydb.db")
df.to_sql("my_table", conn, if_exists="replace",
          index=False)
# if_exists: fail(默认)/replace(覆盖)/append(追加)
conn.close()
```

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 调用公开 API(如天气 API),把返回的 JSON 转为 DataFrame(⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 把 DataFrame 分别导出为 CSV/JSON,验证 `orient` 和 `force_ascii` 参数(⭐⭐,15 分钟)

> 巡场重点: 练习 5 学员常忘记检查 `status_code` —— 提示:"先判断成功再解析,否则 API 挂了你在解析空字符串"。

## 7. 小项目(若本日有,45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 读取中文 CSV 不指定 encoding,报 `UnicodeDecodeError`
  2. `read_sql` 后不关闭数据库连接
  3. API 请求不检查 status_code,直接解析 response.json() 报错
- **作业说明**: 课后 `homework/task01.py`(多格式读取)、`homework/task02.py`(API + 导出),下节课前 10 分钟复盘。

---

## 易错点

1. **编码问题**: 中文 CSV 常用 GBK,`pd.read_csv("f.csv", encoding="gbk")`。
2. **数据库连接关闭**: `read_sql` 后必须 `conn.close()` 或用 `with`。
3. **API 状态码**: 先检查 `response.status_code == 200` 再解析。
4. **JSON 格式**: 只有"列表套字典"格式才能直接 `read_json`,嵌套 JSON 需要额外处理。
5. **导出索引**: `to_csv` 默认导出行索引,通常要加 `index=False`。

## 延伸题

> 以下素材来自外部课程(references.md §2.3),教师可按需选用或替换当堂练。

- **(DataCamp Data Ingestion ⭐⭐)**: 读取多个 CSV 文件并 concat 合并 —— 巩固 concat。
- **(Automate the Boring Stuff ⭐⭐⭐)**: 从 OpenWeatherMap API 拉取天气数据并存储 —— 巩固 API + 导出。
- **(Kaggle Learn ⭐⭐⭐⭐)**: 从 SQLite 数据库读取 Housing 数据,做EDA 报告 —— 综合应用。
