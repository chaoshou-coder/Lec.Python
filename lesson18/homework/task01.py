"""
[难度: ⭐⭐⭐]
[所属知识点: 过拟合 / 欠拟合曲线直觉]
[预计完成时间: 15 分钟]

机器学习中,训练准确率与测试准确率之间的差值可以反映
模型的过拟合程度。请你实现 find_max_gap() 函数, 完成
以下模拟实验:
1. 生成训练集大小 n 的序列: 从 10 到 100, 步长为 10。
2. 假设训练准确率 train = 1 - exp(-n / 30),
   测试准确率 test = 0.8 * (1 - exp(-n / 50))。
3. 计算每个 n 对应的训练-测试准确率差值。
4. 返回差值最大的那个 n。

提示: 使用 numpy.exp 计算指数。

示例:
    >>> n_max = find_max_gap()
    >>> isinstance(n_max, (int, numpy.integer))
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 调用函数并打印结果
    n_max = find_max_gap()
    print("差值最大的 n =", n_max)

    # 测试 2: 验证返回值在合法范围内
    assert 10 <= n_max <= 100, "n_max 应在 10~100 之间"

    # 测试 3: 底层数组正确性验证
    # ns 从 10 到 100 步长 10
    # train = 1 - numpy.exp(-ns / 30)
    # test = 0.8 * (1 - numpy.exp(-ns / 50))
    # return ns[numpy.argmax(train - test)]

    # 测试 4: 边界测试 — 代码不应因 import 报错而无法运行
    import numpy
    ns = numpy.arange(10, 101, 10)
    train = 1 - numpy.exp(-ns / 30)
    test = 0.8 * (1 - numpy.exp(-ns / 50))
    expected = ns[numpy.argmax(train - test)]
    assert n_max == expected, f"期望 {expected}, 实际 {n_max}"
    print("所有测试通过!")
    pass
