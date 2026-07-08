"""
[难度: ⭐⭐]
[所属知识点: confusion_matrix 解读]
[预计完成时间: 10 分钟]

题目: 给定 y_true = [0, 1, 1, 0, 1, 0, 1, 1],
      y_pred = [0, 1, 0, 0, 1, 0, 1, 1],
      使用 confusion_matrix 得到 2×2 矩阵,
      并创建函数 parse_cm(cm) 返回字典:
      {"TN": ..., "FP": ..., "FN": ..., "TP": ...}。

示例:
    >>> # TN=3, FP=0, FN=1, TP=4
"""
from sklearn.metrics import confusion_matrix

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
y_true = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)


def parse_cm(cm):
    """从 2×2 混淆矩阵中解析 TN/FP/FN/TP"""
    tn, fp, fn, tp = cm.ravel()
    return {"TN": int(tn), "FP": int(fp),
            "FN": int(fn), "TP": int(tp)}


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:混淆矩阵形状
    print(f"混淆矩阵:\n{cm}")
    assert cm.shape == (2, 2)
    # 测试 2:parse_cm 返回正确字典
    result = parse_cm(cm)
    print(f"解析结果: {result}")
    assert result == {"TN": 3, "FP": 0, "FN": 1, "TP": 4}
    print("全部测试通过!")
