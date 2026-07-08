"""
[难度: ⭐]
[所属知识点: tokenizer 基础]
[预计完成时间: 5 分钟]

用 AutoTokenizer 加载 Qwen2-0.5B-Instruct 分词器,
对 "你好,世界" 进行 encode,打印 token id 列表,
再 decode 还原,验证分词与还原的一致性。

注意: 需要联网下载模型 (首次运行自动缓存到本地)。

示例:
    >>> tokens = tokenizer.encode("你好,世界")
    >>> print(tokens)
    [xxx, xxx, ...]
    >>> print(tokenizer.decode(tokens))
    '你好,世界'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from transformers import AutoTokenizer

# 需要联网下载模型 (首次运行自动缓存)
tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct"
)

text = "你好,世界"

# 学员: 调用 tokenizer.encode 得到 token id 列表
input_ids = None  # 替换为 pass 并实现
pass

# 学员: 调用 tokenizer.decode 将 id 列表还原为文本
restored = ""  # 替换为 pass 并实现
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 编码结果应为非空列表
    assert isinstance(input_ids, list), "encode 应返回 list"
    assert len(input_ids) > 0, "encode 结果不能为空"

    # 测试 2: 解码还原后应与原文本一致
    assert restored == text, (
        f"decode 还原失败: 期望 '{text}', 实际 '{restored}'"
    )
    print("编码结果:", input_ids)
    print("还原文本:", restored)
    print("token 数:", len(input_ids))
