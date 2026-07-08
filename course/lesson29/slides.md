# Day29 · 训练循环

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day28 已掌握 torch.Tensor / autograd / nn.Module 基础、DataLoader 批量加载
> 关键问题:Day28 能搭网络、能跑 forward,但"训练"到底长啥样?本节给出**标准 5 步公式** —— forward → loss → zero_grad → backward → step —— 并把它封装成可复用模板;最后在 MNIST 上完整跑通。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `nn.Module` 的 `__init__` 和 `forward` 各负责什么?`requires_grad=True` 的作用是什么?backward 只能对什么类型 tensor 调用? 目的: 唤醒 nn.Module / autograd 记忆,为"串起来训练"埋伏笔。
- **赏玩 demo**(3 分钟): 展示两段代码 —— A 段"能跑但一锅粥"(forward / loss / backward 散落在全局变量里,每步都要手动索引);B 段"标准 5 步模板"(清晰 for 循环,每步一行)。让学员感受"结构化代码 vs 面条代码"的可维护性差距 —— **今天目标:让每个人都能写出 B 段**。

---

## 1. 第一讲(25 分钟) —— 标准训练循环 5 步公式

### 知识点 1.1 5 步公式:背下来就是生产力

```python
for epoch in range(num_epochs):
    for xb, yb in train_loader:
        # 1. 前向传播:拿到预测
        pred = model(xb)
        # 2. 计算损失
        loss = criterion(pred, yb)
        # 3. 清零梯度(重要!)
        optimizer.zero_grad()
        # 4. 反向传播:算梯度
        loss.backward()
        # 5. 更新参数
        optimizer.step()
```

> 口诀:**"前算损清更"** — forward、loss、zero_grad、backward、step,顺序不能乱。

### 知识点 1.2 每一步的职责

| 步骤 | 代码 | 干什么 |
|---|---|---|
| forward | `pred = model(xb)` | 当前参数下网络给出的预测 |
| loss | `loss = criterion(pred, yb)` | 预测 vs 真值的差距 |
| zero_grad | `optimizer.zero_grad()` | 把上次梯度清 0 —— PyTorch 默认累加 |
| backward | `loss.backward()` | 对 loss 做反向传播,填 `.grad` |
| step | `optimizer.step()` | 按梯度方向更新一步参数 |

### 知识点 1.3 两块"抹布":训练前清零,验证前关梯度

```python
# 训练模式:Dropout / BN 等行为开启
model.train()

# 验证模式:关 Dropout、关梯度跟踪
model.eval()
with torch.no_grad():
    for xb, yb in val_loader:
        pred = model(xb)
        ...
```

> 🔴 教学红线(忘记 zero_grad 导致梯度累积): 学员最经典的错 —— 5 步里漏了 `optimizer.zero_grad()`,等价于"每步梯度都叠加上去",loss 不降反升。演示:故意漏掉这行,loss 震荡 → 对比加上后正常下降。
>
> 🔴 教学红线(验证时忘 model.eval): Dropout 在 eval 模式会自动关闭;忘调 eval,验证集上的 loss 偏高、accuracy 抖动。新手常"训练 acc 95% 验证 acc 80%",查半天才发现是 Dropout 在验证时仍随机失活。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 给 MNIST 训练脚本挖掉 5 处填空(forward / loss / zero_grad / backward / step),学员补全跑通 (⭐⭐⭐,15 分钟)
- 练习 2: `in_class/practice02.py` —— 故意保留 zero_grad 前加一行 backward,观察 loss 变化,对比"不清零 vs 清零"的差异(⭐⭐,10 分钟)

> 巡场重点: 看学员 forward 是否传错变量 —— 把 `model(yb)` 写成 `model(xb)` 的一个字母之差;loss 是否 `criterion(pred, yb)` 而不是 `criterion(yb, pred)` —— PyTorch 的 loss 函数"传真值在后",和直觉相反。

---

## 3. 第二讲(25 分钟) —— optimizer 与 loss 函数

### 知识点 3.1 两大 optimizer:SGD vs Adam

| 优化器 | 公式 | 特点 |
|---|---|---|
| SGD | `θ = θ - lr * grad` | 简单,配合 momentum 常用 |
| Adam | 自适应 lr,一阶矩 + 二阶矩 | 默认首选,收敛快 |

```python
# SGD
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Adam
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
```

> 口诀:**SGD 是"老实走",Adam 是"聪明走" —— 新手先 Adam,稳定后 SGD+momentum 往往泛化更好**。

### 知识点 3.2 两大 loss 函数:MSELoss vs CrossEntropyLoss

```python
# 回归任务(预测数值):均方误差
criterion_mse = nn.MSELoss()
loss = criterion_mse(pred, target)   # pred 和 target 形状一样

# 分类任务(预测类别):交叉熵
criterion_ce = nn.CrossEntropyLoss()
loss = criterion_ce(logits, labels)
# logits: 原始输出,形状 [N, C];labels: 类别索引,形状 [N]
```

> 🔴 教学红线(CrossEntropyLoss 不需要 softmax): `nn.CrossEntropyLoss` 内部已经做了 softmax,传 logits 即可。学员常在外面再加 `F.softmax`,相当于 softmax 做了两次,概率被压扁,训练困难。
>
> 口诀:**CrossEntropyLoss = LogSoftmax + NLLLoss 合体,直接喂 logits**。

### 知识点 3.3 常用超参数经验

```python
# 图像分类:MNIST 级别
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

# 学习率调度:每 10 个 epoch lr 乘 0.1
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
```

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在同一批 MNIST 数据上分别用 SGD 和 Adam 训练 50 步,画两条 loss 曲线对比下降速度(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 故意把 CrossEntropyLoss 外面套 nn.Softmax,对比训练 loss 下降差异,理解"double softmax"错误 (⭐⭐⭐,10 分钟)

> 巡场重点: 看学员是否画了**同一坐标系**的两条曲线(而不是分两张图)—— 对比实验的可视化必须同尺度才有意义。

---

## 5. 第三讲(25 分钟) —— 验证循环 + 早停

### 知识点 5.1 验证循环:只看不算梯度

```python
model.eval()
total, correct = 0, 0
with torch.no_grad():
    for xb, yb in val_loader:
        pred = model(xb)
        _, predicted = torch.max(pred, 1)
        total += yb.size(0)
        correct += (predicted == yb).sum().item()
val_acc = correct / total
print(f"Val Acc: {val_acc:.4f}")
```

### 知识点 5.2 早停 (Early Stopping):验证 loss 不降就停

```python
best_loss = float("inf")
patience = 5
trigger = 0

for epoch in range(100):
    train_one_epoch(model, train_loader, optimizer, criterion)
    val_loss = evaluate(model, val_loader, criterion)

    if val_loss < best_loss:
        best_loss = val_loss
        torch.save(model.state_dict(), "best.pt")
        trigger = 0
    else:
        trigger += 1
        if trigger >= patience:
            print(f"早停于 epoch {epoch}")
            break
```

> 口诀:**验证 loss 不改善就耐心数,数到 patience 次就停 —— 避免过拟合**。
>
> 🔴 教学红线(错把训练 loss 当监控指标): 新手倾向于"只要训练 loss 一直降就继续跑",这会导致过拟合;必须用**验证集 loss** 做判断标准。

## 6. 小项目:完整 MNIST 训练(45 分钟)

- 项目: `mini_project/project01.py` —— MNIST 手写数字分类完整流水线 (30 行以内核心代码)
  - 数据: `torchvision.datasets.MNIST` + DataLoader
  - 模型: 简单的 `784 → 128 → 10` 全连接网络
  - 训练: Adam + CrossEntropyLoss,10 epoch
  - 可视化: 画 loss 曲线 + acc 曲线双坐标图
  - 目标: 测试 acc > 97% (⭐⭐⭐⭐)

> 巡场重点: 看学员是否把 `model.eval()` 放在验证循环**之外**(比如放在 epoch 循环内部但忘了调回 `model.train()`),导致下一个 epoch 还在 eval 模式训练 —— DNN 业内称"忘调 train"为最隐蔽 bug 之一。

---

## 7. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 忘记 `optimizer.zero_grad()` 导致梯度累加,loss 震荡不降
  2. 验证阶段没有 `model.eval()`,Dropout 仍在工作,val acc 偏低
  3. CrossEntropyLoss 外面套 softmax,double softmax 导致训练困难
- **作业说明**: 课后 `homework/task01.py`(把 MNIST 训练加验证循环 + 早停)、`task02.py`(对比 SGD vs Adam vs AdamW 在 MNIST 上的 loss 曲线),下节课前 10 分钟复盘。

---

## 易错点

1. **PyTorch 默认梯度累加**: 每次 backward 都**加到** `.grad` 上,不清零就等于把多步梯度叠一起 —— 必须显式调用 `optimizer.zero_grad()`。
2. **loss 参数顺序**: `criterion(pred, target)`,`pred` 在前,`target` 在后 —— 和直觉中"先真值后预测"相反。
3. **CrossEntropyLoss 已含 softmax**: 外面再套 softmax 是 double softmax,训练不收敛或很慢。
4. **eval 与 no_grad 要双管齐下**: `model.eval()` 改 Dropout/BN 行为,`torch.no_grad()` 关梯度计算;验证时两个都要。
5. **验证完要切回 train**: 一个 epoch 验证完忘了调 `model.train()`,下一个 epoch 仍在 eval 模式,梯度不更新。
6. **`torch.max` 返回值**: `_, predicted = torch.max(pred, 1)` 第一项是最大值(通常忽略),第二项才是类别索引。
7. **`model.parameters()` vs `model.named_parameters()`**: 前者只给 param 不给名;调试时用后者看每个 name 的 shape,方便排查。

## 延伸题

- **(Learning Rate Finder, Smith 2017, ⭐⭐⭐)**: 从一个极小 lr 开始每步乘 1.1,记录 lr-loss 曲线,找"loss 下降最快的 lr"作为正式训练起点 —— 超参数调优实用技巧。
- **(1cycle Policy, ⭐⭐⭐⭐)**: 实现"先升 lr 再降 lr"的 1cycle 调度,可视化 lr-loss 平面上的轨迹 —— 直观感受 lr 对训练的影响。
- **(TensorBoard 集成, ⭐⭐⭐)**: 在 MNIST 训练里加 `SummaryWriter`,用 TensorBoard 实时看 loss 曲线 —— 工业级调试手段入门。
- **(Mixed Precision + GradScaler, ⭐⭐⭐⭐)**: 用 `torch.cuda.amp.autocast` + `GradScaler` 做混合精度训练,显存减半、速度翻倍 —— 进阶性能优化。
