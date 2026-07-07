# Day31 · 迁移学习 + DL 项目

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day30 已掌握 CNN 架构、训练循环 5 步公式、正则化四件套、MNIST CNN 实战
> 关键问题:ImageNet 用 140 万张图训练 1000 类,我要识别猫/狗/鸟,难道也要从零训练 140 万张?本节给出答案:**不需要**。用别人的预训练 backbone + 自己的小数据做迁移学习,用 1% 的算力达到 90% 的效果。最后在 CIFAR-10 上跑完一个完整的 DL 项目闭环。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— CNN 的卷积核和池化各解决什么问题?ResNet 残差连接的核心公式是什么?正则化四件套是哪四个? 目的: 唤醒 CNN/正则化记忆,为"站在巨人肩膀上"埋伏笔。
- **赏玩 demo**(3 分钟): 展示 ImageNet 1000 类图片(鸟/狗/猫/蝴蝶……),问"你想从零训练识别这 1000 类,会花多少钱?几个月?"引出:**ImageNet 预训练一次 ≈ 几千美元 · 几天 GPU 时间,但 PyTorch 免费让你下载权重,你只需在最后一层改一改就够了**—— 这就是迁移学习。

---

## 1. 第一讲(25 分钟) —— 预训练模型:从 torchvision.models 开宝箱

### 知识点 1.1 一行代码拿到巨头们的劳动成果

```python
import torchvision.models as models

# ResNet-18:18 层,1100 万参数
resnet18 = models.resnet18(pretrained=True)

# VGG-16:16 层,1.38 亿参数(巨大)
vgg16 = models.vgg16(pretrained=True)
```

> 口诀:** pretrained=True 下载权重,pretrained=False 只搭骨架**。

### 知识点 1.2 看模型结构:.fc 是分类头

```python
print(resnet18)
# ...
# (fc): Linear(in_features=512, out_features=1000, bias=True)
```

**512 → 1000** 这个 `fc` 层就是分类头:把 backbone 提取的 512 维特征映射到 1000 类概率,要迁移到 C 类任务就改成 **512 → C**。

### 知识点 1.3 `named_parameters`:逐层检查 name 与 shape

```python
for name, param in resnet18.named_parameters():
    print(name, param.shape)
    # conv1.weight      [64, 3, 7, 7]
    # bn1.weight        [64]
    # layer1.0.conv1.weight [64, 64, 3, 3]
    # ...
    # fc.weight          [1000, 512]
```

> 🔴 教学红线(pretrained 已弃用 vs weights 新 API): PyTorch 1.13 后用 `weights="IMAGENET1K_V1"` 代替 `pretrained=True`,新版本写 `pretrained=True` 会告警。教师可根据环境选版本;但要指出告警的存在。

### 知识点 1.4 迁移学习的经济账

| 方案 | 数据量 | 训练时间 | 最终准确率 |
|---|---|---|---|
| 从零(ImageNet) | 140 万张 | 几天(多卡) | ~75% |
| 从零(CIFAR-10) | 5 万张 | 几小时 | ~80% |
| **迁移(ImageNet→CIFAR-10)** | 5 万张 | **十几分钟** | **~90%** |

> 口诀:**站在巨人肩膀上 —— 用 ImageNet 学到的通用特征(边缘、纹理、形状),只需在小数据上微调分类头**。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 加载 `resnet18(pretrained=True)`,打印 `named_parameters`,确认最后一层输出维度;数一数模型总参数 (数 `param.numel()` 求和) ⭐⭐ (10 分钟)
- 练习 2: `in_class/practice02.py` —— 给一张小猫图做预处理的完整流水线(`Resize(256)` → `CenterCrop(224)` → `ToTensor()` → `Normalize(...)`),送进 resnet18 推理,取 `torch.topk(5)` 看 top5 类别 (⭐⭐⭐,15 分钟)

> 巡场重点: 看学员是否做了 ImageNet 标准化 `Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])` —— 忘做标准化,模型会被"亮度奇怪"的输入搞错位。

---

## 3. 第二讲(25 分钟) —— 迁移学习三步骤

### 知识点 3.1 Step 1:冻结 backbone

把所有 backbone 参数的 `requires_grad` 设为 False,这样 backward 不会计算它们的梯度,**不会更新** —— 只训分类头。

```python
for param in resnet18.parameters():
    param.requires_grad = False
```

### 知识点 3.2 Step 2:替换分类头

```python
num_classes = 10   # CIFAR-10 有 10 类
resnet18.fc = nn.Linear(512, num_classes)
```

替换后,**新 fc 层默认 `requires_grad=True`**,只有它会更新。

### 知识点 3.3 Step 3:只训练分类头

```python
# 优化器只传"需要梯度"的参数(不传 frozen 的)
optimizer = torch.optim.Adam(
    filter(lambda p: p.requires_grad, resnet18.parameters()),
    lr=1e-3
)

# 或者直接传 fc 层的参数:
optimizer = torch.optim.Adam(resnet18.fc.parameters(), lr=1e-3)
```

> 口诀:**先冻后换 —— 不让 backbone 动,只练新脑袋**。

### 知识点 3.4 微调 (Fine-tuning):解冻后面几层

冻结 backbone 适合"小数据、和 ImageNet 分布接近"。如果你数据量大,可以**解冻后几层**(比如 layer3、layer4),用小 lr 微调:

```python
# 解冻 layer4 + fc
for name, param in resnet18.named_parameters():
    if "layer4" in name or "fc" in name:
        param.requires_grad = True
    else:
        param.requires_grad = False

# 微调 lr 设小:分类头 1e-3,backbone 1e-5
optimizer = [
    {"params": resnet18.fc.parameters(), "lr": 1e-3},
    {"params": resnet18.layer4.parameters(), "lr": 1e-5},
]
```

> 🔴 教学红线(微调 lr 过大): 解冻的 backbone 如果用和分类头一样的大学习率,会把 ImageNet 学好的通用特征"洗白" —— 必须小 lr,比如 `1e-5`。
>
> 口诀:**微调是把"已有知识"稍作修整,不是从零推倒 —— lr 要小**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在 dummy 数据(随机 3×224×224 图 + 随机标签)上实现"冻结 → 替换 fc → 训练 1 个 epoch"完整流程,打印 loss 下降值 (⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 故意把冻结代码漏掉,观察参数量仍是 1100 万;补上后观察 `sum(p.requires_grad)` 从 1100 万降到 5120 (fc 的参数) (⭐⭐⭐,10 分钟)

> 巡场重点: 看学员是否有"冻结顺序错" —— 先替换 fc 再冻结,新 fc 会被冻住;**必须先 freeze 再换 fc**(或替换后再把 fc 设 `requires_grad=True`)。

---

## 5. 第三讲(20 分钟) —— 完整 DL 项目 Pipeline

### 知识点 5.1 五步流水线

一个工业级 DL 项目按这个顺序整:

```
数据 → 模型 → 训练 → 评估 → 保存
 1      2      3      4      5
```

### 知识点 5.2 每步职责

| 步 | 做什么 | 关键代码 |
|---|---|---|
| 1 数据 | Dataset + DataLoader + 增强 | `transforms.Compose(...)` |
| 2 模型 | 加载预训练 + 替换 fc + 冻层 | `model.fc = nn.Linear(...)` |
| 3 训练 | 标准 5 步 + 验证 + 日志 | `for epoch: train → eval` |
| 4 评估 | 测试集 acc / 混淆矩阵 | `torch.no_grad()` |
| 5 保存 | 存字典 / 整个模型 / checkpoint | `torch.save(model.state_dict(), ...)` |

### 知识点 5.3 保存与加载

```python
# 保存(state_dict 最通用)
torch.save(model.state_dict(), "resnet18_cifar10.pt")

# 加载:先搭同样骨架,再读字典
model = models.resnet18()
model.fc = nn.Linear(512, 10)
model.load_state_dict(torch.load("resnet18_cifar10.pt"))
model.eval()
```

> 口诀:**save 只存 weights,load 时先搭同样骨架再填肉 —— 不存架构,换机器也能恢复**。
>
> 🔴 教学红线(忘记 model.eval()): 加载后直接推理,忘记调 `model.eval()`,Dropout 仍在工作 —— 推理结果每次不一样。

## 6. 小项目:CIFAR-10 图像分类完整项目(45 分钟)

- 项目: `mini_project/project01.py` —— 完整可运行脚本
  - 数据: `torchvision.datasets.CIFAR-10` + augmentation
    - `RandomCrop(32, padding=4)` + `RandomHorizontalFlip()` + `Normalize(...)`
  - 模型: `resnet18` 迁移学习
    - 预处理: resize 224 (ResNet 原设计输入)
    - 冻结 backbone,替换 fc: `512 → 10`
  - 训练: Adam lr=1e-3,10 epoch
  - 评估: 测试集 acc
  - 目标: **acc > 85%** (⭐⭐⭐⭐⭐)

> 巡场重点: 看学员是否**标准化时用了 ImageNet 的 mean/std,而不是 CIFAR-10 的** —— ResNet 在 ImageNet 上预训练,输入应该按 ImageNet 分布做 Normalize。

---

## 7. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 先替换 fc 再冻结 backbone,新 fc 一起被冻住,等于"白训"
  2. 微调时 backbone lr 和分类头 lr 一样大,把 ImageNet 知识洗白
  3. 加载模型后忘调 model.eval(),推理阶段 Dropout 仍在工作
- **作业说明**: 课后 `homework/task01.py`(在 CIFAR-100 上复现迁移学习,acc > 70%)、`homework/task02.py`(在 Kaggle 猫狗数据集上做二分类迁移学习),下节课前 10 分钟复盘。

---

## 易错点

1. **冻结顺序错**: `先 freeze 再换 fc`,否则新 fc 也被冻;或换完后显式 `fc.requires_grad = True`。
2. **微调 lr 过大**: backbone 和分类头要设不同 lr(比如 backbone 1e-5,fc 1e-3),否则预训练权重被洗白。
3. **ImageNet Normalize 参数**: 迁移学习时输入必须按 ImageNet 的 mean/std 做标准化,而不是当前数据集的。
4. **加载权重忘 eval**: `load_state_dict` 后必须 `model.eval()`,否则 Dropout/BN 行为不正常。
5. **输入尺寸不匹配**: ResNet 原设计接受 224×224,CIFAR-10 是 32×32 —— 必须 `Resize(224)` 上采样。
6. **小数据 + 微调后几层 = 过拟合**: 数据少时就只训分类头(全部冻结),不要贪多。
7. **`torch.save` 不存架构**: 只存 state_dict,换机器要先搭同样骨架再 load。

## 延伸题

- **(GAP 替代 FC, NiN 思路, ⭐⭐⭐)**: 把 ResNet 最后 fc 换成 `nn.AdaptiveAvgPool2d(1)` + `nn.Linear(512, 10)`,对比二者参数量 —— 理解"全局平均池化减少参数"。
- **(Kaggle 猫狗二分类完整版, ⭐⭐⭐⭐)**: 用 Kaggle Dogs vs Cats 数据集做迁移学习 + 早停 + 模型集成,目标是 top5% —— 巩固全流程。
- **(Grad-CAM 可视化, ⭐⭐⭐⭐)**: 对 CIFAR-10 的迁移学习模型做 Grad-CAM,看"模型到底在看哪里" —— 可解释性第一课。
- **(解冻策略时间表, discriminative lr, ⭐⭐⭐⭐)**: 实现"每 5 epoch 解冻一层"的渐进解冻策略,对比"全冻后换"和"全解冻"的 acc 差异 —— 微调高级技巧。
