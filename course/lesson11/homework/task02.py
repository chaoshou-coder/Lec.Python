"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 默认参数 + 循环 + 列表]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 filter_scores(scores, threshold=60),
    返回所有大于等于 threshold 的成绩列表,默认阈值 60。

示例:
    >>> filter_scores([55, 70, 85, 40, 90])
    [70, 85, 90]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def filter_scores(scores, threshold=60):
    result = []
    for s in scores:
        if s >= threshold:
            result.append(s)
    return result


# 示例调用
print("及格分数:", filter_scores([55, 70, 85, 40, 90]))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认阈值 60
    print(f"测试1: {filter_scores([55, 70, 85, 40, 90])}")

    # 测试 2: 自定义阈值
    print(f"测试2: {filter_scores([55, 70, 85], threshold=80)}")

    # 测试 3: 全部不及格
    print(f"测试3: {filter_scores([10, 20, 30])}")

    # 测试 4: 空列表
    print(f"测试4: {filter_scores([])}")
