# Day28 · PyTorch 基础

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day27 已掌握 NumPy ndarray 基本操作、梯度数值验证、Python 类基础(__init__ / self / 方法)
> 关键问题: NumPy 能算张量,但能不能自动求导?能不能跑在 GPU?能不能搭神经网络模块?本节进入 PyTorch 生态 —— 从"数组"升级到"可微张量",再到 nn.Module 搭建网络骨架。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— NumPy 数组 `a * b` 是矩阵乘法还是逐元素乘?`a.shape` 返回什么?你用 Day27 的数值梯度方法求 `y=x²` 的导数, step 要多小才够准? 目的: 唤醒 ndarray 记忆,为"PyTorch 与 NumPy 对照"埋伏笔。
- **赏玩 demo**(3 分钟): 在终端跑一段代码 —— 先建一个 NumPy 数组,再 `torch.from_numpy()` 转成 tensor,做 `.backward()` 后直接打印 `.grad`。"NumPy 只会算结果,PyTorch 自动告诉你导数是多少"—— 一句话点出自动微分的价值。

---

## 1. 第一讲(20 分钟) —— torch.Tensor 基础:从 ndarray 升级

### 知识点 1.1 Tensor vs ndarray:无缝互转,功能超集

PyTorch Tensor ≈ NumPy ndarray 的"加强版":多了自动微分、GPU 加速、神经网络三方。

```python
import numpy as np
import torch

# 从 NumPy 创建(共享内存,改一个另一个也改)
arr = np.array([1.0, 2.0, 3.0])
t = torch.from_numpy(arr)

# 从 Python 列表创建(拷贝,不共享内存)
t2 = torch.tensor([1.0, 2.0, 3.0])

# Tensor 转回 NumPy
arr_back = t2.numpy()
```

> 口诀:**from_numpy 共享,numpy() 传回,tensor() 拷贝一份**。
>
> 🔴 教学红线(from_numpy 共享内存): 学员常以为"转了就互不干扰"。演示 `arr[0] = 99; print(t)` 输出 `[99, 2, 3]` —— `from_numpy` 是"同一块内存换个名",要独立副本用 `.clone()`。

### 知识点 1.2 `requires_grad`:告诉 PyTorch"我要对这个求导"

`requires_grad=True` 让 PyTorch 跟踪这个 tensor 的所有运算,构建计算图。

```python
x = torch.tensor(2.0, requires_grad=True)
y = x ** 3 + 2 * x          # 计算图自动记录
y.backward()                # 反向传播
print(x.grad)               # 3*x² + 2 = 14 (x=2 时)
```

> 直觉:`requires_grad=True` 就像给变量贴上"小抄",每一步运算都写下来,backward 时翻小抄算链式法则。

### 知识点 1.3 设备:CPU vs CUDA

默认 tensor 跑在 CPU;要 GPU 加速得显式搬到 CUDA 设备。

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.tensor([1.0, 2.0], device=device)

# 或创建后再搬
y = torch.tensor([3.0, 4.0]).to(device)
```

> 注意:tensor 运算双方必须在**同一设备**,否则报 `RuntimeError`。新手常把一个放 CPU 一个放 CUDA 然后懵了。

### 知识点 1.4 Tensor 基本运算:和 NumPy 几乎一样

```python
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

print(a + b)        # 逐元素加
print(a @ b)        # 矩阵乘(和 a.matmul(b) 等价)
print(a.sum())      # 全部元素求和,返回标量 tensor
print(a[0, 1])      # 2.0 —— 切片索引和 NumPy 一致

# 形状操作
print(a.reshape(1, 4))   # [[1,2,3,4]]
print(a.view(4))         # [1,2,3,4]
```

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 创建 tensor (从 list / 从 numpy / 全 1 / 全 0 / 随机),打印 dtype 与 shape (⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `from_numpy` 与 `tensor()` 各建一个 tensor,改原 array 后观察谁变了,验证"共享内存" (⭐⭐,15 分钟)

> 巡场重点: 看学员是否把 `dtype=torch.float32` 写成 `dtype=float` —— PyTorch 必须用 `torch.float32` / `torch.int64` 这套,torch 不认识 Python 内置的 `float`/`int`。

---

## 3. 第二讲(25 分钟) —— autograd 自动微分:手算 vs PyTorch 速算

### 知识点 3.1 手算一个函数: `y = 2x²`

设 `x = 3`,手工求导:
- 前向: `y = 2 * 3² = 18`
- 导数: `dy/dx = 4x = 12`

```python
x = torch.tensor(3.0, requires_grad=True)
y = 2 * x ** 2
y.backward()
print(x.grad)   # tensor(12.)  ← 和手算一致
```

### 知识点 3.2 多变量链式法则

PyTorch 自动对**标量求导**;向量/矩阵要先 `.sum()` 或指定 `gradient` 参数。

```python
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2                 # [1, 4, 9]
z = y.sum()                # 14 —— 必须聚成标量再 backward
z.backward()
print(x.grad)              # [2, 4, 6] = 2x
```

> 口诀:**backward 只对标量开口,先用 sum/mean 把它收成标量**。
>
> 🔴 教学红线(in-place 会破坏计算图): 学员常写 `x += 1` 这种 in-place 操作,报 `RuntimeError: leaf variable` —— 必须用 `x = x + 1` 这种新建 tensor 的写法。

### 知识点 3.3 停下跟踪:`torch.no_grad()`

推理阶段不需要梯度,关掉省显存、加速。

```python
with torch.no_grad():
    pred = model(x_test)   # 不建计算图
```

等价写法: `with torch.inference_mode():`(更新,更快)。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 用 autograd 对 `y = x³ + 5x` 在 `x = 2` 求导,与 Day27 数值梯度对比(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 故意触发"非标量 backward 报错"和"in-place 报错",观察错误信息(⭐⭐⭐⭐,10 分钟)

> 巡场重点: 练习 3 学员常忘记 `requires_grad=True` 就直接 backward,报 `element 0 of tensors does not require grad`。提示: **"要跟踪谁,就给谁贴 requires_grad"**。

---

## 5. 第三讲(25 分钟) —— nn.Module 类:用 Python 类搭网络骨架

### 知识点 5.1 类比 Python class:`__init__` 配零件, `forward` 定义流程

`nn.Module` 和其他 Python 类一样,只是多了"登记参数"的约定。

```python
import torch.nn as nn

class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        # __init__ 里"登记"所有层(就像给类配属性)
        self.fc1 = nn.Linear(3, 4)   # 3 入 4 出
        self.fc2 = nn.Linear(4, 2)   # 4 入 2 出

    def forward(self, x):
        # forward 里写数据怎么流(就像给类写方法)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = TinyNet()
print(model)
```

> 口诀:**__init__ 买零件(声明层),forward 接线(定义数据流);必须 super().__init__() 打地基**。

### 知识点 5.2 `parameters()`:拿到所有可训练参数

```python
for name, param in model.named_parameters():
    print(name, param.shape)

# fc1.weight  torch.Size([4, 3])
# fc1.bias    torch.Size([4])
# fc2.weight  torch.Size([2, 4])
# fc2.bias    torch.Size([2])
```

### 知识点 5.3 前向推理一次

```python
x = torch.randn(5, 3)   # 5 个样本,每个 3 维
y = model(x)            # 5 x 2 输出
print(y.shape)          # torch.Size([5, 2])
```

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 定义一个 `3 → 8 → 1` 的 Net,打印 `named_parameters`,手动调一次 forward (⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 故意漏写 `super().__init__()`,观察报错;再故意漏写 `forward` 方法但直接调用 `model(x)`,观察报错(⭐⭐⭐,10 分钟)

> 巡场重点: 看学员是否把 `forward` 命名为 `forword` / `foward` —— 这是最常见的拼写错,IDE 不会提示,但 `model(x)` 会报 `'Net' object is not callable`。

---

## 7. 第四讲(20 分钟) —— DataLoader + Dataset:批量喂数据

### 知识点 7.1 自定义 Dataset:`__getitem__` + `__len__`

Dataset 就是"一份数据清单":`__len__` 告诉一共多少条,`__getitem__(i)` 说出第 i 条长啥样。

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
```

> 类比:Dataset 就是一个既能 `len()` 也能 `[]` 的列表,只不过每条数据按需读入(好比 yield 生成器,用到才取)。

### 知识点 7.2 DataLoader:洗牌 + 分批 + 并行

```python
ds = MyDataset(X_train, y_train)
loader = DataLoader(ds, batch_size=32, shuffle=True, drop_last=True)

for xb, yb in loader:
    print(xb.shape)   # torch.Size([32, ...]) —— 32 条一批
```

> `shuffle=True`: 每轮(epoch)重新洗牌,避免模型"记住顺序"
> `drop_last=True`: 最后不满 batch_size 的一小撮扔掉,防止 BN 计算出错
>
> 🔴 教学红线(默认 drop_last=False): 最后一个 batch 可能只有 1 条,某些层(如 BatchNorm)会崩溃;新手排查半天发现是"尾巴问题"。

## 8. 小项目(45 分钟)

- 项目: `mini_project/project01.py` —— 用 `nn.Linear` 搭一个 `3 → 4 → 2` 网络,手写训练循环(不调 optim,手动 `param.data -= lr * param.grad`),在合成数据 (100 条) 上跑 50 个 epoch 看 loss 下降 (⭐⭐⭐⭐)

> 巡场重点: 看学员是否手动 SGD 写对了 —— `with torch.no_grad(): param.data -= lr * param.grad` 然后 `param.grad.zero_()`;顺序反了会 zero 掉还没更新的梯度。

---

## 9. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 忘记给 `requires_grad=True` 的 tensor 调 `backward()`,报"不需要 grad"
  2. in-place 操作 (`x += 1`) 破坏计算图,报 `leaf variable` 错误
  3. 手写 SGD 时先 `zero_grad()` 再 `step()`,结果是梯度清零=白训
- **作业说明**: 课后 `homework/task01.py`(autograd 求多元函数梯度)、`task02(nn.Module 搭 3 层网络手动训练 50 步)`,下节课前 10 分钟复盘。

---

## 易错点

1. **`requires_grad` 默认 False**: 想求导必须显式传 `True`,否则 backward 报错。
2. **`from_numpy` 共享内存**: 转出来的 tensor 和原始 array 是**同一块内存**,改一个另一个也变;要独立副本用 `.clone()`。
3. **backward 只能对标量**: 向量 tensor 先 `.sum()` 再 `.backward()`。
4. **in-place 操作破坏计算图**: 避免 `x += 1`、`x[0] = 1` 这类直接改值的操作,改用 `x = x + 1` 重建。
5. **nn.Module 必须有 `super().__init__()`**: 漏掉这行,`self.fc1 = ...` 时找不到属性字典,报 `AttributeError`。
6. **forward 拼写错**: `forword` / `foward` / `froward` 都是新手高频错,IDE 不报错但 `model(x)` 会失败。
7. **DataLoader 的 drop_last**: 默认 False,最后不足 batch_size 的尾巴会保留,BatchNorm 对 batch=1 会崩溃。

## 延伸题

- **(Gradient Checking, CS231n, ⭐⭐⭐)**: 写一个函数,对任意 `f(x)`,用 `(f(x+h) - f(x-h)) / 2h` 算数值梯度,再和 `autograd` 结果做 `torch.allclose`,验证自动微分正确性 —— 巩固 Day27 数值梯度 + Day28 autograd。
- **(Tiny Autograd from Scratch, MicroGrad 灵感, ⭐⭐⭐⭐)**: 用手写 `class Value` 实现前向 + backward(类比 Karpathy 的 MicroGrad 视频) —— 进阶理解计算图本质。
- **(CPU vs CUDA timing, ⭐⭐⭐)**: 用 `torch.rand(1000, 1000)` 在 CPU 和 CUDA(如有) 上做 100 次矩阵乘,对比耗时 —— 直观感受 GPU 加速比。
