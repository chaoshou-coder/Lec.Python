"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 递归 + 列表]
[预计完成时间: 30 分钟]

题目描述:
    实现一个函数 flatten(nested_list),把任意嵌套的列表展平为一维列表。

示例:
    >>> flatten([1, [2, [3, 4]], 5])
    [1, 2, 3, 4, 5]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# 示例调用
data = [1, [2, [3, 4]], 5]
print("展平结果:", flatten(data))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 多层嵌套
    print(f"测试1: {flatten([1, [2, [3, 4]], 5])}")

    # 测试 2: 空列表
    print(f"测试2: {flatten([])}")

    # 测试 3: 无嵌套
    print(f"测试3: {flatten([1, 2, 3])}")

    # 测试 4: 深层嵌套
    print(f"测试4: {flatten([[[[1]]], 2])}")
