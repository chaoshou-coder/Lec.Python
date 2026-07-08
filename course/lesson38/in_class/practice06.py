"""
[难度: ⭐⭐⭐⭐]
[所属知识点: CLM 数据准备流水线]
[预计完成时间: 20 分钟]

实现 prepare_data_for_clm 函数:
  1. 对 raw_texts 列表逐条 tokenize
  2. 将所有 token 拼接后按 max_len 切 block
  3. 构造 input_ids 与 labels (CLM 中 labels = input_ids)
  4. 返回 DataLoader,方便训练循环直接迭代

示例:
    >>> dl = prepare_data_for_clm(
    ...     tokenizer, ["文本1", "文本2"], max_len=128
    ... )
    >>> batch = next(iter(dl))
    >>> print(batch["input_ids"].shape)
    torch.Size([4, 128])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
from torch.utils.data import Dataset, Dataset as BaseDataset
from torch.utils.data import DataLoader


class BlockDataset(Dataset):
    """固定长度的 block 数据集。"""

    def __init__(self, input_ids, labels, block_size):
        self.input_ids = input_ids
        self.labels = labels
        self.block_size = block_size

    def __len__(self):
        # 学员: 计算可切出的 block 数量
        return 0  # 替换为 pass 并实现
        pass

    def __getitem__(self, idx):
        start = idx * self.block_size
        end = start + self.block_size
        return {
            "input_ids": self.input_ids[start:end],
            "labels": self.labels[start:end],
        }


def prepare_data_for_clm(
    tokenizer, raw_texts, max_len=128, batch_size=4
):
    """CLM 数据准备流水线。"""
    # 学员: 逐条 tokenize 并拼接所有 token
    all_ids = []  # 替换为 pass 并实现
    pass

    # 学员: 按 max_len 切 block,丢弃尾部不足部分
    input_ids = None  # 替换为 pass 并实现
    pass
    labels = input_ids.clone()

    # 学员: 构造 BlockDataset 与 DataLoader
    ds = BlockDataset(input_ids, labels, max_len)
    dl = DataLoader(ds, batch_size=batch_size, shuffle=True)
    return dl


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 不联网: 用模拟 tokenizer
    class FakeTokenizer:
        def __call__(self, text, **kw):
            ids = [ord(c) % 100 for c in text]
            return {"input_ids": ids}

    tok = FakeTokenizer()
    texts = ["机器学习很有趣", "深度学习是机器学习的一个分支"]

    dl = prepare_data_for_clm(
        tok, texts, max_len=8, batch_size=2
    )

    # 测试 1: DataLoader 可迭代
    batch = next(iter(dl))
    assert "input_ids" in batch
    assert "labels" in batch

    # 测试 2: 形状为 [batch_size, max_len]
    assert batch["input_ids"].shape == (2, 8)
    assert batch["labels"].shape == (2, 8)

    # 测试 3: labels 与 input_ids 相等 (CLM)
    assert torch.equal(batch["input_ids"], batch["labels"])

    print("batch shape:", batch["input_ids"].shape)
    print("流水线验证通过")
