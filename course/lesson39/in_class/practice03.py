"""
[难度: ⭐⭐]
[所属知识点: 将 LoRA 应用到模型]
[预计完成时间: 10 分钟]

题目描述:
构建一个简单的 dummy 模型 nn.Linear(64, 64),
使用 peft 的 get_peft_model 对它应用 LoRA (r=8,
target_modules=["linear"], 注意给 module 起名叫 "linear"),
然后调用 model.print_trainable_parameters() 打印
可训练参数与总参数的比例。

提示:
  model = DummyModel()  # forward 返回 x
  config = LoraConfig(r=8, target_modules=["linear"])
  peft_model = get_peft_model(model, config)

示例:
    >>> apply_lora_to_dummy()
    trainable params: 1024 || all params: 4160
    || trainable%: 24.6154
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch.nn as nn
from peft import LoraConfig, get_peft_model


class DummyModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 关键: 命名必须与 target_modules 对应
        self.linear = nn.Linear(64, 64)

    def forward(self, x):
        return self.linear(x)


def apply_lora_to_dummy():
    """对 dummy 模型应用 LoRA 并打印可训练参数信息。"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    apply_lora_to_dummy()
    # 预期 trainable params = 64*8 + 8*64 = 1024
    print("测试通过 ✓")
