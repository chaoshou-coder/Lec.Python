"""
[难度: ⭐⭐⭐]
[所属知识点: roc_auc_score]
[预计完成时间: 15 分钟]

题目: 使用 sklearn.datasets.make_classification 生成二分类数据
      (n_samples=500, n_classes=2, random_state=42),
      用 LogisticRegression 训练后预测概率 predict_proba()[:, 1],
      再用 roc_auc_score 计算 AUC 值。

示例:
    >>> # AUC 约 0.92~0.95
"""
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
X, y = make_classification(
    n_samples=500, n_classes=2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 注意:roc_auc_score 需要概率,不是类别标签
y_prob = model.predict_proba(X)[:, 1]
auc = roc_auc_score(y, y_prob)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:AUC 在 [0, 1] 范围内
    print(f"AUC = {auc:.4f}")
    assert 0.0 <= auc <= 1.0
    # 测试 2:AUC 应明显优于随机(> 0.8)
    assert auc > 0.8, f"AUC {auc} 过低,模型可能有问题"
    print("全部测试通过!")
