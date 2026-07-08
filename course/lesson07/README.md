# Day07 · 文件 I/O + 异常

## 关键知识点
- `open()` 与文件模式：`'r'` 读、`'w'` 写（覆盖）、`'a'` 追加
- `read()` / `readline()` / `readlines()` 三种读取方式
- `with` 上下文管理：自动 `close()`，永不漏写
- `encoding="utf-8"` 显式指定（跨平台中文乱码问题）
- JSON 读写：`json.dump` / `json.load`（文件）、`json.dumps` / `json.loads`（字符串）
- `ensure_ascii=False` 与 `indent=2`
- 异常处理：`try` / `except` / `else` / `finally`
- 常见异常速查：`FileNotFoundError`、`ValueError`、`TypeError`、`KeyError`、`IndexError`、`json.JSONDecodeError`
- 异常类型分流 vs 裸 `except:`

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 8 分钟 | 写 3 行日记再读出来 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 12 分钟 | `readlines()` 逐行打印课表 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | 通讯录字典写 JSON 再读回 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 13 分钟 | `json.loads()` 解析 API 返回的 JSON 字符串 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 12 分钟 | 除法器加异常防护，输错 3 次退出 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 13 分钟 | 读 JSON 文件，处理 `FileNotFoundError` + `JSONDecodeError` |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | 文件复制器 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | JSON 通讯录升级版 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 25 分钟 | 异常防护的除法器 |

## 小 / 中型项目

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/diary.py` | ⭐⭐⭐⭐ | 45 分钟 | 日记本持久化（JSON + `try-except` + 菜单循环） |

## 阶段复习要点

综合题覆盖：数据类型、算术运算、字符串处理、列表操作、循环、分支、嵌套、`f-string`、`random`、文件 I/O、异常处理。
