"""
[难度: ⭐⭐⭐⭐]
[所属知识点: K-Fold 交叉验证原理]
[预计完成时间: 20 分钟]

交叉验证是模型评估的重要方法。请你实现 my_kfold_split(X, y, k=5)
函数, 将数据集按顺序等分成 k 折, 依次以每份为测试集、其余
为训练集, 返回 (train_idx, test_idx) 索引对列表。

要求:
- X: array-like, shape (n_samples, n_features)
- y: array-like, shape (n_samples,)
- k: 整数, 折数
- 返回: 列表, 包含 k 个元素, 每个元素是 (train_idx, test_idx)
  的元组, 索引均为 numpy array

提示: 使用 numpy.arange 生成索引, 用 numpy.array_split
分成 k 份, 再用 numpy.concatenate 拼接训练集索引。
不要求打乱顺序, 按顺序切分即可。

示例:
    >>> from sklearn.datasets import load_iris
    >>> X, y = load_iris(return_X_y=True)
    >>> folds = my_kfold_split(X[:50], y[:50], k=5)
    >>> len(folds)
    5
    >>> sum(len(t) for _, t in folds)
    50
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from sklearn.datasets import load_iris
    import numpy

    X, y = load_iris(return_X_y=True)

    # 测试 1: 前 50 条数据, k=5
    # len(folds) == 5
    # 每折测试集长度为 10
    # 测试集长度之和为 50
    folds = my_kfold_split(X[:50], y[:50], k=5)
    assert len(folds) == 5, f"期望 5 折, 实际 {len(folds)}"
    for i, (train_idx, test_idx) in enumerate(folds):
        assert len(test_idx) == 10, \
            f"第{i}折测试集长度应为 10, 实际 {len(test_idx)}"
        assert isinstance(train_idx, numpy.ndarray)
        assert isinstance(test_idx, numpy.ndarray)
    assert sum(len(t) for _, t in folds) == 50
    print("测试 1 通过: k=5, 5 折, 每折测试集 10 条")

    # 测试 2: k=2
    # 2 折, 每折测试集 25 条
    folds2 = my_kfold_split(X[:50], y[:50], k=2)
    assert len(folds2) == 2
    for train_idx, test_idx in folds2:
        assert len(test_idx) == 25
    print("测试 2 通过: k=2, 每折测试集 25 条")

    # 测试 3: 边界 k=1
    # 1 折, 测试集大小 == n_samples (全部样本)
    folds1 = my_kfold_split(X[:50], y[:50], k=1)
    assert len(folds1) == 1
    train_idx, test_idx = folds1[0]
    assert len(test_idx) == 50, \
        f"k=1 时测试集应为全部 50 条, 实际 {len(test_idx)}"
    print("测试 3 通过: k=1, 测试集为全部样本")

    print("所有测试通过!")
    pass
