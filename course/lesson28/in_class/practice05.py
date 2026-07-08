"""
[难度: ⭐⭐⭐]
[所属知识点: DataLoader + TensorDataset]
[预计完成时间: 15 分钟]

训练前要把数据装进 DataLoader。请用合成数据练习打包、
分批次与随机打乱的操作。

任务:
  1) 合成数据: X=torch.randn(100,5),
              y=torch.randint(0,2,(100,)).float();
  2) 用 TensorDataset(X, y) 打包;
  3) 用 DataLoader(dataset, batch_size=32, shuffle=True)
     加载;
  4) 迭代一次（一个 for batch in loader），
     打印每个 batch 的 X_batch.shape, y_batch.shape。

示例:
    >>> python3 practice05.py
    batch 1: X -> torch.Size([32, 5]),
             y -> torch.Size([32])
    batch 2: X -> torch.Size([32, 5]),
             y -> torch.Size([32])
    batch 3: X -> torch.Size([32, 5]),
             y -> torch.Size([32])
    batch 4: X -> torch.Size([4, 5]),
             y -> torch.Size([4])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch
from torch.utils.data import TensorDataset, DataLoader

# 1) 合成数据: 100 个样本, 5 维特征, 二分类标签
X = torch.randn(100, 5)
y = torch.randint(0, 2, (100,)).float()

# 2) 打包成 TensorDataset
dataset = TensorDataset(X, y)

# 3) 用 DataLoader 加载, batch_size=32, 打乱
loader = DataLoader(dataset, batch_size=32, shuffle=True)

# 4) 迭代一次, 打印每个 batch 的形状
for i, (X_batch, y_batch) in enumerate(loader, start=1):
    print(f"batch {i}: X -> {X_batch.shape},"
          f" y -> {y_batch.shape}")

# ======================
# 测试区(教师可复制到终端验证)
# ==========================
if __name__ == '__main__':
    # 测试 1: dataset 长度应为 100
    assert len(dataset) == 100

    # 测试 2: 重新迭代, 统计 batch 数与最后一个 batch 大小
    batches = list(loader)
    # 100 // 32 = 3 满批 + 1 小批 = 4
    assert len(batches) == 4
    # 最后一个 batch 大小为 100 - 32*3 = 4
    assert batches[-1][0].shape[0] == 4

    # 测试 3: 每个 batch 的特征维度是 5
    for X_b, y_b in batches:
        assert X_b.shape[1] == 5
        assert y_b.shape[0] == X_b.shape[0]
    print("所有测试通过!")
