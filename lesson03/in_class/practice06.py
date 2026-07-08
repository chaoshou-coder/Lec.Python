"""
[难度: ⭐⭐⭐]
[所属知识点: if/elif/else 与逻辑运算]
[预计完成时间: 15 分钟]

题目描述:
  输入一个年份,判断它是否为闰年。
  闰年规则:
    - 能被 4 整除但不能被 100 整除,或者
    - 能被 400 整除
  输出 "X 是闰年" 或 "X 不是闰年"。

示例:
    >>> 输入: 2000
    2000 是闰年
    >>> 输入: 1900
    1900 不是闰年
    >>> 输入: 2024
    2024 是闰年
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 能被 400 整除
    year = 2000
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
    assert ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    # 测试 2: 能被 100 整除但不能被 400 整除
    year = 1900
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
    assert not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    # 测试 3: 普通闰年
    year = 2024
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
    assert ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    # 测试 4: 非闰年
    year = 2023
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
    assert not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    print("所有测试通过!")
