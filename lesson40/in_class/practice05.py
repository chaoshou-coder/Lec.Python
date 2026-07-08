"""
[难度: ⭐⭐⭐]
[所属知识点: 学习率调度 / Warmup + Cosine]
[预计完成时间: 15 分钟]

实现 SimpleLRScheduler(optimizer, warmup_steps, total_steps)，
前 warmup_steps 线性升温到初始 lr，之后按 cosine 衰减到 0。
每步调用 step()，可通过 get_last_lr() 查看当前 lr。

示例:
    >>> opt = torch.optim.Adam([torch.tensor(1.0, requires_grad=True)], lr=1e-3)
    >>> sched = SimpleLRScheduler(opt, warmup_steps=10, total_steps=100)
    >>> for _ in range(5):
    ...     sched.step()
    >>> print(sched.get_last_lr()[0])  # 应约为 5e-4 (warmup 50%)
    0.0005
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: warmup 阶段第 5 步 (共 10 步)
    # opt = torch.optim.Adam([torch.tensor(1.0, requires_grad=True)], lr=1e-3)
    # sched = SimpleLRScheduler(opt, warmup_steps=10, total_steps=100)
    # for _ in range(5):
    #     sched.step()
    # lr = sched.get_last_lr()[0]
    # assert abs(lr - 5e-4) < 1e-6, f"warmup 异常: {lr}"
    # print("测试 1 通过: warmup lr =", lr)

    # 测试 2: 最终步应衰减接近 0
    # opt2 = torch.optim.Adam([torch.tensor(1.0, requires_grad=True)], lr=1e-3)
    # sched2 = SimpleLRScheduler(opt2, warmup_steps=10, total_steps=100)
    # for _ in range(100):
    #     sched2.step()
    # lr_final = sched2.get_last_lr()[0]
    # assert lr_final < 1e-5, f"cosine 异常: {lr_final}"
    # print("测试 2 通过: 最终 lr =", lr_final)
    pass
