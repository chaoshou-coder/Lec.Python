"""
[难度: ⭐⭐]
[所属知识点: 全局 batch 公式]
[预计完成时间: 10 分钟]

小练习：实现 global_batch(pd, accum, gpus) 返回全局 batch，
公式 = pd * accum * gpus。这是 practice02 的简化版本。

示例:
    >>> global_batch(2, 8, 2)
    32
    >>> global_batch(4, 4, 1)
    16
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: pd=2, gpus=2, accum=8
    # r = global_batch(2, 8, 2)
    # assert r == 32, f"期望 32, 实际 {r}"
    # print("测试 1 通过:", r)

    # 测试 2: 单卡典型配置
    # r2 = global_batch(4, 4, 1)
    # assert r2 == 16
    # print("测试 2 通过:", r2)
    pass
