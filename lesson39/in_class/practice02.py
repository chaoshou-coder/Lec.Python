"""
[难度: ⭐⭐]
[所属知识点: LoRA 参数量计算]
[预计完成时间: 10 分钟]

题目描述:
LoRA 在 d×d 的权重矩阵上插入两个低秩矩阵 A(d×r) 和 B(r×d),
请实现 compute_lora_params(d, r),返回:
  - lora_params: LoRA 引入的参数量 (A + B)
  - total_params: 原权重矩阵参数量 (d×d)
  - ratio: lora_params / total_params 的百分比 (保留 2 位小数)

示例:
    >>> compute_lora_params(4096, 16)
    (131072, 16777216, 0.78)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def compute_lora_params(d, r):
    """计算 LoRA 参数量及占比。

    返回: (lora_params, total_params, ratio_percent)
    """
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 常规情况
    lora, total, ratio = compute_lora_params(4096, 16)
    assert lora == 131072, f"lora 参数错误: {lora}"
    assert total == 16777216, f"total 参数错误: {total}"
    assert ratio == 0.78, f"ratio 错误: {ratio}"
    print(f"LoRA 参数量: {lora}, 原参数量: {total}, "
          f"占比: {ratio}%")

    # 测试 2: 极小维度
    lora2, total2, ratio2 = compute_lora_params(8, 2)
    assert lora2 == 32, f"测试2 lora 错误: {lora2}"
    assert total2 == 64, f"测试2 total 错误: {total2}"
    print(f"LoRA 参数量: {lora2}, 原参数量: {total2}, "
          f"占比: {ratio2}%")

    # 测试 3: 边界 r=0 (退化)
    lora3, _, ratio3 = compute_lora_params(100, 0)
    assert lora3 == 0, f"测试3 lora 应为 0: {lora3}"
    print(f"r=0 时 LoRA 参数量: {lora3}")
    print("测试通过 ✓")
