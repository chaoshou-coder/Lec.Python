"""
[难度: ⭐]
[所属知识点: TrainingArguments 基础]
[预计完成时间: 5 分钟]

从 transformers 导入 TrainingArguments，构造一个默认实例，
并打印三个属性：per_device_train_batch_size、
logging_steps、learning_rate，体会默认超参。

示例:
    >>> args = build_default_args()
    >>> print(args.per_device_train_batch_size)
    8
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认实例打印三个属性
    # args = build_default_args()
    # assert args.per_device_train_batch_size == 8
    # assert args.logging_steps == 500
    # print("测试 1 通过:", args.per_device_train_batch_size)

    # 测试 2: 自定义 epochs 后打印
    # args2 = build_default_args(num_train_epochs=3)
    # assert args2.num_train_epochs == 3
    # print("测试 2 通过:", args2.num_train_epochs)
    pass
