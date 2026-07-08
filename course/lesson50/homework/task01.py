"""
[难度: ⭐⭐]
[所属知识点: 训练/测试集划分]
[预计完成时间: 10 分钟]

题目描述:
    编写 split_dataset(data, test_ratio=0.2) 函数,
    实现先打乱再划分:把输入列表按比例分成训练集和测试集。
    使用 random.shuffle,固定 random.seed(42) 保证可复现。
    打印两者数量。

    重要:**先用 dedup 去重,再划分** ——
    否则同一条数据可能同时出现在训练集和测试集,
    造成"数据泄露"。

示例:
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> train, test = split_dataset(data, test_ratio=0.2)
    >>> print(len(train), len(test))
    8 2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import random

    # 测试 1: 10 条数据,test_ratio=0.2
    print("--- 测试 1:10 条数据 ---")
    data = list(range(1, 11))
    random.seed(42)
    shuffled = data[:]
    random.shuffle(shuffled)
    split_idx = int(len(shuffled) * 0.8)
    train = shuffled[:split_idx]
    test = shuffled[split_idx:]
    print(f"训练集: {len(train)} 条,测试集: {len(test)} 条")
    assert len(train) == 8
    assert len(test) == 2
    # 应无交集
    assert len(set(train) & set(test)) == 0
    print("无数据泄露,通过")

    # 测试 2: 验证可复现性
    print("\n--- 测试 2:可复现性 ---")
    random.seed(42)
    s1 = data[:]
    random.shuffle(s1)
    random.seed(42)
    s2 = data[:]
    random.shuffle(s2)
    assert s1 == s2, "相同种子应产生相同结果"
    print("可复现性通过")
