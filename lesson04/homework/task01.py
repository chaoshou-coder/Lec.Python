"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 切片与循环]
[预计完成时间: 20 分钟]

题目描述:
  编写一个函数 list_to_2d(lst),将一维列表按每 3 个元素
  一组切分成二维列表。若最后一组不足 3 个,也作为一组。
  要求使用切片和循环实现。

示例:
    >>> [1, 2, 3, 4, 5, 6, 7] → [[1, 2, 3], [4, 5, 6], [7]]
    >>> [1, 2, 3] → [[1, 2, 3]]
    >>> [] → []
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def list_to_2d(lst):
    result = []
    i = 0
    while i < len(lst):
        result.append(lst[i:i + 3])
        i += 3
    return result

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 刚好分完
    data_1 = [1, 2, 3, 4, 5, 6]
    result_1 = list_to_2d(data_1)
    print(result_1)
    assert result_1 == [[1, 2, 3], [4, 5, 6]]

    # 测试 2: 最后一组不足 3 个
    data_2 = [1, 2, 3, 4, 5, 6, 7]
    result_2 = list_to_2d(data_2)
    print(result_2)
    assert result_2 == [[1, 2, 3], [4, 5, 6], [7]]

    # 测试 3: 空列表
    data_3 = []
    result_3 = list_to_2d(data_3)
    print(result_3)
    assert result_3 == []

    # 测试 4: 刚好 1 组
    data_4 = [10, 20, 30]
    result_4 = list_to_2d(data_4)
    print(result_4)
    assert result_4 == [[10, 20, 30]]

    print("所有测试通过!")
