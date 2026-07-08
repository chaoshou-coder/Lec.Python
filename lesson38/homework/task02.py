"""
[难度: ⭐⭐⭐]
[所属知识点: prompt 构建]
[预计完成时间: 15 分钟]

编写 build_prompt(instruction, input_text) 函数,
将 Alpaca 格式拼成 chat template 字符串。
要求:
  - input_text 为空时只保留 instruction 段
  - 非空时包含 instruction 与 input 两段
  - 末尾追加 assistant 起始标记,提示模型开始生成

示例:
    >>> print(build_prompt("翻译", "你好"))
    '### Instruction:\n翻译\n\n### Input:\n你好\n\n### Response:\n'
    >>> print(build_prompt("总结", ""))
    '### Instruction:\n总结\n\n### Response:\n'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def build_prompt(instruction, input_text):
    """将 Alpaca 格式拼成 prompt 字符串。"""
    # 学员: 拼接 instruction 段
    # 提示: 参考下方模板,注意 input 为空时跳过 Input 段
    prompt = ""  # 替换为 pass 并实现
    pass
    return prompt


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 含 input 时应包含 Input 段
    p1 = build_prompt("翻译", "你好")
    assert "### Instruction:" in p1
    assert "### Input:" in p1
    assert "### Response:" in p1
    assert "翻译" in p1 and "你好" in p1

    # 测试 2: input 为空时不应包含 Input 段
    p2 = build_prompt("总结", "")
    assert "### Input:" not in p2
    assert "### Response:" in p2

    # 测试 3: 末尾应以 Response 段结尾 (提示模型生成)
    assert p1.strip().endswith("### Response:")
    assert p2.strip().endswith("### Response:")

    print("=== 测试 1 输出 ===")
    print(p1)
    print("=== 测试 2 输出 ===")
    print(p2)
    print("全部测试通过")
