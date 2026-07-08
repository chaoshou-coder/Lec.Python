"""
[难度: ⭐⭐⭐]
[所属知识点: DPO 损失函数]
[预计完成时间: 15 分钟]

写 DPOTrainerLite 类，含 compute_loss：
- chosen_logps: 偏好回答的 log-prob 张量
- rejected_logps: 非偏好回答的 log-prob 张量
- beta: 温度系数，默认 0.1

损失公式：
loss = -log(sigmoid(beta * (chosen_logps - rejected_logps)))

教学点：DPO 直接优化 chosen > rejected 的偏好，
无需 RM、无需 PPO 采样，所以训练更稳定。

示例:
    >>> trainer = DPOTrainerLite()
    >>> loss = trainer.compute_loss(
    ...     torch.tensor([2.0, 1.5]),
    ...     torch.tensor([1.0, 0.5]),
    ...     beta=0.1)
    >>> loss.item()  # 应为一个正的小值
    0.0452
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本 loss
    # trainer = DPOTrainerLite()
    # loss = trainer.compute_loss(
    #     torch.tensor([2.0, 1.5]),
    #     torch.tensor([1.0, 0.5]),
    #     beta=0.1)
    # assert loss.item() > 0
    # print("测试 1 通过: loss =", loss.item())

    # 测试 2: chosen 越大于 rejected，loss 越小
    # loss_easy = trainer.compute_loss(
    #     torch.tensor([5.0]), torch.tensor([0.5]), beta=0.1)
    # loss_hard = trainer.compute_loss(
    #     torch.tensor([1.0]), torch.tensor([0.9]), beta=0.1)
    # assert loss_easy.item() < loss_hard.item()
    # print("测试 2 通过: 简单样本 loss 更小")
    pass
