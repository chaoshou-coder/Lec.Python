"""
[难度: ⭐⭐⭐⭐]
[所属知识点: ExperimentLogger 实验记录类]
[预计完成时间: 20 分钟]

题目描述:
实现一个 ExperimentLogger 类,记录每个 epoch 的 train/val
loss 和 acc,并能通过 dict 导出结果。场景:你在做大量消融实验,
需要"一站式记录"每次实验指标,便于后续画对比图。

类接口要求:
    logger = ExperimentLogger()
    logger.log(epoch=1, train_loss=1.23, val_loss=1.45,
               train_acc=55.6, val_acc=52.3)
    results = logger.to_dict()
    # results = {"train_loss":[1.23], "val_loss":[1.45],
    #           "train_acc":[55.6], "val_acc":[52.3]}

约束:
    - log 方法必须包含所有 4 个指标
    - to_dict 返回 dict,每个 key 对应一个 list
    - 初始化时内部数据结构应为空 list

示例:
    >>> logger.to_dict()
    {'train_loss': [1.23], 'val_loss': [1.45],
     'train_acc': [55.6], 'val_acc': [52.3]}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class ExperimentLogger:
    """实验记录器:按 epoch 记录 train/val loss 和 acc"""

    def __init__(self):
        self.history = {
            "train_loss": [],
            "val_loss": [],
            "train_acc": [],
            "val_acc": [],
        }

    def log(self, epoch, train_loss, val_loss,
            train_acc, val_acc):
        self.history["train_loss"].append(train_loss)
        self.history["val_loss"].append(val_loss)
        self.history["train_acc"].append(train_acc)
        self.history["val_acc"].append(val_acc)

    def to_dict(self):
        return self.history


logger = ExperimentLogger()
logger.log(epoch=1, train_loss=1.23, val_loss=1.45,
           train_acc=55.6, val_acc=52.3)
logger.log(epoch=2, train_loss=0.98, val_loss=1.12,
           train_acc=65.2, val_acc=61.8)

results = logger.to_dict()
print(results)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: to_dict 返回 4 个 key
    assert len(results) == 4, \
        f"应有 4 个 key,实际 {len(results)}"
    print("测试 1 通过")

    # 测试 2: 每个 key 对应 list 长度 = 已记录 epoch 数
    for k, v in results.items():
        assert isinstance(v, list), \
            f"{k} 应为 list"
        assert len(v) == 2, \
            f"{k} 应有 2 条记录,实际 {len(v)}"
    print("测试 2 通过")

    # 测试 3: 数值正确
    assert results["train_loss"] == [1.23, 0.98]
    assert results["val_acc"] == [52.3, 61.8]
    print("测试 3 通过")
