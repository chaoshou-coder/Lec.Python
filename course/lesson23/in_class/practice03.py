"""
[难度: ⭐⭐]
[所属知识点: silhouette_score]
[预计完成时间: 10 分钟]

题目描述:
  用 make_blobs(n_samples=200, centers=4,
  cluster_std=1.0, random_state=42) 生成数据,
  KMeans 取 k=2/3/4/5 分别计算 silhouette_score。
  返回最高分对应的 k,验证最佳 k=4。

示例:
    >>> best_k = silhouette_best_k()
    >>> best_k
    4
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score


def silhouette_best_k():
    # 生成数据
    X, y = make_blobs(
        n_samples=200, centers=4,
        cluster_std=1.0, random_state=42
    )
    best_score = -1
    best_k = 2
    for k in [2, 3, 4, 5]:
        km = KMeans(
            n_clusters=k, random_state=42
        )
        labels = km.fit_predict(X)
        score = silhouette_score(X, labels)
        print(f"k={k}, silhouette_score={score:.4f}")
        if score > best_score:
            best_score = score
            best_k = k
    return best_k


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 最佳 k 应为 4
    best_k = silhouette_best_k()
    print("最佳 k =", best_k)
    assert best_k == 4

    # 测试 2: 返回值在候选范围内
    assert best_k in [2, 3, 4, 5]
    print("测试通过!")
