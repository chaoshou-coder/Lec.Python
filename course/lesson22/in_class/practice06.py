"""
[难度: ⭐⭐⭐]
[所属知识点: n_estimators 调参]
[预计完成时间: 15 分钟]

题目: 使用 load_iris 全套数据(3 分类),
训练 GradientBoostingClassifier,
让 n_estimators 分别取以下值:
  [10, 30, 50, 100, 200]

random_state=42, 数据用
train_test_split(random_state=42) 划分,
测试集占比 0.3。

输出每种 n_estimators 下的测试集准确率,
观察准确率随树数量增加的趋势。

示例:
    >>> # 运行后输出类似:
    >>> # n_estimators= 10, 准确率: 0.9333
    >>> # n_estimators= 30, 准确率: 0.9556
    >>> # n_estimators= 50, 准确率: 0.9556
    >>> # n_estimators=100, 准确率: 0.9778
    >>> # n_estimators=200, 准确率: 0.9778
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. 加载 iris 数据并划分
# 2. 循环 n_estimators 列表
# 3. 每种参数训练并输出准确率
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: n_estimators=10 时准确率应 > 0.85
    # 测试 2: 随着 n_estimators 增大,
    #    准确率应整体呈上升趋势
    pass
