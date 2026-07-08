"""
[难度: ⭐]
[所属知识点: Ollama 命令行调用]
[预计完成时间: 5 分钟]

用 subprocess.run(["ollama", "list"], ...) 调用命令,
列出本地已安装的模型。
若 Ollama 未安装,try/except 友好提示安装方式。
提示: 命令不存在时抛 FileNotFoundError。

示例:
    >>> run()
    NAME            ID      SIZE
    qwen2.5:0.5b    ...
"""

# ======================
# 学员代码区
# ======================
import subprocess

def run():
    # 命令行调用 ollama list
    # 捕获 stdout 并打印
    # 若未安装,提示 "请先安装 Ollama: ..."
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 验证 subprocess 调用结构
    try:
        r = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        print(f"returncode = {r.returncode}")
    except FileNotFoundError:
        print("Ollama 未安装,请访问 ollama.com")
    except Exception as e:
        print(f"异常: {e}")
