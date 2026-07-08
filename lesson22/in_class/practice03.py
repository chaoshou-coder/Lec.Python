"""
[难度: ⭐⭐]
[所属知识点: GradientBoostingClassifier]
[预计完成时间: 10 分钟]

题目: 使用 load_iris 全套 150 条数据(3 分类),
训练 GradientBoostingClassifier,
参数: n_estimators=50, random_state=42。
数据用 train_test_split(random_state=42) 划分,
测试集占比 0.3。
输出:
  (a) 测试集准确率
  (b) staged_predict 返回的前 3 棵树在测试集
      上的预测值(取前 3 个样本打印观察)

示例:
    >>> # 运行后输出类似:
    >>> # 测试集准确率: 0.9556
    >>> # 前 3 棵树预测:
    >>> # 树 1: [2 2 1]
    >>> # 树 2: [2 2 1]
    >>> # 树 3: [2 2 0]
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. 加载 iris 全套数据
# 2. train_test_split 划分, test_size=0.3,
#    random_state=42
# 3. 创建模型, n_estimators=50, random_state=42
# 4. 训练后输出测试准确率
# 5. 用 staged_predict 取前 3 棵树的预测,
#    打印前 3 个样本
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 测试准确率应 > 0.9
    # 测试 2: staged_predict 应返回 50 个
    #    阶段的结果(n_estimators=50)
    pass
