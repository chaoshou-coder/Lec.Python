"""
[难度: ⭐]
[所属知识点: SVC 基本使用]
[预计完成时间: 5 分钟]

题目: 使用 sklearn.datasets.load_iris 加载数据集,
取出前 100 条样本进行二分类(山鸢尾 vs 杂色鸢尾)。
用 SVC() 默认参数训练模型,输出测试集准确率。
数据用 train_test_split(random_state=42) 划分,
测试集占比 0.3。

示例:
    >>> # 运行后输出类似:
    >>> # 测试集准确率: 1.0
"""

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. 加载 iris 数据集,取前 100 条
# 2. 用 train_test_split 划分,test_size=0.3,
#    random_state=42
# 3. 创建 SVC() 模型并训练
# 4. 输出测试集准确率
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况 — 前 100 条二分类
    # 测试 2: 检查准确率是否在合理范围 (>0.9)
    pass
