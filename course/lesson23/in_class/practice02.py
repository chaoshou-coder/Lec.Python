"""
[难度: ⭐⭐]
[所属知识点: 肘部法则 / 最佳 K]
[预计完成时间: 10 分钟]

题目描述:
  用 make_blobs(n_samples=300, centers=3, random_state=0)
  生成数据,KMeans 的 k 从 1 到 8 遍历,
  计算每个 k 对应的 inertia。
  返回字典 {k: inertia},并找出肘部点
  (inertia 下降明显变缓的 k,直接返回 3)。

示例:
    >>> k_dict, elbow = find_elbow()
    >>> elbow
    3
    >>> 3 in k_dict
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def find_elbow():
    # 生成数据
    X, y = make_blobs(
        n_samples=300, centers=3, random_state=0
    )
    k_dict = {}
    for k in range(1, 9):
        km = KMeans(
            n_clusters=k, random_state=0
        )
        km.fit(X)
        k_dict[k] = km.inertia_
    # 找肘部:相邻 inertia 差值的拐点
    inertias = list(k_dict.values())
    diffs = np.diff(inertias)
    diffs2 = np.diff(diffs)
    # 二阶差分最大的点即为肘部(+2 因为
    # diff 后索引偏移 2)
    elbow = np.argmax(diffs2) + 2
    return k_dict, elbow


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 返回字典有 8 个 k
    k_dict, elbow = find_elbow()
    print("k -> inertia:", k_dict)
    print("肘部 k =", elbow)
    assert len(k_dict) == 8

    # 测试 2: 肘部应为 3
    assert elbow == 3
    print("测试通过!")
