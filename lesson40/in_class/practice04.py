"""
[难度: ⭐⭐⭐]
[所属知识点: Trainer + LoRA + Dummy 数据]
[预计完成时间: 15 分钟]

[需要 GPU]

用 8 条 dummy 中文句子 + bert-base-chinese + LoRA（peft）+
Trainer 跑 1 个 epoch，打印最终 loss，体验完整训练管线。

提示：数据集只用 {"text": [...8 条...]}，任务用
AutoModelForSequenceClassification(num_labels=2)。
开启 fp16=True 避免显存翻倍。

示例:
    >>> train_lora_bert()
    {'loss': 0.6931}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有 GPU 时跑完整流程
    # result = train_lora_bert()
    # assert 'loss' in result
    # print("测试 1 通过: loss =", result['loss'])

    # 测试 2: 数据集长度断言
    # ds = build_dummy_dataset()
    # assert len(ds) == 8
    # print("测试 2 通过: 数据集 8 条")
    pass
