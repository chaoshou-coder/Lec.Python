"""
[难度: ⭐⭐⭐]
[所属知识点: if/elif/else 与逻辑运算]
[预计完成时间: 15 分钟]

题目描述:
  输入一个成绩(0~100 之间的整数),输出对应的等级:
    90~100 → A
    80~89  → B
    70~79  → C
    60~69  → D
    0~59   → E
  如果输入不在 0~100 范围内,输出 "成绩无效"。

示例:
    >>> 输入: 95
    A
    >>> 输入: 82
    B
    >>> 输入: 105
    成绩无效
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: A 等级
    score = 95
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "E"
        print(grade)
    else:
        print("成绩无效")
    assert grade == "A"

    # 测试 2: C 等级
    score = 73
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "E"
        print(grade)
    else:
        print("成绩无效")
    assert grade == "C"

    # 测试 3: 成绩无效
    score = 105
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "E"
        print(grade)
    else:
        grade = "成绩无效"
        print(grade)
    assert grade == "成绩无效"

    print("所有测试通过!")
