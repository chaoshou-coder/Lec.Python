# Day16 · 异常处理

## 关键知识点
- `try`/`except`/`else`/`finally` 四块完整结构
- 常见异常类:`ValueError`/`TypeError`/`FileNotFoundError`/`KeyError`/`IndexError`/`ZeroDivisionError`
- `raise` 主动抛出异常
- 自定义异常类(继承 `Exception`)
- 异常处理与循环/文件操作的配合

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 捕获 ValueError,非法输入提示并重试 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | 捕获 ZeroDivisionError,除数为 0 提示 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | try/except/else/finally 四块协同 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | 捕获 FileNotFoundError 并友好提示 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | 捕获 KeyError,键不存在提示 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 20 分钟 | 使用 raise 抛出自定义 ValueError |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 封装 safe_int 函数,循环直到合法 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | 定义并抛出自定义 InvalidEmailError |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 25 分钟 | 综合运用异常处理解析配置文件 |

## 小 / 中型项目

本节无小项目

## 阶段复习要点

后续 Day21 期末总复习将综合考察异常处理各类场景(异常捕获链、raise、自定义异常等)
