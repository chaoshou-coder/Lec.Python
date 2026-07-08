"""
[难度: ⭐⭐⭐]
[所属知识点: 自定义 Dataset 类]
[预计完成时间: 15 分钟]

实现 AlpacaDataset,继承 torch.utils.data.Dataset,
从 Alpaca 格式的 list[dict] 加载数据。
__getitem__ 返回包含 input_ids / attention_mask / labels
的字典,方便 DataLoader 直接使用。

Alpaca 格式示例:
    {"instruction": "...", "input": "...", "output": "..."}

示例:
    >>> ds = AlpacaDataset(data, tokenizer)
    >>> sample = ds[0]
    >>> print(sample.keys())
    dict_keys(['input_ids', 'attention_mask', 'labels'])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
from torch.utils.data import Dataset


class AlpacaDataset(Dataset):
    """Alpaca 格式数据集。"""

    def __init__(self, data, tokenizer, max_len=256):
        self.data = data
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        # 学员: 拼接 instruction + input + output
        # 提示: f"{instruction}\n{input}\n{output}"
        text = ""  # 替换为 pass 并实现
        pass

        # 学员: 调用 tokenizer 进行编码,返回张量
        # 提示: padding="max_length", truncation=True
        enc = None  # 替换为 pass 并实现
        pass

        # 学员: 构建 labels (复制 input_ids)
        labels = None  # 替换为 pass 并实现
        pass

        return {
            "input_ids": enc["input_ids"].squeeze(),
            "attention_mask": enc["attention_mask"].squeeze(),
            "labels": labels.squeeze(),
        }


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 不联网: 用模拟 tokenizer 验证结构
    class FakeTokenizer:
        def __call__(self, text, **kw):
            ids = [1, 2, 3, 4, 5]
            n = len(ids)
            return {
                "input_ids": torch.tensor([ids]),
                "attention_mask": torch.tensor([[1] * n]),
            }

    data = [
        {
            "instruction": "翻译",
            "input": "你好",
            "output": "Hello",
        },
        {
            "instruction": "总结",
            "input": "今天天气好",
            "output": "天气好",
        },
    ]

    ds = AlpacaDataset(data, FakeTokenizer())

    # 测试 1: 长度匹配
    assert len(ds) == 2, f"期望 2, 实际 {len(ds)}"

    # 测试 2: 单样本结构正确
    sample = ds[0]
    assert "input_ids" in sample
    assert "attention_mask" in sample
    assert "labels" in sample
    assert sample["input_ids"].shape == sample["labels"].shape
    print("Dataset 结构正确, keys:", list(sample.keys()))
    print("input_ids shape:", sample["input_ids"].shape)
