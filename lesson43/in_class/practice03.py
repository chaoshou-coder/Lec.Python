"""
[难度: ⭐⭐]
[所属知识点: GGUF 文件名解析]
[预计完成时间: 10 分钟]

写一个函数 parse_gguf_name(filename),
从文件名中提取 模型名 / 参数量 / 量化格式,
返回 dict{model, params, quant}。
测试 3 个不同格式的文件名。

示例:
    >>> parse_gguf_name(
        "Qwen2-7B-Instruct-Q4_K_M.gguf"
    )
    {"model": "Qwen2-7B-Instruct",
     "params": "7B", "quant": "Q4_K_M"}
"""

# ======================
# 学员代码区
# ======================
import re

def parse_gguf_name(filename):
    # 用正则或字符串操作解析
    # 返回 dict,三个 key 必须存在
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 标准格式
    r1 = parse_gguf_name(
        "Qwen2-7B-Instruct-Q4_K_M.gguf"
    )
    print(f"测试1 -> {r1}")

    # 测试 2: 不同模型
    r2 = parse_gguf_name(
        "Llama-3-8B-Q8_0.gguf"
    )
    print(f"测试2 -> {r2}")

    # 测试 3: 复杂版本号
    r3 = parse_gguf_name(
        "DeepSeek-R1-14B-F16.gguf"
    )
    print(f"测试3 -> {r3}")
