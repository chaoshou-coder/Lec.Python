"""
[难度: ⭐⭐⭐]
[所属知识点: DBSCAN]
[预计完成时间: 15 分钟]

题目描述:
  用 make_moons(n_samples=200, noise=0.1,
  random_state=42) 生成数据,
  用 DBSCAN(eps=0.3, min_samples=5) 聚类。
  输出聚类标签(unique labels)和
  噪声点数(标签为 -1 的点)。

示例:
    >>> labels, noise_cnt = moons_dbscan()
    >>> noise_cnt >= 0
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons


def moons_dbscan():
    # 生成数据
    X, y = make_moons(
        n_samples=200, noise=0.1, random_state=42
    )
    # DBSCAN 聚类
    db = DBSCAN(eps=0.3, min_samples=5)
    labels = db.fit_predict(X)
    unique_labels = set(labels)
    noise_cnt = list(labels).count(-1)
    return unique_labels, noise_cnt


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 标签集合包含 -1(噪声)
    labels, noise_cnt = moons_dbscan()
    print("聚类标签:", labels)
    print("噪声点数:", noise_cnt)
    assert -1 in labels

    # 测试 2: 噪声点数非负且小于总数
    assert 0 <= noise_cnt <= 200
    print("测试通过!")
