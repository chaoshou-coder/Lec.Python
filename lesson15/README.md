# Day15 · 文件操作进阶 + os 模块

## 关键知识点
- `os.getcwd()`:获取当前工作目录
- `os.listdir()`:列出目录下文件与子目录
- `os.mkdir()` / `os.rmdir()`:创建 / 删除空目录
- `os.rename()`:重命名文件
- `os.path.exists()`:判断路径是否存在
- `os.path.getsize()`:获取文件大小- 组合:遍历 + 过滤扩展名 + 批量文件操作

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | `os.getcwd()` 打印工作目录 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | `os.listdir()` 遍历打印 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | `mkdir` + `exists` + `rmdir` 全流程 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | `os.path.exists` 检查文件有无 || 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | `listdir` + `.endswith('.txt')` 过滤 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 20 分钟 | `os.rename` 重命名并校验内容 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 批量创建 file_n.txt 写入序号 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | 给目录下 .txt 文件前加序号 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 统计文件数量和总字节大小 |

## 小 / 中型项目

本节无小项目。

## 阶段复习要点

Day08~Day15 期末综合方向提示:- 综合文件操作 + 函数封装 + 递归遍历目录
- 结合 Day13 控制台工程,实现"持久化日志 + 文件备份"- 重点检查异常处理与路径拼接是否规范
