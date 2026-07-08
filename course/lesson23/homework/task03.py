"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 聚类模型评估综合]
[预计完成时间: 20 分钟]

题目描述:
  封装一个函数 clustering_report(X, k_range)——
  对输入数据 X,在 k_range 范围内用 KMeans 聚类,
  计算每个 k 的 inertia 和 silhouette_score,
  返回最佳 k(轮廓系数最高)和
  对应的所有指标 DataFrame。

示例:
    >>> from sklearn.datasets import make_blobs
    >>> X, _ = make_blobs(
    ...     n_samples=200, centers=3,
    ...     random_state=42
    ... )
    >>> best_k, df = clustering_report(X, [2,3,4,5])
    >>> best_k
    3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def clustering_report(X, k_range):
    records = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42)
        labels = km.fit_predict(X)
        inertia = km.inertia_
        score = silhouette_score(X, labels)
        records.append({
            'k': k,
            'inertia': inertia,
            'silhouette_score': score
        })
    df = pd.DataFrame(records)
    # 轮廓系数最高的 k 为最佳
    best_idx = df['silhouette_score'].idxmax()
    best_k = int(df.loc[best_idx, 'k'])
    return best_k, df


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from sklearn.datasets import make_blobs
    # 测试 1: 3 簇数据,最佳 k 应为 3
    X, _ = make_blobs(
        n_samples=200, centers=3, random_state=42
    )
    best_k, df = clustering_report(X, [2, 3, 4, 5])
    print("指标表:\n", df)
    print("最佳 k =", best_k)
    assert best_k == 3

    # 测试 2: DataFrame 列完整
    assert list(df.columns) == [
        'k', 'inertia', 'silhouette_score'
    ]
    assert len(df) == 4
    print("测试通过!")
