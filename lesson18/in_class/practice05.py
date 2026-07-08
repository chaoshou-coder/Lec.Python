"""
[难度: ⭐⭐⭐]
[所属知识点: train_test_split + 分层直觉]
[预计完成时间: 15 分钟]

题目: 从 sklearn.datasets.load_iris 加载数据,
分别按 test_ratio = 0.1/0.2/0.3/0.4/0.5 切分,
使用 sklearn.model_selection.train_test_split,
设 stratify=y 以保证每类比例,
统计每种比例下训练集和测试集的样本总数,
返回一个 pandas DataFrame,
列名为("测试比例","训练集样本数","测试集样本数"),共 5 行。

提示: 确保 stratify=y 使各类样本按比例切分,避免不均衡。

示例:
    >>> df = analyze_split_ratios()
    >>> df.shape
    (5, 3)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 调用函数并打印结果
    df = analyze_split_ratios()
    print(df)

    # 验证 DataFrame 形状为 (5, 3)
    assert df.shape == (5, 3), "形状应为 (5, 3)"

    # 验证测试比例列
    assert list(df["测试比例"]) == [0.1, 0.2, 0.3, 0.4, 0.5]

    # 验证训练集+测试集总数恒为 150
    total = df["训练集样本数"] + df["测试集样本数"]
    assert total.eq(150).all(), "训练集+测试集总数应为 150"
