"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Pipeline + SVC]
[预计完成时间: 20 分钟]

题目: 使用 load_iris 全套 150 条数据(3 分类),
用 sklearn Pipeline 将 StandardScaler 和 SVC
串联成一个流水线:
  Pipeline([
      ("scaler", StandardScaler()),
      ("svc", SVC())
  ])

数据用 train_test_split(random_state=42) 划分,
测试集占比 0.3。

输出:
  (a) Pipeline 方式的测试准确率
  (b) 不用 Pipeline,手动 StandardScaler 后再
      SVC 的测试准确率

对比两种方式准确率是否一致,
体会 Pipeline 的便利性。

示例:
    >>> # 运行后输出类似:
    >>> # Pipeline 准确率: 0.9778
    >>> # 手动 Scale 准确率: 0.9778
    >>> # 两种方式结果一致!
"""

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 1. 加载数据并划分
# 2. 方式 a: 构建 Pipeline,训练并输出准确率
# 3. 方式 b: 手动 scaler.fit_transform,
#    再 SVC 训练并输出准确率
# 4. 打印对比结论
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: Pipeline 准确率应 > 0.9
    # 测试 2: 两种方式准确率应相等(一致)
    pass
