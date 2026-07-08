"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Trainer SFT 全流程 / LoRA / fp16]
[预计完成时间: 20 分钟]

[需要 GPU]

用 Trainer 对 Qwen2-0.5B-Instruct 跑 1 epoch SFT：
- 数据：dummy prompt/answer 共 6 条
- 配置：TrainingArguments(fp16=True, num_train_epochs=1,
         per_device_train_batch_size=2, logging_steps=2)

红线：务必 fp16=True，否则 7B 类稍后就会 OOM。

示例:
    >>> run_sft()
    {'loss': 1.89}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有 GPU 时完整训练
    # result = run_sft()
    # assert 'loss' in result
    # print("测试 1 通过: loss =", result['loss'])

    # 测试 2: 数据构建
    # ds = build_sft_dataset()
    # assert len(ds) == 6
    # print("测试 2 通过: 数据集 6 条")
    pass
