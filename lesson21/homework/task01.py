"""
[难度: ⭐⭐⭐]
[所属知识点: 特征重要性可视化]
[预计完成时间: 15 分钟]

题目: 用 RandomForestClassifier(n_estimators=50) 训练 iris 数据,
获取 feature_importances_,按重要性降序输出特征名及对应分数
(保留 3 位小数),并用柱状图展示。
提示: 可用 matplotlib 或直接打印 Series。

示例:
    >>> run()
    花瓣长度 (cm): 0.452
    花瓣宽度 (cm): 0.426
    花萼长度 (cm): 0.089
    花萼宽度 (cm): 0.033
    (柱状图显示)
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    # 1. 按重要性降序排序
    importances = model.feature_importances_
    pairs = sorted(
        zip(iris.feature_names, importances),
        key=lambda x: x[1],
        reverse=True,
    )

    names = [p[0] for p in pairs]
    scores = [p[1] for p in pairs]

    # 2. 打印特征重要性(保留 3 位小数)
    for name, score in pairs:
        print(f"{name}: {score:.3f}")

    # 3. 绘制柱状图
    plt.figure(figsize=(8, 4))
    plt.bar(names, scores, color="steelblue")
    plt.title("Iris 特征重要性(RandomForest)")
    plt.ylabel("重要性")
    plt.tight_layout()
    plt.savefig("feature_importance.png")
    print("柱状图已保存为 feature_importance.png")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 花瓣特征重要性应明显高于花萼特征
    run()
