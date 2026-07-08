"""
[难度: ⭐]
[所属知识点: KMeans 基本使用]
[预计完成时间: 5 分钟]

题目描述:
  用 make_blobs(n_samples=150, centers=3, random_state=42)
  生成 3 个簇的数据,再用 KMeans(n_clusters=3) 聚类。
  输出聚类中心 cluster_centers_ 和 inertia_。

示例:
    >>> km = blobs_elbow_km()
    >>> centers, inertia = km
    >>> len(centers)
    3
    >>> inertia > 0
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def blobs_elbow_km():
    # 生成数据
    X, y = make_blobs(
        n_samples=150, centers=3, random_state=42
    )
    # KMeans 聚类
    km = KMeans(n_clusters=3, random_state=42)
    km.fit(X)
    return km.cluster_centers_, km.inertia_


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 聚类中心数量为 3
    centers, inertia = blobs_elbow_km()
    print("聚类中心形状:", centers.shape)
    print("聚类中心:\n", centers)
    assert len(centers) == 3

    # 测试 2: inertia 为正值
    print("inertia_:", inertia)
    assert inertia > 0
    print("测试通过!")
