"""
[难度: ⭐⭐⭐⭐]
[所属知识点: TrainerPipeline / Qwen2 LoRA 微调]
[预计完成时间: 20 分钟]

[需要 GPU]

写 TrainerPipeline 类，封装三个步骤：
- prepare_model(): 加载 Qwen2-0.5B-Instruct + LoRA
- prepare_data(): 构造 dummy 数据 6 条 (prompt/answer)
- train(): Trainer 跑 1 epoch，fp16=True，打印 loss

红线：7B 模型不开 fp16=True 直接 OOM，
Qwen2-0.5B 虽然小但同样要养成好习惯。

示例:
    >>> pipe = TrainerPipeline()
    >>> pipe.prepare_model()
    >>> pipe.prepare_data()
    >>> pipe.train()
    loss: 2.31
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有 GPU 时完整流程
    # pipe = TrainerPipeline()
    # pipe.prepare_model()
    # pipe.prepare_data()
    # pipe.train()
    # print("测试 1 通过: 训练完成")

    # 测试 2: 数据长度断言
    # pipe2 = TrainerPipeline()
    # ds = pipe2.prepare_data()
    # assert len(ds) == 6
    # print("测试 2 通过: 数据集 6 条")
    pass
