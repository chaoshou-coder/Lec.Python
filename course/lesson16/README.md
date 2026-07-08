# Lesson16 · 数据摄取(CSV / JSON / Excel / SQL / API)

> 前置: Lesson11-15 已掌握 NumPy / Pandas / 可视化
> 重点: 数据不只是 CSV,还有 JSON、Excel、数据库、API —— 一行代码连任何数据源

## 关键知识点
- `read_csv` 参数详解:encoding / sep / header / index_col / usecols / nrows / skiprows / na_values
- `read_excel`:指定 sheet、读多个 sheet(返回字典)
- `read_json`:文件 / 字符串(必须是"列表套字典"格式)
- `read_sql`:`sqlite3` 连接 + SQL 查询,用完 `conn.close()`
- API 数据拉取:`requests.get` → status_code 检查 → response.json()
- 数据导出:`to_csv`(index=False) / `to_json`(orient/force_ascii) / `to_sql`(if_exists)

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | read_csv 中文 gbk + skiprows |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | read_excel 指定 sheet/usecols |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | read_json 字符串 + 嵌套字段 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | read_sql + with 自动关闭 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 15 分钟 | 调用公开 API 转 DataFrame |
| 6 | `in_class/practice06.py` | ⭐⭐ | 15 分钟 | DataFrame 导出 CSV/JSON |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 多格式读取 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | API + 导出 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- 中文 CSV 常用 GBK,读取失败尝试 encoding="gbk"
- `read_sql` 后必须 `conn.close()` 或用 `with`
- API 请求先检查 `status_code == 200` 再解析
- JSON 嵌套需要 `json_normalize` 或手动解析
- `to_csv` 默认导出行索引,通常加 index=False
