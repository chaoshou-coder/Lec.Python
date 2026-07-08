"""
[难度: ⭐⭐⭐]
[所属知识点: 场景化模型选型]
[预计完成时间: 15 分钟]

实现 choose_model_for_scenario(scenario) 函数,根据场景
"写公众号文案"/"客服对话"/"代码补全" 按许可/显存/
中文打分,返回最佳模型+理由。

示例:
    >>> choose_model_for_scenario("写公众号文案")
    ('Qwen2.5-7B', '中文强,apache 许可')
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def choose_model_for_scenario(scenario):
    """根据场景返回 (最佳模型, 理由)"""
    # 提示:可硬编码候选模型字典,按场景关键字匹配
    candidates = {
        "写公众号文案": [
            ("Qwen2.5-7B", "apache 许可,中文强,低显存"),
            ("ChatGLM3-6B", "中文强,但需 8G 显存"),
        ],
        "客服对话": [
            ("Qwen2.5-1.5B", "轻量快,apache 许可"),
            ("Baichuan2-7B", "中文好,但许可受限"),
        ],
        "代码补全": [
            ("DeepSeek-Coder-6.7B", "代码专项强"),
            ("CodeLlama-7B", "通用代码,met AI 许可"),
        ],
    }
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: "写公众号文案"
    model, reason = choose_model_for_scenario("写公众号文案")
    print("文案场景 ->", model, "|", reason)
    assert model, "应返回一个模型"
    assert "Qwen" in model or "GLM" in model, "应选中文模型"

    # 测试 2: "客服对话" 和 "代码补全"
    for s in ["客服对话", "代码补全"]:
        m, r = choose_model_for_scenario(s)
        print(f"{s} -> {m} | {r}")
        assert m and r, f"{s} 应返回模型与理由"
    print("所有测试通过")
    pass
