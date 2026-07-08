"""
[难度: ⭐⭐⭐]
[所属知识点: 循环累加与比较]
[预计完成时间: 15 分钟]

题目描述:
  给定一组成绩 [85, 92, 78, 90, 88],
  使用循环累加求总分,遍历求最高分和最低分,
  最后计算平均分(总分 / 个数)。
  要求: 不能使用 sum()、max()、min() 函数,
  全部用循环和条件判断实现。

示例:
    >>> 成绩 [85, 92, 78, 90, 88]
    总分: 433,平均分: 86.6,最高分: 92,最低分: 78
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
scores = [85, 92, 78, 90, 88]
total = 0
highest = scores[0]
lowest = scores[0]
for score in scores:
    total += score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
average = total / len(scores)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 普通成绩
    scores_1 = [85, 92, 78, 90, 88]
    t_1 = 0
    h_1 = scores_1[0]
    l_1 = scores_1[0]
    for s in scores_1:
        t_1 += s
        if s > h_1:
            h_1 = s
        if s < l_1:
            l_1 = s
    a_1 = t_1 / len(scores_1)
    print(f"总分: {t_1},平均分: {a_1},"
          f"最高分: {h_1},最低分: {l_1}")
    assert t_1 == 433
    assert h_1 == 92
    assert l_1 == 78

    # 测试 2: 只有一个成绩
    scores_2 = [100]
    t_2 = 0
    h_2 = scores_2[0]
    l_2 = scores_2[0]
    for s in scores_2:
        t_2 += s
        if s > h_2:
            h_2 = s
        if s < l_2:
            l_2 = s
    a_2 = t_2 / len(scores_2)
    print(f"总分: {t_2},平均分: {a_2},"
          f"最高分: {h_2},最低分: {l_2}")
    assert t_2 == 100
    assert h_2 == 100
    assert l_2 == 100

    # 测试 3: 有零分
    scores_3 = [0, 60, 90, 75, 100]
    t_3 = 0
    h_3 = scores_3[0]
    l_3 = scores_3[0]
    for s in scores_3:
        t_3 += s
        if s > h_3:
            h_3 = s
        if s < l_3:
            l_3 = s
    a_3 = t_3 / len(scores_3)
    print(f"总分: {t_3},平均分: {a_3},"
          f"最高分: {h_3},最低分: {l_3}")
    assert t_3 == 325
    assert h_3 == 100
    assert l_3 == 0

    print("所有测试通过!")
