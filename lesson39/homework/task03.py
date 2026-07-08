"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 不同 rank 的 LoRA 显存对比可视化]
[预计完成时间: 20 分钟]

题目描述:
给定一个 base 模型 nn.Linear(1024, 1024),
实现 compare_peft_memory(base_model, r_list=[4, 8, 16, 32]),
对每个 r 值:
  1. 对该模型应用 LoRA (仅对该层, target_modules 对应命名),
     统计 trainable 参数量
  2. 在同一文本柱状图中用 ▇ 符号可视化,每 5000 参数打印一个 ▇
  3. 返回字典 {r: trainable_params}

要求柱子右对齐,格式如:
  r= 4 | ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ | 8192
  r= 8 | ▇▇▇▇...             | 16384

示例:
    >>> model = nn.Linear(1024, 1024)
    >>> result = compare_peft_memory(model, [4, 8, 16, 32])
    r= 4 | ▇▇▇▇▇▇▇▇           | 8192
    r= 8 | ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇   | 16384
    ...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch.nn as nn
from peft import LoraConfig, get_peft_model


class SimpleModel(nn.Module):
    """单层线性模型,命名 layer 以便 LoRA 定位。"""

    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(1024, 1024)

    def forward(self, x):
        return self.layer(x)


def compare_peft_memory(base_model, r_list):
    """对比不同 r 下的 trainable 参数量并可视化。

    返回: dict, {r: trainable_params}
    """
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    model = SimpleModel()
    result = compare_peft_memory(model, [4, 8, 16, 32])

    # 验证返回值
    expected = {4: 8192, 8: 16384, 16: 32768, 32: 65536}
    for r, params in expected.items():
        assert result[r] == params, (
            f"r={r} 期望 {params}, 实际 {result[r]}"
        )
    print(f"\n返回结果: {result}")

    # 测试边界: r=0
    result2 = compare_peft_memory(SimpleModel(), [0])
    assert result2[0] == 0, f"r=0 应返回 0: {result2[0]}"
    print(f"r=0 边界: {result2}")

    # 测试边界: 空列表
    result3 = compare_peft_memory(SimpleModel(), [])
    assert result3 == {}, f"空列表应返回空字典: {result3}"
    print(f"空列表边界: {result3}")
    print("测试通过 ✓")
