"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 循环 + in + append]
[预计完成时间: 20 分钟]

题目描述:
    给定一个列表,去掉所有重复元素,保留第一次出现的元素,
    并打印结果。要求用循环和 in 判断实现,不使用 set。

示例:
    >>> nums = [1, 2, 3, 2, 4, 3, 5]
    pass
    输出: [1, 2, 3, 4, 5]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
nums = [1, 2, 3, 2, 4, 3, 5]
result = []
for item in nums:
    if item not in result:
        result.append(item)
print("去重后:", result)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有重复
    t1 = [1, 2, 3, 2, 4, 3, 5]
    r1 = []
    for x in t1:
        if x not in r1:
            r1.append(x)
    print(f"测试1: {r1}")  # [1,2,3,4,5]

    # 测试 2: 全部相同
    t2 = [7, 7, 7]
    r2 = []
    for x in t2:
        if x not in r2:
            r2.append(x)
    print(f"测试2: {r2}")  # [7]

    # 测试 3: 空列表
    t3 = []
    r3 = []
    for x in t3:
        if x not in r3:
            r3.append(x)
    print(f"测试3: {r3}")  # []
