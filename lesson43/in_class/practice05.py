"""
[难度: ⭐⭐⭐]
[所属知识点: 显存与量化推荐]
[预计完成时间: 15 分钟]

写一个函数 select_quantization(vram_gb, params_b),
根据可用显存(GB)和参数量(B)推荐量化格式。
规则(预留 2GB 给系统):
 - 可用 >= 参数量 * 16/8/1e9 -> F16
 - 可用 >= 参数量 * 8.5/8/1e9 -> Q8_0
 - 可用 >= 参数量 * 4.8/8/1e9 -> Q4_K_M
 - 可用 >= 参数量 * 2.7/8/1e9 -> Q2_K
 - 否则 -> "显存不足"
测试 8/16/24 GB + 7B 模型。

示例:
    >>> select_quantization(8, 7e9)
    Q4_K_M
"""

# ======================
# 学员代码区
# ======================
def select_quantization(vram_gb, params_b):
    # 预留 2GB 给系统
    # 从高到低判断可用显存
    # 返回推荐的量化字符串
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 8GB + 7B
    r1 = select_quantization(8, 7e9)
    print(f"8GB + 7B -> {r1}")

    # 测试 2: 16GB + 7B
    r2 = select_quantization(16, 7e9)
    print(f"16GB + 7B -> {r2}")

    # 测试 3: 24GB + 7B
    r3 = select_quantization(24, 7e9)
    print(f"24GB + 7B -> {r3}")

    # 测试 4: 显存不足
    r4 = select_quantization(2, 7e9)
    print(f"2GB + 7B -> {r4}")
