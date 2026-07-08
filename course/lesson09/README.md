# Day09 · 模块与高级特性

## 关键知识点
- 三种 `import` 方式：`import 模块`、`from ... import ...`、`as` 别名
- 自定义模块：同目录 `.py` 文件直接 `import`
- 包（Package）= 模块的文件夹 + `__init__.py`
- 生成器 `yield`：惰性计算、逐个产出、不占内存
- `yield from` 委托子生成器
- 生成器 vs 列表（内存、遍历次数、`len()`）
- 上下文管理器：`__enter__` / `__exit__`（进/出自动执行）
- 装饰器：接收函数 → 返回新函数，`@decorator` 语法糖
- `functools.wraps` 保留原函数名/文档
- 带参数的装饰器（再加一层）

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 把 `Student` 类移到独立模块，主程序 import 使用 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 10 分钟 | 搭 3 个文件的包结构（含 `__init__.py`） |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | 生成器实现斐波那契数列前 n 项 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 13 分钟 | 用生成器读大文件，每次只读一行到内存 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 12 分钟 | 实现 `@log` 装饰器，打印函数名和参数 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 13 分钟 | `ResourceManager` 类作为上下文管理器，`with` 退出自动 `close()` |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | 生成器实现无限序列 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 25 分钟 | 装饰器带参数 + 类方法装饰 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 项目结构搭建多模块工具包 |

## 小 / 中型项目

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/toolkit/` 整合 | ⭐⭐⭐⭐ | 45 分钟 | 工具包（`decorators.py` / `generators.py` / `main.py`） |

## 阶段复习要点

后续 Day14 阶段复习
