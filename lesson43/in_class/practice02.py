"""
[难度: ⭐⭐]
[所属知识点: GGUF 量化大小估算]
[预计完成时间: 10 分钟]

写一个函数 gguf_size(params_b, quant),
根据参数量与量化格式估算 GGUF 占用显存(GB)。
支持: {"Q2_K": 2.7, "Q4_K_M": 4.8,
       "Q8_0": 8.5, "F16": 16}(单位 bits/param),
公式: size_GB = params_b * bits_per_param / 8 / 1e9
测试 Qwen2-7B 在不同量化下的体积。

示例:
    >>> gguf_size(7e9, "Q4_K_M")
    4.2
"""

# ======================
# 学员代码区
# ======================
def gguf_size(params_b, quant):
    # 量化格式 -> 每参数 bits 映射
    # 返回 float GB,保留两位小数
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: Qwen2-7B Q4_K_M
    s1 = gguf_size(7e9, "Q4_K_M")
    print(f"7B Q4_K_M = {s1:.2f} GB")

    # 测试 2: 各种量化对比
    for q in ["Q2_K", "Q4_K_M", "Q8_0", "F16"]:
        s = gguf_size(7e9, q)
        print(f"7B {q:7s} = {s:.2f} GB")

    # 测试 3: 不支持的量化格式
    try:
        gguf_size(7e9, "FP8")
    except ValueError as e:
        print(f"测试3 -> 捕获异常: {e}")
