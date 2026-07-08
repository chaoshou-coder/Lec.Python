# Day13 · 阶段复习② + 控制台计算器## 关键知识点
- Day08~Day12 综合:函数 + 列表 + lambda + filter/sorted
- 递归展平、回文判断、字符串解析
- 主循环 + `input()` 交互式控制台程序
- 模块化:分离运算函数 add/sub/mul/div- 历史记录:列表存储 / 只保留最近 N 条## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 15 分钟 | 函数判断字符串是否回文 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | `*args` 累加,空参返回 0 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐⭐ | 20 分钟 | sorted + lambda 按元组第二位排序 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 20 分钟 | filter + lambda 过滤 3 的倍数 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐⭐ | 25 分钟 | 递归 flatten 展平嵌套列表 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 学生成绩管理综合:排序 + filter |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | `calc` 解析优先级四则运算 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 控制台计算器,add/sub/mul/div |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 计算器加 history 记录最近 5 条 |

## 小 / 中型项目

**控制台计算器** (`task02` 为中型项目基础)- 目标:交互循环读取 `数字 运算符 数字` 格式- 验收:四则运算正确 / 除零提示 / `q` 退出
- 建议时长:30 分钟## 阶段复习要点

综合题覆盖:函数定义、lambda、filter/sorted、递归展平、字符串处理、列表 CRUD。重点检查:
- 是否写对递归基线条件
- lambda key 是否按指定字段排序
- 函数是否单一职责 / 主循环是否清晰