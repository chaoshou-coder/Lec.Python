"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 特征选择 + 树模型]
[预计完成时间: 20 分钟]

题目: 在 iris 数据上,先用 RandomForest 得到特征重要性,
只保留重要性 > 0.1 的特征,重新训练 DecisionTree,
对比全特征和筛选后特征的准确率差异。
提示: 当阈值过高导致所有特征被过滤时,降低阈值。

示例:
    >>> run()
    全特征(4 个)测试准确率: 0.97
    筛选后特征(2 个): 花瓣长度 (cm), 花瓣宽度 (cm)
    筛选后测试准确率: 0.95
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # 1. 用 RandomForest 获取特征重要性
    rf = RandomForestClassifier(n_estimators=50, random_state=42)
    rf.fit(X_train, y_train)
    importances = rf.feature_importances_

    # 2. 选择重要性 > 0.1 的特征
    threshold = 0.1
    selected_idx = [i for i, v in enumerate(importances) if v > threshold]

    # 若全部过滤则降低阈值
    if len(selected_idx) == 0:
        threshold = 0.0
        selected_idx = list(range(len(importances)))

    selected_names = [iris.feature_names[i] for i in selected_idx]

    # 3. 全特征训练并评估
    dt_all = DecisionTreeClassifier(random_state=42)
    dt_all.fit(X_train, y_train)
    all_acc = dt_all.score(X_test, y_test)
    print(f"全特征({X_train.shape[1]} 个)测试准确率: {all_acc:.2f}")

    # 4. 筛选后特征训练并评估
    X_train_sel = X_train[:, selected_idx]
    X_test_sel = X_test[:, selected_idx]
    dt_sel = DecisionTreeClassifier(random_state=42)
    dt_sel.fit(X_train_sel, y_train)
    sel_acc = dt_sel.score(X_test_sel, y_test)

    print(f"筛选后特征({len(selected_idx)} 个): "
          f"{', '.join(selected_names)}")
    print(f"筛选后测试准确率: {sel_acc:.2f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 筛选后特征减少但准确率变化不大
    run()
