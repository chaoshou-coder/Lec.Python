"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合(随机数 + 统计 + 广播)]
[预计完成时间: 30 分钟]

题目描述:
    综合运用 NumPy 的随机数、统计、广播完成以下任务:

    1. 用 np.random.randint 生成 5 名学生
       3 门课程的成绩(0~100),存入 5x3 数组
    2. 计算每名学生的平均分(广播)
    3. 计算每门课程的最高分
    4. 对所有成绩做 Z-score 标准化

    要求: 全部使用向量化运算,不出现 for 循环。

示例:
    >>> # 成绩表 shape=(5, 3)
    >>> print(scores.mean(axis=1))  # 学生平均
    [75.33 82.00 ...]
    >>> print(scores.max(axis=0))   # 课程最高
    [95 88 92]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np

# 任务 1: 生成随机成绩
# 提示: np.random.randint(0, 101, size=(5, 3))
# 设置随机种子保证可复现: np.random.seed(42)
scores = None

# 任务 2: 每名学生的平均分
# 提示: scores.mean(axis=1)
student_avg = None

# 任务 3: 每门课程的最高分
# 提示: scores.max(axis=0)
course_max = None

# 任务 4: Z-score 标准化
# 提示: (scores - scores.mean()) / scores.std()
normalized = None

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    print(f"成绩表(5 学生 x 3 课程):\n{scores}")
    print(f"学生平均分: {student_avg}")
    print(f"课程最高分: {course_max}")
    print(f"标准化后:\n{normalized}")
