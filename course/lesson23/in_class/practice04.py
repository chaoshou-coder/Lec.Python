"""
[难度: ⭐⭐]
[所属知识点: PCA]
[预计完成时间: 10 分钟]

题目描述:
  用 load_iris 数据,X 有 4 个特征。
  用 PCA(n_components=2) 降到二维,
  输出降维后数据的形状和 explained_variance_ratio_。

示例:
    >>> X_pca, ratio = iris_pca_2d()
    >>> X_pca.shape
    (150, 2)
    >>> len(ratio)
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


def iris_pca_2d():
    # 加载数据
    iris = load_iris()
    X = iris.data
    # PCA 降维
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    return X_pca, pca.explained_variance_ratio_


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 降维后形状为 (150, 2)
    X_pca, ratio = iris_pca_2d()
    print("降维后形状:", X_pca.shape)
    print("explained_variance_ratio_:", ratio)
    assert X_pca.shape == (150, 2)

    # 测试 2: 方差比有两个值且和 ≤ 1
    assert len(ratio) == 2
    assert sum(ratio) <= 1.0
    print("测试通过!")
