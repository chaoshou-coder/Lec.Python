"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 异常处理综合]
[预计完成时间: 30 分钟]

题目描述:
编写一个函数 `safe_process(path)`,
读取 JSON 文件并返回其中的 "data" 键对应的值。
需要处理以下异常:
- FileNotFoundError: 提示"文件不存在"
- json.JSONDecodeError: 提示"JSON 解析错误"
- KeyError: 提示"键 data 不存在"

示例:
    >>> safe_process("data.json") → 返回 data 的值
    >>> safe_process("not_exist.json") → 提示"文件不存在"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常文件
    # 测试 2: 文件不存在
    # 测试 3: JSON 格式错误
    # 测试 4: 缺少 data 键
    pass
