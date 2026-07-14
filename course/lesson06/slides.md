# Day06 · 列表与字典

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-05 已掌握变量、字符串、条件、循环、`def` 函数、`return`、`in` 运算符
> 关键问题: 当数据量增大(比如 100 个名字),一个一个变量存不现实 —— Python 提供**列表**(有序排队)和**字典**(带标签盒子)两种容器,本节进入 **CRUD 时代 = 增删改查**

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— Python 函数四种形式是哪四种?`return a, b` 实际返回什么?`in` 运算符能判断什么?
- **赏玩 demo**(3 分钟): 在黑板上画 5 个独立变量 `name1 = "张三"`, `name2 = "李四"` ... 画到第 5 个时停下:"如果我要存 1000 个名字怎么办?"引出"列表 = 把一排格子粘在一起"。再问: "如果既存名字又存电话,一一对应怎么办?"引出"字典 = 带 key 的快递柜"。

---

## 1. 第一讲(15 分钟) —— 列表创建、索引、切片

### 知识点 1.1 列表:有序、可变、可重复

```python
fruits = ["苹果", "香蕉", "橘子"]
numbers = [1, 2, 3, 4, 5]
mixed = "张三", 18, True]    # 可混合类型(但不推荐)
empty = []                   # 空列表
```

> 列表和字符串很像:**有序、支持索引和切片**;关键区别是字符串不可变,列表**可以修改**。

### 知识点 1.2 索引 + 切片(同字符串)

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
print(fruits[0])     # 苹果
print(fruits[-1])    # 葡萄
print(fruits[1:3])   # ['香蕉', '橘子'] ← 左闭右开
print(fruits[::-1])  # ['葡萄', '橘子', '香蕉', '苹果'] ← 逆序
```

### 知识点 1.3 列表是可变的(跟字符串不一样!)

```python
fruits = ["苹果", "香蕉"]
fruits[0] = "榴莲"           # 直接改,OK!
print(fruits)                # ['榴莲', '香蕉']

# 字符串:s[0] = "X"  ← 报错!字符串不可变
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 列表创建 + 索引 + 打印全部(⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— `append()` + `while` 循环输入朋友名单(⭐⭐,15 分钟)

> 巡场重点: 看学员是否用了 `fruits[-1]` 取最后一个(而不是 `fruits[len(fruits)-1]`,虽然后者也对但不够 Python)。

---

## 3. 第二讲(15 分钟) —— 列表 CRUD:`append` `insert` `pop` `remove` `sort`

### 知识点 3.1 增:`append` `insert` `extend`

```python
fruits = ["苹果", "香蕉"]

# append:末尾追加一个
fruits.append("橘子")
print(fruits)   # ['苹果', '香蕉', '橘子']

# insert:指定位置插入
fruits.insert(1, "榴莲")
print(fruits)   # ['苹果', '榴莲', '香蕉', '橘子']

# extend:合并另一列表(等价 +=)
fruits.extend(["葡萄", "西瓜"])
```

### 知识点 3.2 删:`pop` `remove` `clear`

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄"]

# pop:按索引删除,返回被删元素
last = fruits.pop()         # 删末尾 "葡萄"
first = fruits.pop(0)       # 删索引 0 "苹果"

# remove:按值删第一个匹配项
fruits.remove("香蕉")       # 删 "香蕉"
# fruits.remove("不存在的值")  ← ValueError!

# clear:清空整个列表
# fruits.clear()
```

### 知识点 3.3 改 + 查:`sort` `index` `count`

```python
nums = [3, 1, 4, 1, 5]
nums.sort()                 # 原地排序,原列表改变 → [1, 1, 3, 4, 5]
nums.sort(reverse=True)     # 降序 → [5, 4, 3, 1, 1]

# 判断是否存在
if 3 in nums:
    print("找到了")

# 第一次出现的索引
idx = nums.index(3)          # 2

# 计数
cnt = nums.count(1)          # 2
```

> 🔴 教学红线(`sort()` 返回 None): 学员常写 `sorted_nums = nums.sort()` 然后 `print(sorted_nums)` 得到 `None`。**`sort()` 是原地排序,返回 `None`**,要直接看 `nums`。如需保留原列表用 `sorted(nums)`。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 累加求总分/最高/最低(不用 sum/max)(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— `in` 运算符判断用户名是否重复(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 3 学员常把 `highest = 0` 而不是 `scores[0]`,负数分数时出错;练习 4 看学员是否 `if new_user in users` 而不是手写循环。

---

## 5. 第三讲(15 分钟) —— 字典 CRUD

### 知识点 5.1 字典:带 key 的快递柜

```python
# 创建
stu = {"name": "小明", "age": 18, "city": "成都"}
empty_dict = {}

# 取值(两种方式)
print(stu["name"])       # 小明
# print(stu["phone"])    # ❌ KeyError!
print(stu.get("phone", "未填写"))   # 未填写 ← get 有默认值,不报错
```

> 口诀:**列表用索引(0,1,2...)找元素;字典用 key 找 value**。

### 知识点 5.2 增 / 改 / 删

```python
stu = {"name": "小明", "age": 18}

# 增:直接给新 key 赋值
stu["city"] = "成都"

# 改:覆盖原有 key 的值
stu["age"] = 19

# 删:pop
stu.pop("city")

# 清空
# stu.clear()
```

### 知识点 5.3 遍历字典:`keys()` `values()` `items()`

```python
stu = {"name": "小明", "age": 18, "city": "成都"}

for key in stu:
    print(key)                  # name age city(遍历 key)

for key in stu.keys():
    print(key)

for value in stu.values():
    print(value)                # 小明 18 成都

for key, value in stu.items():
    print(f"{key}: {value}")   # 最强迭代方式
```

> `items()` 是字典最强的迭代方式 —— 同时拿到 key 和 value,**必须掌握**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 简易购物车菜单(添加/删除/退出)(⭐⭐⭐⭐,20 分钟)
- 练习 6: `in_class/practice06.py` —— 嵌套列表 + f-string 格式化学生信息(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 练习 5 看学员写的是函数式的还是脚本式的,引导函数式封装;练习 6 看学员是否用 f-string 拼接多个字段,还是用 `+` 累加。

---

## 7. 小项目:通讯录 v1(45 分钟)

- 项目: `mini_project/` 新建 `contact_book_v1.py`
- 要求:用**字典**存储通讯录,菜单循环:
  1. 添加联系人(name → phone)
  2. 查找联系人(按 name 查 phone)
  3. 删除联系人
  4. 查看全部联系人
  0. 退出
- 核心数据结构:`contacts = {"小明": "13800138000", "小红": "13900139000"}`

> 巡场重点: 学员常忘了处理"查无此人"的边界(用 `if name in contacts` 或 `contacts.get(name, "未找到")`);第二个常见 bug 是"空通讯录查看全部"要给出友好提示而不是啥也不显示。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. `list.sort()` 返回 `None`,学员误以为它返回新列表
  2. 字典 `d[key]` 不存在时 `KeyError`,应当用 `d.get(key, 默认值)`
  3. 删除列表元素时修改了正在遍历的列表(边遍历边删导致跳元素)
- **作业说明**: `homework/task01.py`(BMI 计算器循环输入)、`homework/task02.py`(水仙花数 + 循环)、`homework/task03.py`(猜数字游戏),下节课前 10 分钟复盘。

---

## 易错点

1. **`list.sort()` 是原地排序**,返回 `None`,不要写 `sorted = lst.sort()`。
2. **`d[key]` 找不到会 `KeyError`**,安全取值用 `d.get(key, default)`。
3. **遍历列表时不要修改列表**(增删元素),会跳过元素;如需改动,遍历副本或倒序删。
4. **`append(x)` 追加单个元素**,`extend([x, y])` 或 `+=` 合并另一个列表。
5. **列表切片返回新列表**,不改变原列表;`sort()` 改变原列表,两个行为相反。

## 延伸题

- **(Grocery List, CS50P Week3, ⭐)**: 输入菜名,统计每种菜出现次数,按大写字母序输出 —— 巩固字典 `counts[item] = counts.get(item, 0) + 1`。
- **(Taqueria, CS50P Week3, ⭐⭐⭐)**: 外卖菜单查价 + 累加总价 —— 巩固字典 + while 菜单循环。
- **(Scourgify, CS50P Week3, ⭐⭐⭐⭐)**: 读 CSV 清洗数据后写回 —— 为 Day13/16 文件+CSV 做铺垫。