"""
[难度: ⭐⭐]
[所属知识点: Perplexity 使用的红线检查]
[预计完成时间: 10 分钟]

写一个函数 audit_ppl_usage(train_texts, test_texts),
检查是否用训练集算 perplexity 这一红线违规。
规则:
 - train_texts 为空 -> 报错 "无训练数据"
 - test_texts 为空  -> 报红线警告 "禁止用训练集算 PPL"
 - 两者都有        -> 通过
请测试故意缺 test_texts 的 case,捕获红线警告。

示例:
    >>> audit_ppl_usage(["a"], [])
    ⚠ 红线: 禁止用训练集算 PPL,数据泄露!
"""

# ======================
# 学员代码区
# ======================
def audit_ppl_usage(train_texts, test_texts):
    # 检查 train/test 是否为空,
    # 返回字符串说明检查结果
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 只有训练集,没有测试集 -> 红线
    r1 = audit_ppl_usage(
        ["今天天气好", "机器学习"],
        []
    )
    print(f"测试1 -> {r1}")

    # 测试 2: 训练集测试集都有 -> 通过
    r2 = audit_ppl_usage(
        ["今天天气好"],
        ["明天下雨吗"]
    )
    print(f"测试2 -> {r2}")

    # 测试 3: 训练集为空 -> 报错
    r3 = audit_ppl_usage([], ["test"])
    print(f"测试3 -> {r3}")
