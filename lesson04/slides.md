# Day04 · 循环入门

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-03 已掌握变量、字符串、`if/elif/else`、比较与逻辑运算符、`in` 运算符
> 关键问题: 如何让电脑**重复**做一件事而不喊累?本节让代码拥有"循环"能力 —— 重复 + 终止条件 + 累加累乘,为后续"遍历列表/字典"打地基

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `if/elif/else` 的执行顺序是什么?`=` 和 `==` 的区别?"四年一闰百年不闰四百年又闰"怎么用 `and/or` 表达?
- **赏玩 demo**(3 分钟): 投影一行 `print("啪啪啪")`,"我要鼓 100 次掌,难道要复制 100 遍?"学员笑声中引出"循环"。现场改成 `for i in range(100): print("啪啪啪")`,一句话搞定。

---

## 1. 第一讲(15 分钟) —— `while` 循环

### 知识点 1.1 `while`:当条件成立就一直干

```python
# 打印 1 到 5
count = 1
while count <= 5:       # 冒号 + 缩进
    print(count)
    count += 1          # 没有这行就是死循环!
print("循环结束")
```

> 口诀:**while = 当...时,就继续**。先判断,再执行,每次执行完检查条件还成不成立。

### 知识点 1.2 死循环与终止条件

```python
# ❌ 死循环(永远不停)
# while True:
#     print("停不下来")

# ✅ 用 break 主动退出
while True:
    word = input("输入 quit 退出:")
    if word == "quit":
        break           # 立刻跳出整个循环
print("你退出了")
```

> 🔴 教学红线(忘记递增): 学员最常见的 bug 是 `while` 忘了写 `count += 1`,导致死循环。板书口诀:**while 三要素 —— 起始值、终止条件、递增步进,缺一不可**。

### 知识点 1.3 `break` 与 `continue`

```python
# break:彻底结束循环
for i in range(10):
    if i == 5:
        break           # 遇到 5 直接退出,后续不再执行
    print(i)            # 输出 0,1,2,3,4

# continue:跳过本次,继续下一趟
for i in range(10):
    if i % 2 == 0:
        continue        # 偶数跳过不打印
    print(i)            # 输出 1,3,5,7,9
```

> 区别:**break 是"辞职",continue 是"请一次假继续上班**"。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— `while` 循环打印 1 到 10(⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— `range` 步长:从 100 到 1 打印所有偶数(⭐,10 分钟)

> 巡场重点: 看学员是否漏了 `count += 1` 或 `count -= 1`;其次看 `range(100, 0, -2)` 的终止值应写成 `0` 而不是 `-1`(因为 `range` 左闭右开,`-1` 会包含 0)。

---

## 3. 第二讲(15 分钟) —— `for` 循环与 `range`

### 知识点 3.1 `for item in 序列`:遍历

```python
# 遍历字符串
for ch in "Python":
    print(ch)           # P y t h o n 各一行

# 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")
```

> `for` 循环最适合"**已知长度、要处理每一个元素**"的场景。

### 知识点 3.2 `range(start, stop, step)`:生成整数数列

```python
for i in range(5):
    print(i)            # 0,1,2,3,4

for i in range(1, 6):
    print(i)            # 1,2,3,4,5

for i in range(0, 10, 2):
    print(i)            # 0,2,4,6,8

for i in range(100, 0, -2):
    print(i)            # 100,98,...,2
```

> `range(start, stop, step)`:**从 start 开始(含),到 stop 结束(不含),每次跳 step**。没有循环对象时用 `range`,有循环对象直接 `for item in`。

### 知识点 3.3 累加器模式

```python
# 求 1 + 2 + ... + 100
total = 0                    # 1. 初始化为 0
for i in range(1, 101):
    total += i               # 2. 累加
print(total)                 # 5050

# 求奇数的乘积
product = 1                  # 1. 乘法的初始值为 1(不是 0!)
for i in range(1, 10, 2):
    product *= i
print(product)               # 945
```

> 🔴 教学红线(累乘初值为 1): 学员初学乘积时常把 `product = 0` 进来,导致结果恒为 0。口诀:**加 0 乘 1,初始值不要搞反**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 九九乘法表(嵌套 for + `end=''`)(⭐⭐⭐,20 分钟)
- 练习 4: `in_class/practice04.py` —— `while + //` 计算整数位数(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 3 学员常对 `end=''` 位置困惑 —— 应放在**内层 print** 控制列对齐,**外层 print()** 空一行换行。练习 4 提醒:``` 会向下取整,`1000 // 10 = 100`。

---

## 5. 第三讲(15 分钟) —— 循环控制 + 综合实战

### 知识点 5.1 鸡兔同笼:循环 + 条件合作

```python
# 35 个头,94 只脚,几只鸡几只兔?
for chicken in range(36):
    rabbit = 35 - chicken
    if chicken * 2 + rabbit * 4 == 94:
        print(f"鸡 {chicken} 只,兔 {rabbit} 只")
        break
```

### 知识点 5.2 菜单循环:死循环 + 分支退出

```python
while True:
    print("\n=== 简易菜单 ===")
    print("1. 喂食  2. 玩耍  3. 睡觉  0. 退出")
    choice = input("请选择:")
    if choice == "1":
        print("喂食中...")
    elif choice == "2":
        print("玩耍中...")
    elif choice == "3":
        print("睡觉中...")
    elif choice == "0":
        print("再见!")
        break
    else:
        print("无效输入,请重新选择")
```

> 这种 `while True + break` 模式是**菜单类程序的骨架**,几乎后续所有小项目都会复用。

### 知识点 5.3 字符串重复:`*` 运算符

```python
print("*" * 20)     # ********************
print(" " * 4 + "***")  # 三角形第一行
```

> `"*" * 20` 是字符串的乘法,**`"*" * n = 重复 n 倍"**,打印星号类图案时省掉循环。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 输入整数直到 0 结束,统计奇数均值与偶积(⭐⭐⭐⭐,20 分钟)
- 练习 6: `in_class/practice06.py` —— 打印星号三角形和 20 个星号(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 练习 5 提醒:**0 不参与统计**,且"没有奇数时均值不要除零"。练习 6 建议先画图再编码,**每行 = n 个空格 + m 个星号**,找出行号与 n/m 的数学关系。

---

## 7. 小项目:等腰三角形绘制(45 分钟)

- 项目: `mini_project/` 新建 `triangle_draw.py`
- 要求: 输入行数 n,打印由 `*` 组成的等腰三角形(n=5 示例):

```
    *
   ***
  *****
 *******
*********
```

- 规律:第 i 行(从 0 开始) = `(n - i - 1)` 个空格 + `(2 * i + 1)` 个星号

> 巡场重点: 学员常数错空格,"第一行 4 个空格" 应该对应 n=5,i=0 时 `n-i-1=4`。**先用代入法验证 i=0 和 i=n-1**。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. `while` 循环忘记递增步进,死循环
  2. 累乘初值写成 0,导致结果恒为 0
  3. `range(start, stop)` 的第二参数写错(如从 100 到 1 的偶数,`stop` 应写 `0`)
- **作业说明**: `homework/task01.py`(火箭发射倒计时 `time.sleep`)、`homework/task02.py`(猴子吃桃逆推),下节课前 10 分钟复盘。

---

## 易错点

1. **`while` 缺少递增步进会变死循环** —— 三要素:起始、终止、步进。
2. **累乘初始值为 1,累加初始值为 0** —— 初值为 0 则乘积恒 0。
3. **`range(start, stop)` 左闭右开** —— `stop` 不会被取到。
4. **`break` 跳出整个循环,`continue` 只是跳过本次** —— 两者作用域不同。
5. **嵌套循环缩进** —— 内层比外层多 4 格,搞错缩进就跨层。

## 延伸题

- **( camelCase, CS50P Week2, ⭐⭐)**: 把输入的 camelCase 转 snake_case —— 巩固 `for ch in s` + `.isupper()` + 条件分支。
- **(Vanity Plates, CS50P Week2, ⭐⭐⭐)**: 验证车牌格式合法性 —— 巩固 `isdigit` + `isalpha` + 切片组合。
- **(Nutrition Facts, CS50P Week2, ⭐⭐⭐)**: 输入水果名,查字典输出热量 —— 预告 Day06 字典。
