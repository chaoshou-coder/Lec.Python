"""
[难度: ⭐⭐⭐]
[所属知识点: 聚类算法适用场景]
[预计完成时间: 15 分钟]

题目描述:
  用 make_circles(n_samples=300, factor=0.5,
  noise=0.05, random_state=42) 生成同心圆数据,
  分别用 KMeans(n_clusters=2) 和
  DBSCAN(eps=0.2, min_samples=5) 聚类。
  用 silhouette_score 对比两种方法,
  验证 DBSCAN 在非凸形状上更优。

示例:
    >>> km_score, db_score = circles_compare()
    >>> db_score > km_score
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_circles
from sklearn.metrics import silhouette_score


def circles_compare():
    # 生成同心圆数据
    X, y = make_circles(
        n_samples=300, factor=0.5,
        noise=0.05, random_state=42
    )
    # KMeans 聚类
    km = KMeans(n_clusters=2, random_state=42)
    km_labels = km.fit_predict(X)
    km_score = silhouette_score(X, km_labels)
    # DBSCAN 聚类
    db = DBSCAN(eps=0.2, min_samples=5)
    db_labels = db.fit_predict(X)
    db_score = silhouette_score(X, db_labels)
    return km_score, db_score


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: DBSCAN 分数高于 KMeans
    km_score, db_score = circles_compare()
    print("KMeans silhouette_score:", km_score)
    print("DBSCAN silhouette_score:", db_score)
    assert db_score > km_score

    # 测试 2: 两个分数都在 [-1, 1] 范围内
    assert -1 <= km_score <= 1
    assert -1 <= db_score <= 1
    print("测试通过!")
