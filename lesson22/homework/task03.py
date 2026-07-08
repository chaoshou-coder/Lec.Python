"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 模型对比评估]
[预计完成时间: 20 分钟]

题目: 使用 load_iris 全套数据(3 分类),
对比两个模型:
  模型 A: GradientBoostingClassifier(
      n_estimators=100, random_state=42)
  模型 B: SVC(kernel="rbf", C=1.0)

训练策略: 用不同的 random_state 随机切分
(test_size=0.3),分别取 random_state=
[0, 1, 2],各训练 3 次。

输出:
  - 模型 A 3 次平均准确率 ± 标准差
  - 模型 B 3 次平均准确率 ± 标准差

在注释中分析: 在小样本、多分类场景下,
哪个模型更稳健(标准差更小)?

示例:
    >>> # 运行后输出类似:
    >>> # GBDT 平均准确率: 0.9644 ± 0.0148
    >>> # SVM  平均准确率: 0.9711 ± 0.0117
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. 加载 iris 数据
# 2. 循环 random_state = [0, 1, 2],
#    每次划分 + 训练两个模型,
#    记录准确率
# 3. 计算平均准确率和标准差并输出
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两个模型平均准确率都应 > 0.9
    # 测试 2: 标准差应 < 0.05(都较稳定)
    pass
