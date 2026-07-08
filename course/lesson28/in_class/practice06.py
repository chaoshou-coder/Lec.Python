"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整训练 pipeline
          （model+DataLoader+optimizer+loss）]
[预计完成时间: 20 分钟]

把散落的知识串成完整 pipeline，在合成数据上跑 10 epoch，
观察 loss 下降趋势——这是训练神经网络的标配流程。

任务:
  1) 定义 class MLP(nn.Module): 两层 (in=10->hid=32->out=1),
      hidden 用 ReLU 激活, out 不激活（BCEWithLogitsLoss）;
  2) 合成数据 X=torch.randn(200,10),
             y=torch.randint(0,2,(200,)).float();
  3) DataLoader batch_size=64, shuffle=True;
  4) optimizer=Adam(lr=1e-2), loss_fn=BCEWithLogitsLoss;
  5) 跑 10 epoch, 每个 epoch 计算平均 loss,
     打印 epoch 编号和 loss, loss 应呈下降趋势。

示例:
    >>> python3 practice06.py
    epoch  1  loss: 0.6932
    epoch  2  loss: 0.6710
    ...
    epoch 10  loss: 0.5103
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


# 1) 定义两层 MLP
class MLP(nn.Module):
    """输入 10 -> 隐藏 32 (ReLU) -> 输出 1"""

    def __init__(self, in_features=10, hidden=32, out_features=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_features, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_features),
        )

    def forward(self, x):
        return self.net(x).squeeze(1)  # shape: (N,1)->(N,)


# 2) 合成数据: 200 个样本, 10 维特征, 二分类标签
X = torch.randn(200, 10)
y = torch.randint(0, 2, (200,)).float()

# 3) DataLoader
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

# 4) 模型、优化器、损失函数
model = MLP()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
loss_fn = nn.BCEWithLogitsLoss()

# 5) 训练 10 epoch
model.train()
for epoch in range(1, 11):
    total_loss = 0.0
    n_batches = 0
    for X_batch, y_batch in loader:
        optimizer.zero_grad()
        pred = model(X_batch)
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        n_batches += 1
    avg_loss = total_loss / n_batches
    print(f"epoch {epoch:2d}  loss: {avg_loss:.4f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 模型输出形状应为 (200,)
    model.eval()
    with torch.no_grad():
        out = model(X)
    assert out.shape == torch.Size([200])

    # 测试 2: 模型有可学习参数
    params = list(model.parameters())
    assert len(params) == 4  # w1, b1, w2, b2

    # 测试 3: 重新跑 2 epoch, 平均 loss 是有限正数
    model.train()
    tmp_loss = 0.0
    tmp_cnt = 0
    for X_b, y_b in loader:
        p = model(X_b)
        l = loss_fn(p, y_b)
        tmp_loss += l.item()
        tmp_cnt += 1
    avg = tmp_loss / tmp_cnt
    assert 0 < avg < 10
    print("所有测试通过!")
