"""
[难度: ⭐⭐]
[所属知识点: TrainingArguments 审计 / 混合精度]
[预计完成时间: 10 分钟]

写 audit_training_args(args)，检查两项红线：
1. 是否开启 fp16 或 bf16（至少一个为 True）
2. learning_rate 是否 <= 1e-3

返回 dict {"fp16_ok": bool, "lr_ok": bool}。

教学红线：忘记 fp16=True 导致显存翻倍、7B 直接 OOM。

示例:
    >>> from transformers import TrainingArguments
    >>> args = TrainingArguments("./out", fp16=True, lr=2e-5)
    >>> audit_training_args(args)
    {'fp16_ok': True, 'lr_ok': True}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正确开启 fp16 + 小 lr
    # args1 = TrainingArguments("./out", fp16=True, lr=2e-5)
    # r1 = audit_training_args(args1)
    # assert r1 == {'fp16_ok': True, 'lr_ok': True}
    # print("测试 1 通过:", r1)

    # 测试 2: 忘记开 fp16 → 典型失败案例
    # args2 = TrainingArguments("./out", lr=2e-5)
    # r2 = audit_training_args(args2)
    # assert r2['fp16_ok'] is False
    # print("测试 2 通过 (捕获风险):", r2)
    pass
