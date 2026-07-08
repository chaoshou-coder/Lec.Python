"""
[难度: ⭐⭐⭐⭐]
[所属知识点: MinMaxScaler vs StandardScaler]
[预计完成时间: 20 分钟]

题目描述:
对比两种缩放器在异常值数据 [1,2,3,4,5,100] 上的效果,
用 sklearn 的 MinMaxScaler 和 StandardScaler 分别
fit_transform,返回两个结果。
观察哪个受异常值影响更大,在注释中说明原因。

原因说明:
    MinMax 将最小值映射到 0,最大值映射到 1,异常值 100 直接
    成为最大值,导致其余数据被压缩到接近 0 的区域;
    StandardScaler 基于均值和标准差,异常值虽然也会拉偏
    均值,但影响相对更小。

示例:
    >>> minmax 结果中前 5 个数都接近 0
    >>> standard 结果中数据分布更均匀
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def compare_scalers(values):
    """对比 MinMaxScaler 和 StandardScaler 在异常值上的效果"""
    data = np.array(values).reshape(-1, 1)

    minmax = MinMaxScaler()
    result_minmax = minmax.fit_transform(data).flatten()

    std = StandardScaler()
    result_std = std.fit_transform(data).flatten()

    return result_minmax, result_std


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 含异常值的数据
    values = [1, 2, 3, 4, 5, 100]
    r_minmax, r_std = compare_scalers(values)
    print("原始数据:    ", values)
    print("MinMax 结果: ", np.round(r_minmax, 4))
    print("Standard 结果:", np.round(r_std, 4))

    # 测试 2: 无异常值的均匀数据
    values2 = [10, 20, 30, 40, 50]
    r2_minmax, r2_std = compare_scalers(values2)
    print("\n无异常值数据:    ", values2)
    print("MinMax 结果:     ", np.round(r2_minmax, 4))
    print("Standard 结果:   ", np.round(r2_std, 4))
