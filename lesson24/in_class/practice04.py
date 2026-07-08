"""
[难度: ⭐⭐]
[所属知识点: cross_val_score]
[预计完成时间: 10 分钟]

题目: 加载 sklearn.datasets.load_iris 数据,
      使用 LogisticRegression(max_iter=200) 进行 5 折交叉验证,
      输出每折准确率以及均值 ± 标准差。

示例:
    >>> # 每折准确率约 0.93~1.00,均值约 0.97
"""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)

mean_score = scores.mean()
std_score = scores.std()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:共 5 个分数
    print(f"每折准确率: {scores}")
    assert len(scores) == 5
    # 测试 2:均值在合理范围(> 0.9)
    print(f"均值: {mean_score:.4f},标准差: {std_score:.4f}")
    assert mean_score > 0.9
    print("全部测试通过!")
