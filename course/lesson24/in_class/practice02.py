"""
[难度: ⭐⭐]
[所属知识点: precision_score, recall_score, f1_score]
[预计完成时间: 10 分钟]

题目: 给定 y_true = [0, 1, 1, 0, 1, 0, 1, 1],
      y_pred = [0, 1, 0, 0, 1, 0, 1, 1],
      分别计算 precision / recall / f1_score
      (average="binary")。
      在注释中解释:如果把所有样本都预测为正类,
      recall = 1 但 precision 会下降,请举例验证。

示例:
    >>> # precision ≈ 1.0, recall ≈ 0.8333, f1 ≈ 0.9091
"""
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
)

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
y_true = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1]

precision = precision_score(y_true, y_pred, average="binary")
recall = recall_score(y_true, y_pred, average="binary")
f1 = f1_score(y_true, y_pred, average="binary")

# 如果把所有样本都预测为正类:
# y_all_one = [1, 1, 1, 1, 1, 1, 1, 1]
# 此时 TP = 5 (真实为正的有 5 个), FP = 3 (真实为负的有 3 个)
# recall = TP / (TP + FN) = 5 / 5 = 1.0 (所有正样本都被找到)
# precision = TP / (TP + FP) = 5 / 8 = 0.625 (预测为正的里只有 5 个对)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:原始预测指标
    print(f"precision: {precision:.4f}")
    print(f"recall:    {recall:.4f}")
    print(f"f1:        {f1:.4f}")
    assert abs(precision - 1.0) < 1e-6
    assert abs(recall - 0.8333) < 1e-3
    # 测试 2:全部预测为正时 recall=1, precision 下降
    y_all_one = [1] * len(y_true)
    r = recall_score(y_true, y_all_one, average="binary")
    p = precision_score(y_true, y_all_one, average="binary")
    print(f"全正预测: recall={r}, precision={p}")
    assert r == 1.0
    assert abs(p - 0.625) < 1e-6
    print("全部测试通过!")
