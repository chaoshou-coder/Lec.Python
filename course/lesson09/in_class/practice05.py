"""
[难度: ⭐⭐⭐⭐]
[所属知识点: copy.copy() / copy.deepcopy()]
[预计完成时间: 20 分钟]

题目描述:
    给定列表 [1,2,3,[4,5]],分别用 copy.copy() 和 copy.deepcopy() 拷贝,
    然后修改原列表的嵌套列表元素,观察拷贝后的差异,并打印结果。

示例:
    >>> original = [1, 2, 3, [4, 5]]
    修改 original[3].append(6) 后
    copy 版嵌套列表会同步变化,deepcopy 版不会。
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import copy

original = [1, 2, 3, [4, 5]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
# 修改原列表的嵌套部分
original[3].append(6)
print("原列表:", original)
print("浅拷贝:", shallow)
print("深拷贝:", deep)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 浅拷贝会受影响
    import copy as cp
    orig = [1, 2, 3, [4, 5]]
    s = cp.copy(orig)
    orig[3].append(6)
    print(f"测试1 浅拷贝受影响: {s[3]}")

    # 测试 2: 深拷贝不受影响
    orig2 = [1, 2, 3, [4, 5]]
    d = cp.deepcopy(orig2)
    orig2[3].append(6)
    print(f"测试2 深拷贝不受影响: {d[3]}")

    # 测试 3: 替换外层元素不影响拷贝
    orig3 = [1, 2, 3, [4, 5]]
    s3 = cp.copy(orig3)
    orig3[0] = 99
    print(f"测试3 浅拷贝外层不变: {s3[0]}")
