"""
[难度: ⭐⭐]
[所属知识点: 梯度累积 / 全局 batch 计算]
[预计完成时间: 10 分钟]

在显存有限时，通过梯度累积放大全局 batch。
实现 compute_effective_batch(per_device, grad_accum, n_gpus=1)
返回全局等效 batch_size = per_device * grad_accum * n_gpus。

红线提示：不开 fp16=True 时显存翻倍，7B 直接 OOM，
所以常用小 per_device + 大 grad_accum 替代大 batch。

示例:
    >>> compute_effective_batch(4, 4, 1)
    16
    >>> compute_effective_batch(2, 8, 2)
    32
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: per_device=4, grad_accum=4, 单卡
    # result = compute_effective_batch(4, 4, 1)
    # assert result == 16, f"期望 16, 实际 {result}"
    # print("测试 1 通过: 全局 batch =", result)

    # 测试 2: 双卡, per_device=2, accum=8
    # result2 = compute_effective_batch(2, 8, 2)
    # assert result2 == 32, f"期望 32, 实际 {result2}"
    # print("测试 2 通过: 全局 batch =", result2)
    pass
