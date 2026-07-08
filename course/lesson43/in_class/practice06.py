"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 部署检查全流程]
[预计完成时间: 20 分钟]

写一个 DeployChecker 类,封装部署检查:
1. check_ollama_installed() -> bool
2. list_models() -> list[str]
3. recommend_quant(vram_gb, params_b) -> str
4. generate(model, prompt) -> str(带 try/except)
测试整个流程: 检查安装 -> 列模型 -> 推荐量化 -> 生成。

示例:
    >>> checker = DeployChecker()
    >>> checker.check_ollama_installed()
    True
    >>> checker.recommend_quant(8, 7e9)
    Q4_K_M
"""

# ======================
# 学员代码区
# ======================
import subprocess

class DeployChecker:
    def __init__(self):
        pass

    def check_ollama_installed(self):
        # subprocess.run(["ollama", "--version"])
        # 未安装返回 False
        pass

    def list_models(self):
        # ollama list,解析模型名列表
        # 未安装返回 []
        pass

    def recommend_quant(self, vram_gb, params_b):
        # 复用 select_quantization 逻辑
        pass

    def generate(self, model, prompt):
        # ollama chat 生成
        # 捕获异常友好返回
        pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    checker = DeployChecker()

    # 测试 1: 检查安装
    ok = checker.check_ollama_installed()
    print(f"Ollama 已安装? {ok}")

    # 测试 2: 列模型
    models = checker.list_models()
    print(f"本地模型: {models}")

    # 测试 3: 推荐量化
    q = checker.recommend_quant(8, 7e9)
    print(f"8GB + 7B -> {q}")

    # 测试 4: 生成
    out = checker.generate(
        "qwen2.5:0.5b", "你好"
    )
    print(f"生成结果: {out}")
