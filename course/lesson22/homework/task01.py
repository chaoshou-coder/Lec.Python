"""
[难度: ⭐⭐⭐]
[所属知识点: 正则化参数 C]
[预计完成时间: 15 分钟]

题目: 使用 make_moons 生成非线性数据:
  n_samples=200, noise=0.2, random_state=42

用 SVC(kernel="rbf") 训练,
让正则化参数 C 分别取: 0.01, 1, 100。

数据用 train_test_split(random_state=42) 划分,
测试集占比 0.3。

输出三种 C 值的测试集准确率,
说明 C 越大 margin 越窄、容错越低,
在噪声数据上过大 C 可能过拟合。

示例:
    >>> # 运行后输出类似:
    >>> # C=0.01  准确率: 0.8833
    >>> # C=1     准确率: 0.9333
    >>> # C=100   准确率: 0.9167
"""

from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. make_moons 生成数据
# 2. train_test_split 划分
# 3. 循环 C in [0.01, 1, 100],
#    训练 SVC(kernel="rbf", C=C),
#    输出准确率
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: C=0.01 准确率应偏低(欠拟合)
    # 测试 2: C=1 准确率应较高
    pass
