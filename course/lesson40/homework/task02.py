"""
[难度: ⭐⭐⭐]
[所属知识点: 链式调用 / TrainingArguments 构建器]
[预计完成时间: 15 分钟]

写 TrainingConfigBuilder 类，链式调用返回 TrainingArguments：
- .task("qa")：设置任务标签
- .epochs(3)：设置 num_train_epochs
- .lr(2e-4)：设置 learning_rate
- .fp16(True)：设置 fp16
- .build()：返回 TrainingArguments 实例

红线：7 类模型务必 .fp16(True)，否则显存翻倍 OOM。

示例:
    >>> builder = TrainingConfigBuilder()
    >>> args = builder.task("qa").epochs(3).lr(2e-4).fp16(True).build()
    >>> print(args.num_train_epochs)
    3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 完整链式调用
    # builder = TrainingConfigBuilder()
    # args = builder.task("qa").epochs(3).lr(2e-4).fp16(True).build()
    # assert args.num_train_epochs == 3
    # assert args.learning_rate == 2e-4
    # assert args.fp16 is True
    # print("测试 1 通过: fp16 =", args.fp16)

    # 测试 2: 默认构建
    # args2 = TrainingConfigBuilder().build()
    # assert args2.fp16 is False  # 默认关闭，提醒学员主动开
    # print("测试 2 通过: 默认 fp16 =", args2.fp16)
    pass
