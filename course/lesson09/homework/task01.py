"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 列表生成式 + 二维列表]
[预计完成时间: 20 分钟]

题目描述:
    给定二维列表 [[1,2,3],[4,5,6]],用列表生成式转置为
    [[1,4],[2,5],[3,6]],并打印结果。

示例:
    >>> matrix = [[1,2,3],[4,5,6]]
    输出: [[1, 4], [2, 5], [3, 6]]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("原矩阵:", matrix)
print("转置后:", transposed)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 2x3 矩阵
    m1 = [[1, 2, 3], [4, 5, 6]]
    t1 = [[row[i] for row in m1] for i in range(len(m1[0]))]
    print(f"测试1: {t1}")

    # 测试 2: 方阵 2x2
    m2 = [[1, 2], [3, 4]]
    t2 = [[row[i] for row in m2] for i in range(len(m2[0]))]
    print(f"测试2: {t2}")

    # 测试 3: 单行
    m3 = [[1, 2, 3]]
    t3 = [[row[i] for row in m3] for i in range(len(m3[0]))]
    print(f"测试3: {t3}")
