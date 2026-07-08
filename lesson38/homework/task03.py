"""
[难度: ⭐⭐⭐⭐]
[所属知识点: SFT label masking]
[预计完成时间: 20 分钟]

实现 SFTDataProcessor 类,含 tokenize_dataset 方法:
  - 对 raw_ds 中每条样本,拼接 instruction + input 作为
    prompt,output 作为 response
  - tokenize 拼接后的完整序列
  - 对 prompt 段 (assistant 之外) 的 label 填 -100,
    只有 response 段参与 loss 计算

提示: tokenizer 返回的 input_ids 是 list 或 tensor,
可通过切片将 prompt 对应位置的 labels 设为 -100。

示例:
    >>> proc = SFTDataProcessor(tokenizer, max_len=256)
    >>> out = proc.tokenize_dataset(raw_ds)
    >>> print(out[0]["labels"][:10])
    tensor([-100, -100, -100, ..., 456, 789])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
from torch.utils.data import Dataset


class SFTDataset(Dataset):
    """包装 tokenize 后的结果。"""

    def __init__(self, processed):
        self.processed = processed

    def __len__(self):
        return len(self.processed)

    def __getitem__(self, idx):
        return self.processed[idx]


class SFTDataProcessor:
    """SFT 数据处理器: 对 assistant 段外 label 填 -100。"""

    def __init__(self, tokenizer, max_len=256):
        self.tokenizer = tokenizer
        self.max_len = max_len

    def tokenize_dataset(self, raw_ds):
        """逐条 tokenize 并构造 labels。"""
        results = []
        for sample in raw_ds:
            instruction = sample["instruction"]
            input_text = sample.get("input", "") or ""
            output = sample["output"]

            # 学员: 拼接 prompt 与 response
            prompt = ""    # 替换为 pass 并实现
            response = ""  # 替换为 pass 并实现
            pass

            # 学员: 分别 tokenize prompt 与完整序列
            prompt_ids = []  # 替换为 pass 并实现
            full_ids = []    # 替换为 pass 并实现
            pass

            # 学员: 构造 labels,prompt 段填 -100
            labels = None  # 替换为 pass 并实现
            pass

            results.append({
                "input_ids": torch.tensor(full_ids),
                "labels": torch.tensor(labels),
            })

        return SFTDataset(results)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 不联网: 用模拟 tokenizer
    class FakeTokenizer:
        def __call__(self, text, **kw):
            ids = [ord(c) % 50 + 10 for c in text]
            return {"input_ids": ids}

    raw_ds = [
        {
            "instruction": "翻译",
            "input": "你好",
            "output": "Hello",
        },
        {
            "instruction": "总结",
            "input": "",
            "output": "天气好",
        },
    ]

    proc = SFTDataProcessor(FakeTokenizer(), max_len=256)
    ds = proc.tokenize_dataset(raw_ds)

    # 测试 1: 数据条数一致
    assert len(ds) == 2

    # 测试 2: prompt 段 labels 为 -100
    sample = ds[0]
    assert "input_ids" in sample and "labels" in sample
    assert sample["input_ids"].shape == sample["labels"].shape
    assert (sample["labels"][:3] == -100).all(), (
        "prompt 段 labels 应全为 -100"
    )

    # 测试 3: response 段 labels 不为 -100
    assert (sample["labels"][-3:] != -100).any(), (
        "response 段 labels 应保留真实 id"
    )

    print("labels 示例:", sample["labels"])
    print("SFT label masking 验证通过")
