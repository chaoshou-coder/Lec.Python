"""
[难度: ⭐⭐⭐]
[所属知识点: LoRA 配置预设]
[预计完成时间: 15 分钟]

题目描述:
实现 LoraConfigFactory.role(role),根据不同的使用场景
返回不同的 LoraConfig:
  - "省显存":  r=4,  lora_alpha=8,  target_modules=["q_proj"]
  - "平衡":    r=8,  lora_alpha=16, target_modules=["q_proj","v_proj"]
  - "高精度":  r=32, lora_alpha=64, target_modules=["q_proj","k_proj",
                                                  "v_proj","o_proj"]
  - 其他输入:  抛出 ValueError("未知角色: xxx")

示例:
    >>> cfg = LoraConfigFactory.role("平衡")
    r=8, alpha=16, modules=['q_proj', 'v_proj']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from peft import LoraConfig


class LoraConfigFactory:
    """根据角色预设返回 LoraConfig。"""

    @staticmethod
    def role(role):
        pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 省显存
    cfg1 = LoraConfigFactory.role("省显存")
    assert cfg1.r == 4
    assert cfg1.lora_alpha == 8
    print(f"省显存: r={cfg1.r}, alpha={cfg1.lora_alpha}, "
          f"modules={cfg1.target_modules}")

    # 测试 2: 平衡
    cfg2 = LoraConfigFactory.role("平衡")
    assert cfg2.r == 8
    assert cfg2.lora_alpha == 16
    print(f"平衡: r={cfg2.r}, alpha={cfg2.lora_alpha}, "
          f"modules={cfg2.target_modules}")

    # 测试 3: 高精度
    cfg3 = LoraConfigFactory.role("高精度")
    assert cfg3.r == 32
    assert cfg3.lora_alpha == 64
    assert len(cfg3.target_modules) == 4
    print(f"高精度: r={cfg3.r}, alpha={cfg3.lora_alpha}, "
          f"modules={cfg3.target_modules}")

    # 测试 4: 异常角色
    try:
        LoraConfigFactory.role("未知角色")
        print("未抛出异常 ✗")
    except ValueError as e:
        print(f"捕获异常: {e}")

    print("测试通过 ✓")
