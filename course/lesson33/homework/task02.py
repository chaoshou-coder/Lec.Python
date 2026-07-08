"""
[难度: ⭐⭐⭐]
[所属知识点: 序列模型 / 手写训练步 / 反向传播]
[预计完成时间: 15 分钟]

手写一个训练步函数 train_step，完成
"梯度清零 → 前向 → 算损失 → 反向 → 更新" 完整流程。

任务:
  1. 定义函数 train_step(model, optimizer, batch_x, batch_y, criterion)
  2. 在函数内依次: optimizer.zero_grad() → pred=model(x)
     → loss=criterion(pred,y) → loss.backward() → optimizer.step()
  3. 返回 loss.item()(float 标量)
  4. 测试时用一个线性模型在随机数据上跑两步，打印损失

示例:
    >>> loss = train_step(model, opt, x, y, nn.MSELoss())
    >>> print(loss)   # 例如 1.0234
"""

import torch
import torch.nn as nn
import torch.optim as optim

# 一个小模型: 输入 5 维，输出 1 维
model = nn.Linear(in_features=5, out_features=1)
optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def train_step(model, optimizer, batch_x, batch_y, criterion):
    """单步训练: 返回 float 型损失。"""
    # 梯度清零，防止累加上一步梯度
    optimizer.zero_grad()
    # 前向传播
    pred = model(batch_x)
    # 计算损失
    loss = criterion(pred, batch_y)
    # 反向传播，计算梯度
    loss.backward()
    # 参数更新
    optimizer.step()
    return loss.item()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 构造一批随机输入 (batch_size=8, input_dim=5)
    x = torch.randn(8, 5)
    # 目标值 (batch_size=1, output_dim=1)
    y = torch.randn(8, 1)

    # 测试 1: 跑一步，检查 loss 是 float
    loss1 = train_step(model, optimizer, x, y, criterion)
    assert isinstance(loss1, float), \
        f"返回值错误: float, 实际 {type(loss1)}"
    print(f"第 1 步损失: {loss1:.4f}")

    # 测试 2: 再跑一步，观察损失被正常打印
    loss2 = train_step(model, optimizer, x, y, criterion)
    print(f"第 2 步损失: {loss2:.4f}")
    print("测试通过: train_step 运行正常!")
