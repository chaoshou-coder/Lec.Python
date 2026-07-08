"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 模型雷达筛选]
[预计完成时间: 20 分钟]

实现 ModelRadar 类,hardcode 10 个常见 LLM 信息,提供
filter_by(license, lang, max_params) 方法筛选;用表格
打印结果,并对"中文创业公司 8G 卡"场景推荐 3 个合适
模型。

示例:
    >>> radar = ModelRadar()
    >>> radar.filter_by("apache-2.0", "zh", 7)
    [{'name': 'Qwen2.5-7B', ...}]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ModelRadar:
    """模型雷达:硬编码 10 个 LLM,支持按许可/语言/
    参数量筛选,并以表格打印推荐结果。"""

    def __init__(self):
        self.models = [
            {"name": "Qwen2.5-7B", "license": "apache-2.0",
             "lang": "zh", "params": 7},
            {"name": "Qwen2.5-1.5B", "license": "apache-2.0",
             "lang": "zh", "params": 1.5},
            {"name": "ChatGLM3-6B", "license": "other",
             "lang": "zh", "params": 6},
            {"name": "Baichuan2-7B", "license": "other",
             "lang": "zh", "params": 7},
            {"name": "DeepSeek-Coder-6.7B", "license": "other",
             "lang": "en", "params": 6.7},
            {"name": "Llama3-8B-Instruct", "license": "other",
             "lang": "en", "params": 8},
            {"name": "Mistral-7B", "license": "apache-2.0",
             "lang": "en", "params": 7},
            {"name": "Yi-6B", "license": "apache-2.0",
             "lang": "zh", "params": 6},
            {"name": "Phi-3-mini", "license": "mit",
             "lang": "en", "params": 3.8},
            {"name": "CodeLlama-7B", "license": "other",
             "lang": "en", "params": 7},
        ]

    def filter_by(self, license, lang, max_params):
        """按许可/语言/最大参数量筛选模型列表"""
        pass

    def print_table(self, rows):
        """以简易表格打印模型信息"""
        # 提示:表头 name/license/lang/params
        header = f"{'name':<22}{'license':<14}{'lang':<6}{'params'}"
        print(header)
        print("-" * len(header))
        for r in rows:
            print(f"{r['name']:<22}{r['license']:<14}"
                  f"{r['lang']:<6}{r['params']}")

    def recommend_8g_chinese_startup(self):
        """中文创业公司 8G 卡场景推荐 3 个模型"""
        # 8G 卡 <= 7B,中文,apache 优先
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    radar = ModelRadar()

    # 测试 1: filter_by apache/zh/7B
    rows = radar.filter_by("apache-2.0", "zh", 7)
    print("=== apache / zh / <=7B ===")
    radar.print_table(rows)
    assert len(rows) >= 2, "应至少 2 个模型"
    for r in rows:
        assert r["license"] == "apache-2.0"
        assert r["lang"] == "zh"
        assert r["params"] <= 7

    # 测试 2: 8G 卡场景推荐
    print("\n=== 8G 卡中文创业推荐 ===")
    top3 = radar.recommend_8g_chinese_startup()
    radar.print_table(top3)
    assert len(top3) == 3, "应推荐 3 个模型"
    print("所有测试通过")
    pass
