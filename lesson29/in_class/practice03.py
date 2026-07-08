"""
[难度: ⭐⭐]
[所属知识点: model.eval() + torch.no_grad() 验证循环]
[预计完成时间: 10 分钟]

在验证集上评估模型时要用 eval 模式和 no_grad。

任务：
1) 定义一个含 nn.Dropout(0.5) 的简单分类模型
   SimpleClf：fc1 = Linear(10, 32), relu, dropout,
   fc2 = Linear(32, 2)；
2) 在合成数据上训练 5 epoch；
3) 用 model.eval() + torch.no_grad() 评估，计算准确率；
4) 打印准确率。

示例:
    >>> python3 practice03.py
    训练完成
    验证准确率: 68.50%
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification

torch.manual_seed(42)

# 合成数据
X_np, y_np = make_classification(
    n_samples=500, n_features=10, n_classes=2,
    n_informative=5, random_state=42
)
X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.long)


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
class SimpleClf(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(10, 32),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(32, 2),
        )

    def forward(self, x):
        return self.net(x)


model = SimpleClf()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-2)

# 训练 5 epoch
model.train()
for epoch in range(5):
    optimizer.zero_grad()
    out = model(X)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()

# 验证：model.eval() + no_grad
model.eval()
correct = 0
total = 0
with torch.no_grad():
    out = model(X)
    pred = out.argmax(dim=1)
    correct = (pred == y).sum().item()
    total = y.size(0)
acc = correct / total * 100
print("训练完成")
print(f"验证准确率: {acc:.2f}%")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 准确率在合理范围 (0, 100)
    assert 0 < acc < 100
    # 测试 2: 模型参数存在
    params = list(model.parameters())
    assert len(params) == 4
    # 测试 3: 预测值只有 0 或 1
    with torch.no_grad():
        preds = model(X).argmax(dim=1)
    assert preds.min() >= 0 and preds.max() <= 1
    print("所有测试通过!")
