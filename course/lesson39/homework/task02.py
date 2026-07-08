"""
[难度: ⭐⭐⭐]
[所属知识点: QLoRA 配置方案]
[预计完成时间: 15 分钟]

题目描述:
不同的 GPU 硬件对应不同的 QLoRA 配置方案。
实现 QloraConfig.from_profile(profile),根据 profile 字符串
返回不同的 LoraConfig:
  - "A100":    r=64, lora_alpha=128, target_modules 包含全部 4 个
             注意力投影 (q_proj/k_proj/v_proj/o_proj),use_rslora=True
  - "消费级":  r=16, lora_alpha=32, target_modules 仅
             q_proj/v_proj, use_rslora=False
  - "入门卡":  r=8,  lora_alpha=16, target_modules 仅
             q_proj, use_rslora=False
  - 其他输入:   raise ValueError("未知配置方案: xxx")

示例:
    >>> cfg = QloraConfig.from_profile("消费级")
    r=16, alpha=32, modules=['q_proj', 'v_proj'],
    rslora=False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from peft import LoraConfig


class QloraConfig:
    """根据硬件 profile 返回合适的 LoraConfig。"""

    @staticmethod
    def from_profile(profile):
        pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: A100 大卡
    cfg1 = QloraConfig.from_profile("A100")
    assert cfg1.r == 64
    assert cfg1.lora_alpha == 128
    assert len(cfg1.target_modules) == 4
    assert cfg1.use_rslora is True
    print(f"A100: r={cfg1.r}, alpha={cfg1.lora_alpha}, "
          f"modules={cfg1.target_modules}, "
          f"rslora={cfg1.use_rslora}")

    # 测试 2: 消费级
    cfg2 = QloraConfig.from_profile("消费级")
    assert cfg2.r == 16
    assert cfg2.lora_alpha == 32
    assert list(cfg2.target_modules) == ["q_proj", "v_proj"]
    assert cfg2.use_rslora is False
    print(f"消费级: r={cfg2.r}, alpha={cfg2.lora_alpha}, "
          f"modules={cfg2.target_modules}, "
          f"rslora={cfg2.use_rslora}")

    # 测试 3: 入门卡
    cfg3 = QloraConfig.from_profile("入门卡")
    assert cfg3.r == 8
    assert cfg3.lora_alpha == 16
    assert list(cfg3.target_modules) == ["q_proj"]
    print(f"入门卡: r={cfg3.r}, alpha={cfg3.lora_alpha}")

    # 测试 4: 异常 profile
    try:
        QloraConfig.from_profile("未知硬件")
        print("未抛出异常 ✗")
    except ValueError as e:
        print(f"捕获异常: {e}")

    print("测试通过 ✓")
