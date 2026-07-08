"""
[难度: ⭐⭐]
[所属知识点: 监督 vs 无监督分类]
[预计完成时间: 10 分钟]

给定一组数据集描述(字典列表),写一个函数
`classify_problem(datasets)`,返回每个数据集的类型:
"监督学习" 或 "无监督学习"。

判断规则:
- label 字段不为 None 且不为空字符串 → 有标签 → "监督学习"
- label 字段为 None 或为空字符串 → 无标签 → "无监督学习"

返回与输入等长的字符串列表。

数据集示例:
    [
        {"name": "鸢尾花",   "label": "species"},
        {"name": "客户分群", "label": None},
        {"name": "房价预测", "label": "price"}
    ]

示例:
    >>> classify_problem([
    ...     {"name": "鸢尾花",   "label": "species"},
    ...     {"name": "客户分群", "label": None}
    ... ])
    ['监督学习', '无监督学习']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 三个数据集的混合情况
    # datasets1 = [
    #     {"name": "鸢尾花",   "label": "species"},
    #     {"name": "客户分群", "label": None},
    #     {"name": "房价预测", "label": "price"},
    # ]
    # print(classify_problem(datasets1))
    # 应输出: ['监督学习', '无监督学习', '监督学习']
    #
    # 测试 2: 空列表,返回空列表(边界情况)
    # print(classify_problem([]))
    # 应输出: []
    #
    # 测试 3: 空字符串标签视为无标签
    # datasets3 = [
    #     {"name": "文本聚类", "label": ""},
    #     {"name": "手写数字", "label": "digit"},
    # ]
    # print(classify_problem(datasets3))
    # 应输出: ['无监督学习', '监督学习']
    pass
