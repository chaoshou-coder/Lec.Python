"""
[难度: ⭐⭐⭐]
[所属知识点: 方差解释率 / 主成分选择]
[预计完成时间: 15 分钟]

题目描述:
  用 load_iris 的 X,PCA(n_components=4) 不降维,
  输出 explained_variance_ratio_。
  计算累计方差贡献率,找出至少保留 95% 方差
  的最小主成分数。

示例:
    >>> ratio, n_components = variance_threshold()
    >>> n_components
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ================
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


def variance_threshold():
    # 加载数据
    iris = load_iris()
    X = iris.data
    # PCA 不降维
    pca = PCA(n_components=4)
    pca.fit(X)
    ratio = pca.explained_variance_ratio_
    # 累计方差贡献率
    cumsum = np.cumsum(ratio)
    print("累计方差贡献率:", cumsum)
    # 找至少保留 95% 的最小主成分数
    n_components = np.argmax(cumsum >= 0.95) + 1
    return ratio, n_components


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 方差比长度为 4
    ratio, n_components = variance_threshold()
    print("explained_variance_ratio_:", ratio)
    print("保留 95% 方差的最小主成分数:",
          n_components)
    assert len(ratio) == 4

    # 测试 2: 最小主成分数应为 2
    assert n_components == 2
    print("测试通过!")
