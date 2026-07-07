"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 循环、in 运算符、append()]
[预计完成时间: 20 分钟]

题目描述:
  给定一个包含重复元素的列表,编写函数 remove_dup(lst),
  去掉所有重复元素,只保留第一次出现的元素,
  并返回新列表。要求使用循环、in 和 append() 实现。

示例:
    >>> [1, 2, 1, 3, 2, 4] → [1, 2, 3, 4]
    >>> ["a", "b", "a", "c"] → ["a", "b", "c"]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def remove_dup(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 普通整数列表
    data_1 = [1, 2, 1, 3, 2, 4]
    result_1 = remove_dup(data_1)
    print(result_1)
    assert result_1 == [1, 2, 3, 4]

    # 测试 2: 字符列表
    data_2 = ["a", "b", "a", "c"]
    result_2 = remove_dup(data_2)
    print(result_2)
    assert result_2 == ["a", "b", "c"]

    # 测试 3: 无重复元素
    data_3 = [1, 2, 3]
    result_3 = remove_dup(data_3)
    print(result_3)
    assert result_3 == [1, 2, 3]

    # 测试 4: 空列表
    data_4 = []
    result_4 = remove_dup(data_4)
    print(result_4)
    assert result_4 == []

    # 测试 5: 全部相同
    data_5 = [7, 7, 7]
    result_5 = remove_dup(data_5)
    print(result_5)
    assert result_5 == [7]

    print("所有测试通过!")
