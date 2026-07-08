"""
[难度: ⭐⭐⭐]
[所属知识点: Dataset / DataLoader / 偏好数据]
[预计完成时间: 15 分钟]

用 datasets 构造 PreferenceDataset(Dataset)：
- 存 prompt / chosen / rejected 三个字段
- __len__ / __getitem__
- 用 DataLoader 测试 batch 输出

教学点：DPO 输入就是这种 prompt + chosen + rejected
三联对，HF trl 的 DPOTrainer 底层读的就是此类数据。

示例:
    >>> ds = PreferenceDataset(3)
    >>> loader = DataLoader(ds, batch_size=2)
    >>> batch = next(iter(loader))
    >>> batch['prompt']
    ['问题 0', '问题 1']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: Dataset 长度
    # ds = PreferenceDataset(5)
    # assert len(ds) == 5
    # print("测试 1 通过: len =", len(ds))

    # 测试 2: DataLoader batch
    # loader = DataLoader(ds, batch_size=2)
    # batch = next(iter(loader))
    # assert 'prompt' in batch and 'chosen' in batch
    # print("测试 2 通过: batch keys =", list(batch.keys()))
    pass
