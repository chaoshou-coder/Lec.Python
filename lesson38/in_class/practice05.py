"""
[难度: ⭐⭐⭐]
[所属知识点: datasets.map]
[预计完成时间: 15 分钟]

用 datasets.load_dataset 加载 tatsu-lab/alpaca 前 200 条,
编写 format_alpaca(sample) 将 instruction/input/output
拼接成统一文本字段,通过 ds.map 批量转换。

注意: 需要联网下载数据集 (首次运行自动缓存)。

示例:
    >>> def format_alpaca(sample):
    ...     ...
    >>> ds = ds.map(format_alpaca)
    >>> print(ds[0]["text"])
    '### Instruction:\n...'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from datasets import load_dataset

# 需要联网下载数据集
ds = load_dataset(
    "tatsu-lab/alpaca", split="train[:200]"
)


def format_alpaca(sample):
    """将单条 Alpaca 数据拼接为统一文本。"""
    instruction = sample["instruction"]
    input_text = sample.get("input", "") or ""
    output = sample["output"]

    # 学员: 拼接文本 (input 为空时忽略)
    # 提示: 参考 Alpaca prompt 模板格式
    text = ""  # 替换为 pass 并实现
    pass

    return {"text": text}


# 学员: 调用 ds.map 批量转换
ds = None  # 替换为 pass 并实现
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: map 后应新增 "text" 字段
    assert "text" in ds.column_names, (
        "map 后应包含 'text' 列"
    )

    # 测试 2: 每条 text 都应包含 instruction 与 output
    sample = ds[0]
    assert sample["instruction"] in sample["text"]
    assert sample["output"] in sample["text"]

    # 测试 3: 无 input 时不应出现 "### Input:"
    no_input = [x for x in ds if not x["input"]]
    if no_input:
        formatted = format_alpaca(no_input[0])["text"]
        assert "### Input:" not in formatted, (
            "input 为空时不应包含 Input 段"
        )

    print("数据集大小:", len(ds))
    print("字段:", ds.column_names)
    print("样本文本:\n", ds[0]["text"][:200])
