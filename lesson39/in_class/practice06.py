"""
[难度: ⭐⭐⭐⭐]
[所属知识点: LoRA 生命周期管理]
[预计完成时间: 20 分钟]

题目描述:
实现一个 LoRAManager 类,封装 LoRA 的完整生命周期:
  1. __init__(self, model): 存储原始模型,记录初始可训参数数
  2. wrap_model(self, r=8): 对模型所有线性层应用 LoRA,
     返回 peft 模型,并打印包装后的可训练参数占比
  3. merge_and_unload(self): 将 LoRA 权重合并回基座模型,
     返回普通 nn.Module,并验证合并后所有参数 requires_grad=True
  4. get_memory_saving(self): 返回 LoRA 节省的显存百分比
     (公式: 1 - trainable_params / total_params, 保留 2 位小数)

用 3 层 MLP 模型 (Linear(32,64)->ReLU->Linear(64,64)
->ReLU->Linear(64,10)) 进行测试,分别调用以上方法。

示例:
    >>> mgr = LoRAManager(model)
    >>> peft_model = mgr.wrap_model(r=8)
    可训练占比: ...%
    >>> merged = mgr.merge_and_unload()
    合并完成, 所有参数可训练: True
    >>> mgr.get_memory_saving()
    95.23
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch.nn as nn
from peft import LoraConfig, get_peft_model


class ThreeLayerMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(32, 64)
        self.relu1 = nn.ReLU()
        self.layer2 = nn.Linear(64, 64)
        self.relu2 = nn.ReLU()
        self.layer3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.relu1(self.layer1(x))
        x = self.relu2(self.layer2(x))
        return self.layer3(x)


class LoRAManager:
    """管理 LoRA 包装、合并与显存统计。"""

    def __init__(self, model):
        self.original_model = model
        self.peft_model = None
        # 计算总参数量
        self.total_params = sum(
            p.numel() for p in model.parameters()
        )

    def wrap_model(self, r=8):
        """对所有 Linear 层应用 LoRA。"""
        pass

    def merge_and_unload(self):
        """合并 LoRA 权重并返回普通模型。"""
        pass

    def get_memory_saving(self):
        """返回节省的显存百分比 (float)。"""
        pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    model = ThreeLayerMLP()
    mgr = LoRAManager(model)

    # 测试 wrap
    peft_model = mgr.wrap_model(r=8)
    assert peft_model is not None, "包装失败"
    print(f"总参数量: {mgr.total_params}")

    # 测试显存节省
    saving = mgr.get_memory_saving()
    assert saving > 0, f"显存节省应为正数: {saving}"
    print(f"显存节省: {saving}%")

    # 测试合并
    merged = mgr.merge_and_unload()
    all_requires_grad = all(
        p.requires_grad for p in merged.parameters()
    )
    assert all_requires_grad, "合并后所有参数应可训练"
    print("合并完成, 所有参数可训练: True")
    print("测试通过 ✓")
