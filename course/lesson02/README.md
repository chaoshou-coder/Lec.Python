# Day02 · 字符串与格式化

## 关键知识点
- 字符串创建与转义字符（`\n`、`\t`、`\\`、`\"`、`\'`）
- 字符串索引：`s[i]`、负数倒着数
- 字符串切片：`s[start:end]`（左闭右开）、步长 `s[start:end:step]`
- `len()` 获取字符串长度
- 字符串查找：`find()`、`rfind()`
- 字符串判断：`isdigit()`、`isalpha()`、`isalnum()`
- 字符串替换：`replace()`（全量替换、字符串不可变）
- 格式化输出：`%`、`str.format()`、f-string（重点）

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 用 `find()` 定位 `@`，切片提取邮箱域名 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | `len()` + `isdigit()` 校验手机号合法性 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | `find()` 与 `rfind()` 正反查找关键字 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | `rfind()` 提取文件名与后缀 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | 身份证号提取出生年月日，f-string 拼接 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | `replace()` 替换敏感词 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | 解析 URL 协议与域名 |
| 3 | `homework/task03.py` | ⭐⭐⭐ | 15 分钟 | ASCII 字母转大写 |

## 小 / 中型项目

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/phone_masking.py` | ⭐⭐⭐ | 25 分钟 | `len()` + `isdigit()` 校验 11 位手机号，切片脱敏为 `138****8000` |

## 阶段复习要点

后续 Day07 阶段复习
