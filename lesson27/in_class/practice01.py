"""
[难度: ⭐]
[所属知识点: 链式法则 / Sigmoid 导数]
[预计完成时间: 5 分钟]

反向传播需要激活函数的导数。Sigmoid 函数定义为
σ(x) = 1 / (1 + e^(-x))。请证明并实现:
σ'(x) = σ(x) * (1 - σ(x))。

任务: 分别用"直接求导公式"和"快捷公式"两种方式计算
sigmoid 的导数，验证它们结果完全一致。

示例:
    >>> x = np.array([0, 2, -1, 5])
    >>> sigmoid_derivative_direct(x)
    array([0.25, 0.10499359, 0.19661193, 0.00664806])
    >>> sigmoid_derivative_shortcut(x)
    array([0.25, 0.10499359, 0.19661193, 0.00664806])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import numpy as np

    # 测试 1: 常规输入
    x = np.array([0, 2, -1, 5])
    direct = None  # 学员实现后替换
    shortcut = None
    print("测试1 - x =", x)
    print("直接公式结果:", direct)
    print("快捷公式结果:", shortcut)
    print("两者是否一致:", np.allclose(direct, shortcut))

    # 测试 2: 边界情况 (大负数, 大正数)
    x_edge = np.array([-100, 100])
    print("\n测试2 - 边界 x =", x_edge)
    print("快捷公式结果:", None)  # 学员实现后替换
