"""
[难度: ⭐⭐]
[所属知识点: 嵌入维度与批量编码]
[预计完成时间: 10 分钟]

场景: 实现 compare_models 函数,分别加载两个模型,
对同一句"自然语言处理"编码,返回两个模型的嵌入维度 (int, int)。

示例:
    >>> d1, d2 = compare_models()
    >>> isinstance(d1, int) and isinstance(d2, int)
    True
"""

import numpy as np
from sentence_transformers import SentenceTransformer


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def compare_models() -> tuple:
    """加载两个模型,对固定句子编码,返回嵌入维度元组"""
    sentence = "自然语言处理"
    model_name_a = "all-MiniLM-L6-v2"
    model_name_b = "paraphrase-multilingual-MiniLM-L12-v2"
    # TODO: 加载 model_name_a,对 sentence 编码,记录维度 d1
    # TODO: 加载 model_name_b,对 sentence 编码,记录维度 d2
    # TODO: 返回 (d1, d2)
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 返回两个正整数
    d1, d2 = compare_models()
    assert isinstance(d1, int) and d1 > 0, "d1 应为正整数"
    assert isinstance(d2, int) and d2 > 0, "d2 应为正整数"
    print(f"测试 1 通过: d1={d1}, d2={d2}")

    # 测试 2: 同一模型再次调用,维度一致
    d1_again, _ = compare_models()
    assert d1 == d1_again, "同一模型维度应相同"
    print("测试 2 通过: 维度一致")
