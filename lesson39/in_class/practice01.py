"""
[难度: ⭐]
[所属知识点: LoraConfig 基础配置]
[预计完成时间: 5 分钟]

题目描述:
从 peft 库导入 LoraConfig,实例化一个配置对象,
设置 r=16, lora_alpha=32,
target_modules=["q_proj", "v_proj"],
然后打印这三个参数的值。

示例:
    >>> config = build_lora_config()
    r=16, lora_alpha=32,
    target_modules=['q_proj', 'v_proj']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from peft import LoraConfig


def build_lora_config():
    """返回一个配置好的 LoraConfig 对象。"""
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    cfg = build_lora_config()
    assert cfg.r == 16, f"r 应为 16, 实际为 {cfg.r}"
    assert cfg.lora_alpha == 32, (
        f"lora_alpha 应为 32, 实际为 {cfg.lora_alpha}"
    )
    assert list(cfg.target_modules) == ["q_proj", "v_proj"], (
        f"target_modules 不匹配: {cfg.target_modules}"
    )
    print(
        f"r={cfg.r}, lora_alpha={cfg.lora_alpha}, "
        f"target_modules={cfg.target_modules}"
    )
    print("测试通过 ✓")
