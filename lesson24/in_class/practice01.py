"""
[难度: ⭐]
[所属知识点: accuracy_score]
[预计完成时间: 5 分钟]

题目: 给定 y_true = [0, 1, 1, 0, 1, 0, 1, 1],
      y_pred = [0, 1, 0, 0, 1, 0, 1, 1],
      使用 sklearn.metrics.accuracy_score 计算准确率,
      并手动验证准确率 = 正确数 / 总数。

示例:
    >>> # 准确率应为 0.875 (7 个正确 / 8 个总数)
"""
from sklearn.metrics import accuracy_score

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
y_true = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1]

# 计算准确率
acc = accuracy_score(y_true, y_pred)

# 手动验证:正确数 / 总数
correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
total = len(y_true)
acc_manual = correct / total

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:准确率应为 0.875
    print(f"accuracy_score 结果: {acc}")
    assert acc == 0.875, f"期望 0.875,实际 {acc}"
    # 测试 2:手动计算与 sklearn 结果一致
    print(f"手动计算结果: {acc_manual}")
    assert acc == acc_manual, "手动计算应与 sklearn 一致"
    print("全部测试通过!")
