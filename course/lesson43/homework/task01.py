"""
[难度: ⭐⭐]
[所属知识点: GGUF 文件解析与排序]
[预计完成时间: 10 分钟]

给定 10 个 GGUF 文件名,用 parse_gguf_name 解析,
并按显存从小到大排序打印。
需要复用 lesson43 的 parse_gguf_name 函数。

示例:
    >>> run()
    Qwen2-7B-Q2_K     -> 2.36 GB
    Qwen2-7B-Q4_K_M   -> 4.20 GB
    ...
"""

# ======================
# 学员代码区
# ======================
import re

def parse_gguf_name(filename):
    # 复用文件名解析逻辑
    pass

def gguf_size(params_b, quant):
    # 复用大小估算逻辑
    pass

def run():
    files = [
        "Qwen2-7B-Instruct-Q8_0.gguf",
        "Qwen2-7B-Instruct-Q2_K.gguf",
        "Qwen2-7B-Instruct-Q4_K_M.gguf",
        "Qwen2-7B-Instruct-F16.gguf",
        "Llama-3-8B-Q4_K_M.gguf",
        "Llama-3-8B-Q2_K.gguf",
        "Llama-3-8B-F16.gguf",
        "Qwen2-1.5B-Q4_K_M.gguf",
        "Qwen2-1.5B-F16.gguf",
        "Qwen2-1.5B-Q2_K.gguf",
    ]
    # 解析 -> 计算大小 -> 排序打印
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 单个文件
    r = parse_gguf_name("Qwen2-7B-Q4_K_M.gguf")
    print(f"单文件解析: {r}")

    # 测试 3: 边界 - 未知量化
    try:
        infos = re.findall(r"\d+(?:\.\d+)?[BbQq]", "X-99B-XYZ.gguf")
        print(f"量化识别中间结果: {infos}")
    except Exception as e:
        print(f"异常: {e}")
