# Day30 · CNN + RNN 直觉 + 正则化

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day29 已掌握标准训练循环 5 步公式、MNIST 全连接训练、loss/acc 可视化
> 关键问题:全连接网络处理图像时参数爆炸、忽略空间结构;处理序列时"读完就忘"。本节给出两大架构 —— CNN(空间特征)和 RNN(时序记忆)—— 再加"正则化四件套"防过拟合,让你从"能写模板"升级为"能选课代表模型"。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 训练循环 5 步依次是什么?验证阶段要调哪些方法关哪些行为?CrossEntropyLoss 前要不要 softmax? 目的: 唤醒训练循环记忆,为"引入新架构"埋伏笔。
- **赏玩 demo**(3 分钟): 展示一张猫的图片,问"你怎么认出这是猫?"学员大概率回答"看到耳朵、眼睛、胡子"。引出:**人眼先看边缘 → 再拼纹理 → 最后认出耳朵眼睛**—— 这就是 CNN 的层级特征思想:浅层学边缘、中层学纹理、深层学语义。

---

## 1. 第一讲(25 分钟) —— CNN 直觉:卷积核、特征图、池化

### 知识点 1.1 卷积核:每个核 = 一个特征探测器

卷积核(又称 filter)是一个小权重矩阵,在输入图像上**滑动**,每到一个位置做一次"点乘+求和",输出一个数 —— 这堆数拼成一张**特征图**(Feature Map)。

```python
import torch.nn as nn

# 1 通道(灰度) → 8 个核,每个 3×3
conv = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3)

# 输入: batch=1, channel=1, 28×28
x = torch.randn(1, 1, 28, 28)
out = conv(x)
print(out.shape)   # torch.Size([1, 8, 26, 26])
```

> 直觉:**8 个核 = 8 种探测器**(比如一个专门找竖线、一个专门找横线……),每张 feature map 输出一种特征的"响应热力图"。

### 知识点 1.2 特征图尺寸公式

```
输出尺寸 = (输入尺寸 - kernel_size + 2×padding) / stride + 1
```

默认 `padding=0, stride=1`,所以 `28×28` 经 `kernel_size=3` 变为 `26×26`。

> 口诀:**没 padding 就缩水,kernel 多大就少 (k-1) 圈**。

### 知识点 1.3 池化 (Pooling):降维 + 平移不变性

池化不学参数,只做"区域汇总"。最常用 **MaxPool2d(2)** —— 把 2×2 窗口的最大值留下,**尺寸减半**。

```python
pool = nn.MaxPool2d(kernel_size=2)

x = torch.randn(1, 8, 26, 26)
out = pool(x)
print(out.shape)   # torch.Size([1, 8, 13, 13]) —— 长宽各减半
```

> 直觉:**池化 = 局部"投票"保留最强响应**—— 即使边缘位置偏了一点,最大值还是能抓住。

### 知识点 1.4 经典 CNN 组装顺序

```python
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3),    # 28 → 26
            nn.ReLU(),
            nn.MaxPool2d(2),        # 26 → 13
            nn.Conv2d(16, 32, 3),   # 13 → 11
            nn.ReLU(),
            nn.MaxPool2d(2),        # 11 → 5
        )
        self.classifier = nn.Linear(32 * 5 * 5, 10)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)   # 展平
        return self.classifier(x)
```

> 口诀:**Conv-ReLU-Pool 三连,层层递进 —— 浅层看边缘,深层看语义**。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 给出输入 `1×1×28×28`,计算 `Conv2d(1, 8, kernel_size=3)` 输出 feature map 尺寸;再加 `MaxPool2d(2)`,最终多少? ⭐⭐ 手算 + 代码验证 (10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `conv.weight.data` 手动写入一个垂直边缘检测核(左列 -1、右列 +1),对一张手写数字图看 feature map,可视化"探测器"效果 (⭐⭐⭐,15 分钟)

> 巡场重点: 练习 1 学员常把"padding=0, stride=1"偷换成别的值,强调:**默认值就是 0 和 1,别想当然加 1**。

---

## 3. 第二讲(20 分钟) —— ResNet 残差连接:一条"高速公路"

### 知识点 3.1 为什么需要残差? 深层网络的退化问题

直觉上"56 层应该比 20 层好,毕竟多了 36 层可以兜底"。但实际上,**普通深层网络在训练集上表现反而更差** —— 不是过拟合,是"多余层学不到恒等映射,反而添乱"。

### 知识点 3.2 残差块:`F(x) + x`

普通块:`H(x) = F(x)` —— 让网络**从零**学目标映射。
残差块:`H(x) = F(x) + x` —— 让网络学**修正量**(残差),多学一层"补充一点"就行。

```python
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)

    def forward(self, x):
        residual = x              # 保存输入
        out = torch.relu(self.conv1(x))
        out = self.conv2(out)
        out = out + residual      # 残差连接!
        return torch.relu(out)
```

> 口诀:**F(x)+x 是"传送门",学不到新东西就原样送过去,绝不添乱**。
>
> 直觉:**残差块 = 学霸做作业:先看看参考答案(恒等映射),再改自己的错误(F(x)),比从零写一份靠谱得多**。

### 知识点 3.3 经典 ResNet 族

- ResNet-18 / 34 / 50 / 101 / 152 —— 数字=层数
- 18/34 用 BasicBlock(两个 3×3),50+ 用 Bottleneck(1×1 → 3×3 → 1×1)

## 4. 当堂练 2(20 分钟)

- 练习 3: `in_class/practice03.py` —— 给定一个 2×2 输入矩阵和一个 3×3 卷积核(padding=1),手算 `F(x) + x` 的前向传播数值例子(⭐⭐⭐,15 分钟)

> 巡场重点: 手算时学员常忘了 `+ residual` 这步,这就是"把 ResNet 当普通 Conv 用"的纸面版本 —— 指出后要求重算。

---

## 5. 第三讲(20 分钟) —— RNN / LSTM:序列建模直觉

### 知识点 5.1 RNN = 带"记忆"的神经元

普通网络:每份输入独立处理。RNN:**上一步的输出(隐藏状态)带入下一步**—— 就像读书,每个字的理解都基于前面的上下文。

```python
rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)
x = torch.randn(5, 3, 10)   # batch=5, seq_len=3, dim=10
out, h = rnn(x)
print(out.shape)   # [5, 3, 20] —— 每步都有一个输出
print(h.shape)     # [1, 5, 20] —— 最后的隐藏状态
```

### 知识点 5.2 LSTM:三个门控 = 遗忘、输入、输出

普通 RNN 长序列会"遗忘早期信息"(梯度消失)。LSTM 用三个门解决:

| 门 | 决定 | 类比 |
|---|---|---|
| 遗忘门 | 上一记忆丢掉多少 | 忘掉不重要的过去 |
| 输入门 | 当前信息记多少 | 记下新知识 |
| 输出门 | 本次输出告诉别人多少 | 说话留三分 |

```python
lstm = nn.LSTM(input_size=10, hidden_size=20, batch_first=True)
out, (h_n, c_n) = lstm(x)
# h_n: 隐藏状态,c_n: 细胞状态(长期记忆)
```

> 口诀:**LSTM 三扇门 —— 遗忘、输入、输出;长期记忆 c 是慢变量,短期 h 是快变量**。

## 6. 第四讲(20 分钟) —— 正则化四件套

### 知识点 6.1 Dropout:随机"打翻"神经元

训练时以概率 p 随机把神经元输出置 0,每次迭代随机失活不同子集 —— 迫使网络**不依赖任何单个神经元**。

```python
self.dropout = nn.Dropout(p=0.5)   # 50% 失活

# forward
x = self.dropout(x)
```

> 🔴 教学红线(eval 时 Dropout 会自动关,但很多人不信): `model.eval()` 内部把 Dropout 置为 identity;但如果你在 forward 里**手动**写了 `self.training` 判断就绕过了。建议永远让 nn.Dropout 自己处理,不要在 forward 里写 `if self.training:` 控制 dropout。

### 知识点 6.2 BatchNorm:给每层"标准化"

对每个 mini-batch 做 (x - mean) / std,再加可学参数 γ 和 β 恢复表达力 —— 稳定训练、允许更大学习率。

```python
self.bn = nn.BatchNorm1d(num_features=128)   # 全连接后
self.bn2d = nn.BatchNorm2d(num_features=64)  # 卷积后
```

### 知识点 6.3 权重衰减 (L2 正则)

```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
```

等价于在 loss 里加 `λ * ||w||²` —— 惩罚"大权重",鼓励参数小而平。

### 知识点 6.4 早停 (Day29 已讲,重申一遍)

验证集 loss 不再下降就停。四种正则化**可以组合使用**,但不要一次性全上 —— 定位问题时先减再增。

> 口诀:**Dropout 随机抽查,BatchNorm 稳输入,权重衰减不让参数飘,早停见好就收**。

## 7. 小项目(45 分钟)

- 项目: `mini_project/project01.py` —— 在 MNIST 上用 `nn.Conv2d` 搭一个简单 CNN
  - 架构: `Conv(1,32,3) → ReLU → MaxPool(2) → Conv(32,64,3) → ReLU → MaxPool(2) → FC(64*7*7, 10)`
  - 加 `nn.Dropout(0.5)` 在 FC 前
  - 训练 5 个 epoch
  - 对比 "有 Dropout vs 无 Dropout" 在测试集上的 acc
  - 目标:无 Dropout 约 99%,有 Dropout 约 99.1% - 看泛化差距 (⭐⭐⭐⭐)

> 巡场重点: 看学员是否把 MaxPool 后的尺寸算错 —— 28 → 14 → 7 不是 "28 → 26 → 13",因为 MaxPool 只看当前尺寸,"先 Conv 缩水再 Pool 折半"要分两步算。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. MaxPool 后尺寸算错:忘了 Conv 先缩水、Pool 再折半,直接套公式套错
  2. forward 里手动 if self.training 控制 dropout,绕过了 eval 自动关闭机制
  3. 同时打开所有正则化方法出问题,不知道是哪个导致 loss 不正常
- **作业说明**: 课后 `homework/task01.py`(把 MNIST CNN 加 BatchNorm 对比效果)、`homework/task02.py`(用 nn.LSTM 做一个简单字符序列预测),下节课前 10 分钟复盘。

---

## 易错点

1. **Conv 输出尺寸公式**: `(W - K + 2P) / S + 1`,默认 `P=0,S=1` → 输出 `= W - K + 1`。
2. **BatchNorm 放在 ReLU 前还是后**: 两种流派都行,主流是 `Conv → BN → ReLU`;重要的是 forward 顺序和声明顺序一致。
3. **Dropout 在 eval 时由 PyTorch 自动关闭**: 不要在 forward 里手动 `if self.training:` 控制dropout,绕过了 eval 自动关闭。
4. **RNN 的 batch_first=True**: PyTorch 默认 `batch_first=False`,输入是 `[seq_len, batch, dim]`,新手必踩坑。
5. **LSTM 返回元组 `(h_n, c_n)`**: 不要把 `h_n + c_n` 当输出;通常只用 `h_n` 或 `out`。
6. **ResNet 残差连接要求输入输出形状一致**: 维度不同时要用 1×1 Conv 做 projection 对齐。
7. **数据增强不属于模型**: RandomCrop / RandomHorizontalFlip 等应在 Dataset 的 `__getitem__` 里做,而不是 forward 里。

## 延伸题

- **(CNN 可视化, Grad-CAM 思路, ⭐⭐⭐⭐)**: 对 MNIST CNN 的最后一个 Conv 层做特征图可视化,看"模型到底在看哪里" —— 可解释性入门。
- **(手写字符级语言模型, Karpathy char-rnn, ⭐⭐⭐⭐)**: 用 LSTM 训练一个"读了金庸全集后生成金庸文风"的字符级模型 —— RNN 趣味项目。
- **(CIFAR-10 baseline with augmentation, ⭐⭐⭐)**: 在 CIFAR-10 上加 RandomCrop + HorizontalFlip 等数据增强,对比加/不加 augmentation 的 acc 差距 —— 数据增强的价值。
- **(消融实验基本功, ⭐⭐⭐⭐)**: 把今天学的四种正则化(Dropout / BN / 权重衰减 / 早停)做 2⁴ 种组合,矩阵式报告 acc —— 科学实验方法入门。
