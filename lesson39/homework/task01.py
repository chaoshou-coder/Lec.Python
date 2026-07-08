"""
[难度: ⭐⭐]
[所属知识点: 显存对比分析]
[预计完成时间: 10 分钟]

题目描述:
某基座模型某一层的权重维度 d=2048, 现以 r=32 做 LoRA 微调。
请实现 compare_memory(d, r),返回一个字典,包含:
  - lora_params:       LoRA 引入的参数量 (2 * d * r)
  - full_params:       原权重矩阵参数量 (d * d)
  - lora_memory_mb:    LoRA 优化器状态显存 (假设 Adam,
                      每个参数 4 bytes × 4 份),单位 MB
  - full_memory_mb:    全量微调优化器状态显存,单位 MB
  - saving_ratio:      节省比例 (1 - lora_memory_mb / full_memory_mb),
                      保留 4 位小数

示例:
    >>> result = compare_memory(2048, 32)
    LoRA 参数量: 131072
    全量参数量: 4194304
    LoRA 显存: 1.95 MB
    全量显存: 64.0 MB
    节省比例: 96.95%
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def compare_memory(d, r):
    """对比 LoRA 与全量微调的显存占用。

    返回: dict,含参数量与显存信息 (MB, 保留 2 位小数)。
    """
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 常规情况
    res = compare_memory(2048, 32)
    assert res["lora_params"] == 131072, (
        f"LoRA 参数量错误: {res['lora_params']}"
    )
    assert res["full_params"] == 4194304, (
        f"全量参数量错误: {res['full_params']}"
    )
    print(f"LoRA 参数量: {res['lora_params']}")
    print(f"全量参数量: {res['full_params']}")
    print(f"LoRA 显存: {res['lora_memory_mb']} MB")
    print(f"全量显存: {res['full_memory_mb']} MB")
    print(f"节省比例: {res['saving_ratio'] * 100:.2f}%")

    # 测试 2: 极端情况 r=d (LoRA 退化为全量)
    res2 = compare_memory(100, 100)
    assert res2["lora_params"] == 20000
    assert res2["full_params"] == 10000
    print(f"\nr=d 时 LoRA 参数={res2['lora_params']}, "
          f"全量参数={res2['full_params']}")

    # 测试 3: r=0 退化情况
    res3 = compare_memory(512, 0)
    assert res3["lora_params"] == 0
    assert res3["saving_ratio"] == 1.0, (
        f"r=0 时应节省 100%: {res3['saving_ratio']}"
    )
    print(f"r=0 时显存节省: {res3['saving_ratio'] * 100:.2f}%")
    print("测试通过 ✓")
