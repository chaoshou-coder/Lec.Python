# Day17 · JSON 与 CSV

## 关键知识点
- `json.dumps()`/`json.loads()` 字符串与 Python 互转
- `json.dump()`/`json.load()` 文件与 Python 互转
- `csv.reader()`/`csv.writer()` 读写 CSV 文件
- `with` 语句配合文件操作管理资源
- 异常处理在 IO 场景中的应用

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | json.dumps() 字典转 JSON 字符串 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | json.loads() JSON 字符串转字典 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | json.dump() 写入 JSON 文件 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | json.load() 读取 JSON 文件 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | csv.writer + csv.reader 综合读写 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | save_ledger/load_ledger JSON 持久化 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | 字典列表导出为 CSV 文件 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 综合账本:增删查 / 月度统计 / CSV 导出 |

## 小 / 中型项目

**个人账本管理工具**(homework/task03.py)
- 目标:实现一个兼具 JSON 持久化、CSV 导出、月度统计的命令行账本
- 验收点:添加记录 / 查看所有记录 / 按月统计 / 导出 CSV / 异常处理
- 建议时长:30 分钟

## 阶段复习要点

后续 Day21 期末总复习将综合考察 JSON/CSV IO 与异常处理协同
