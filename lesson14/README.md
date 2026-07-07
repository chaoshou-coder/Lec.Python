# Day14 · 文件操作基础

## 关键知识点
- `open()` 四大模式:`'r'` `'w'` `'a'` `'rb'`
- `write()` 写入 / `read()` 一次读全 / `readline()` 逐行
- `with … as` 自动关闭,异常也安全
- 文件编码:`encoding='utf-8'` 与 gbk
- `print('…', file=fp)` 直接把输出写入文件
- 路径异常处理:`FileNotFoundError`

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | `open('w')` + write 写 3 行文本 || 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | `open('r')` + read 读取全文 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | `readline()` 逐行加行号打印 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | `with open` 语法自动关闭文件 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | `'a'` 追加模式不覆盖原内容 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | log 函数加时间戳,自动创建目录 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | `copy_file(src, dst)` 完整复制 |

## 小 / 中型项目

本节无小项目。

## 阶段复习要点

Day08~Day14 阶段复习建议:- 文件读 / 写 / 追加三种模式 + `with` 语句- Day08-12 综合题目薄弱点回练(递归 / lambda / filter)
- 可让学生实现"日志程序 + 文件持久化"作为综合巩固
