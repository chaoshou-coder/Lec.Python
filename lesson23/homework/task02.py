"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 降维 + 聚类组合]
[预计完成时间: 20 分钟]

题目描述:
  用 load_iris 数据,先用 PCA(n_components=2) 降维,
  再用 KMeans(n_clusters=3) 聚类。
  计算降维后聚类的 silhouette_score,
  与直接在原始 4 维空间聚类的 silhouette_score 对比。

示例:
    >>> score_pca, score_raw = pca_then_kmeans()
    >>> score_pca > 0
    True
    >>> score_raw > 0
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


def pca_then_kmeans():
    # 加载数据
    iris = load_iris()
    X = iris.data
    # 原始空间 KMeans
    km_raw = KMeans(n_clusters=3, random_state=42)
    labels_raw = km_raw.fit_predict(X)
    score_raw = silhouette_score(X, labels_raw)
    # PCA 降维后 KMeans
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X)
    km_pca = KMeans(n_clusters=3, random_state=42)
    labels_pca = km_pca.fit_predict(X_pca)
    score_pca = silhouette_score(X_pca, labels_pca)
    return score_pca, score_raw


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两个分数均为正
    score_pca, score_raw = pca_then_kmeans()
    print("PCA 降维后 silhouette_score:",
          score_pca)
    print("原始空间 silhouette_score:",
          score_raw)
    assert score_pca > 0
    assert score_raw > 0

    # 测试 2: 两个分数都在合理范围内
    assert -1 <= score_pca <= 1
    assert -1 <= score_raw <= 1
    print("测试通过!")
