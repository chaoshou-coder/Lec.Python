# Day07 · 文件 I/O + 异常

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-06(print/input/变量/字符串/分支/循环/函数/列表字典)
> 关键问题: 让程序**持久化数据到磁盘**,并学会用异常处理让程序
> **不因报错就崩溃**

---

## 0. 引入(5 分钟)

- **破冰 + 抽问**(2 分钟): "前 6 天写的程序,一关掉窗口,数据
  全丢了 —— 怎么让数据留下来?"引出**文件 I/O**:程序 ↔ 硬盘
  之间的桥梁。
- **赏玩 demo**(3 分钟): 当场写一个"日记本",运行两次 —— 第二次
  能读到第一次写的内容,学员瞬间理解"持久化"三字的分量。

---

## 1. 第一讲(15 分钟) —— 文件读写基础

### 知识点 1.1 `open()` 与文件模式

1. `open(路径, 模式)` 打开文件,返回文件对象。
2. 三种基础模式:`'r'` 读(默认)、`'w'` 写(覆盖)、`'a'` 追加。
3. 读完、写完都要 `close()`,否则数据可能丢。

```python
# 写文件(覆盖)
f = open("a.txt", "w", encoding="utf-8")
f.write("第一行\n")
f.write("第二行\n")
f.close()               # 不关可能丢数据

# 读文件
f = open("a.txt", "r", encoding="utf-8")
content = f.read()      # 一次性读完全部
print(content)
f.close()
```

> 口诀:**写 `'w'` 会覆盖,追加用 `'a'`,读完记得 `close()`**。

### 知识点 1.2 `read()` / `readline()` / `readlines()`

```python
f = open("a.txt", "r", encoding="utf-8")

f.read()        # 整个文件 → 一个字符串
f.readline()    # 只读一行 → 字符串
f.readlines()   # 全部读入 → 每行作为字符串的列表

f.close()
```

### 知识点 1.3 `with` 上下文管理(推荐写法)

`with` 块结束时**自动调用 `close()`**,即便中间报错也会关,
永不漏写。

```python
# 最佳写法
with open("a.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 出 with 块,f 已自动关闭
print(content)
```

> 🔴 教学红线(`encoding`): Windows 上中文文件默认 `gbk`,
> Mac/Linux 是 `utf-8`,跨平台要**显式写
> `encoding="utf-8"`**,否则遇到中文就 `UnicodeDecodeError`。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 写 3 行日记再读出来
  (⭐⭐,8 分钟)
- 练习 2: `in_class/practice02.py` —— `readlines()` 逐行打印
  课表(⭐⭐⭐,12 分钟)

> 巡场重点: 学员常漏写 `encoding="utf-8"`,在中文路径电脑上直接
> 报错。巡场先检查这一行。

---

## 3. 第二讲(15 分钟) —— JSON 读写

### 知识点 3.1 为何需要 JSON

纯文本 `"apple,banana,orange"` 无法表达**结构化数据**(列表/
字典嵌套)。JSON(JavaScript Object Notation)是程序之间交换数
据的"通用语言"。Python 内置 `json` 模块。

### 知识点 3.2 `json.dump` / `json.load`(文件) 与
`json.dumps` / `json.loads`(字符串)

```python
import json

data = {
    "name": "小明",
    "scores": [90, 85, 92],
    "is_vip": True
}

# 写入 JSON 文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["scores"])     # [90, 85, 92]
```

- `ensure_ascii=False`:中文不转 `\uXXXX`。
- `indent=2`:美化缩进,人可读。

> 🔴 教学误区(JSON ≠ Python dict): JSON 里 `true/false/null`,
> Python 里 `True/False/None`。`json.dump` 自动转换,但手拼 JSON
> 文件时用错必崩。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 把通讯录字典写成 JSON
  再读回(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— 用 `json.loads()` 解析
  API 返回的 JSON 字符串(⭐⭐⭐,13 分钟)

> 巡场重点: `json.load`(文件) vs `json.loads`(字符串)的 `s` 是
> 新手高频混用,提前在白板上画对照表。

---

## 5. 第三讲(15 分钟) —— 异常处理

### 知识点 5.1 为何 try-except

程序遇到错误会**崩溃退出**。`try-except` 让我们"抓住"错误,
决定下一步,而不是直接死掉。

### 知识点 5.2 `try` / `except` / `else` / `finally`

```python
try:
    num = int(input("请输入整数:"))
    result = 100 / num
except ValueError:
    print("输入的不是整数!")
except ZeroDivisionError:
    print("不能除以 0!")
else:
    print("计算结果是:", result)    # 没异常才跑
finally:
    print("无论有无异常都执行")    # 常用来关文件/清理资源
```

### 知识点 5.3 常见异常速查

| 异常 | 触发场景 |
|---|---|
| `FileNotFoundError` | `open()` 文件不存在 |
| `ValueError` | `int("abc")` 转换失败 |
| `TypeError` | `"hello" + 1` 类型不匹配 |
| `KeyError` | 访问字典不存在的 key |
| `IndexError` | 访问列表越界索引 |
| `json.JSONDecodeError` | `json.loads("")` 解析非法字符串|

> 口诀:**`try` 里放危险代码,`except` 按类型分流,`else` 无错才跑,
> `finally` 必定执行**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 给除法器加异常防护,
  输错 3 次退出(⭐⭐⭐,12 分钟)
- 练习 6: `in_class/practice06.py` —— 读 JSON 文件,处理
  `FileNotFoundError` + `JSONDecodeError`(⭐⭐⭐⭐,13 分钟)

> 巡场重点: 学员常把 `except:`(裸 except)写一切,强调**必须指定
> 异常类型**,否则会吞掉真正的 Bug。

---

## 7. 小项目:日记本持久化(45 分钟)

- 项目: `mini_project/` 新建 `diary.py`
- 需求:
  1. 启动时读取 `diary.json`(不存在则用空列表)。
  2. 让用户输入一段日记,追加进列表,立刻写回文件。
  3. 输入 `quit` 时退出,并把全部日记打印出来。
  4. 所有文件操作套 `try-except`,崩不了。

```python
import json, os

FILE = "diary.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(diary):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(diary, f, ensure_ascii=False, indent=2)

# 主循环(学员补完)
diary = load()
while True:
    line = input("写日记(quit 退出):")
    if line == "quit":
        break
    diary.append(line)
    save(diary)
print("你的日记:", diary)
```

> 巡场重点: `json.load` 读空文件报 `JSONDecodeError`,提示学员
> 判空或用 `try` 跳过。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. 漏写 `encoding="utf-8"`,中文路径报错
  2. 混淆 `json.load`(文件)和 `json.loads`(字符串)
  3. 裸 `except:` 吞掉真正的 Bug
- **作业说明**: `homework/task01.py`(文件复制器)、
  `homework/task02.py`(JSON 通讯录升级版)、
  `homework/task03.py`(异常防护的除法器),下节课前 10 分钟复盘。

---

## 易错点

1. **`'w'` 模式会覆盖原文件**,`open("a.txt","w")` 瞬间清空 ——
   想追加用 `'a'`。
2. **`encoding="utf-8"` 必显式写**,跨平台中文乱码/报错是高频
   Bug。
3. **`json.load` 读文件,`json.loads` 读字符串**,末尾的 `s` 不是
   typo,是 file vs string 的区分。
4. **裸 `except:` 会吞掉所有异常**,包括 `Ctrl+C`,永远指定具体
   异常类型。
5. **出 `with` 块文件已关**,再 `f.write()` 报
   `ValueError: I/O operation on closed file`。

## 延伸题

- **(CS50P Week8 IO, ⭐⭐)**: 用 `readlines()` 读一份英文文本,
  统计单词数/行数/字符数 —— 巩固文件读取 + 字符串分割。
- **(CS50P Week8 Shirt, ⭐⭐⭐)**: 把多张 CSV 数据合并为一张
  报表 —— 巩固 JSON/文件 I/O。
- **(Real Python Exception, ⭐⭐⭐)**: 写一个"安全除法"函数,
  接受任意输入,遇到非数字/除零返回 `None` 而不是抛异常 ——
  巩固异常类型分流。
