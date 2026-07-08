"""
[难度: ⭐⭐⭐]
[所属知识点: 核函数 / SVC]
[预计完成时间: 15 分钟]

题目: 使用 sklearn.datasets.make_moons 生成
非线性可分数据集:
  n_samples=200, noise=0.2, random_state=42

用 SVC 分别搭配三种核函数训练:
  kernel="linear"
  kernel="rbf"
  kernel="poly"

数据用 train_test_split(random_state=42) 划分,
测试集占比 0.3。
输出三种核函数的测试集准确率,
验证 RBF 核在非线性数据上的优势。

示例:
    >>> # 运行后输出类似:
    >>> # linear 核准确率: 0.8500
    >>> # rbf   核准确率: 0.9333
    >>> # poly  核准确率: 0.9167
"""

from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. make_moons 生成数据
# 2. train_test_split 划分
# 3. 循环 ["linear","rbf","poly"] 三种核,
#    分别训练 SVC(kernel=...),输出准确率
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: rbf 准确率应最高(非线性数据)
    # 测试 2: linear 准确率应低于 rbf
    pass
