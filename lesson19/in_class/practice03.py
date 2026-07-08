"""
[难度: ⭐⭐]
[所属知识点: LabelEncoder]
[预计完成时间: 10 分钟]

题目描述:
手写 `my_label_encode(labels)` 实现标签编码。
输入 ["猫", "狗", "猫", "鸟", "狗"],
返回编码数组和对应类别字典。
类别按 Unicode 码点排序(即 sorted 默认顺序)。

示例:
    >>> encoded, cats = my_label_encode(["猫", "狗", "猫", "鸟", "狗"])
    >>> encoded = array([1, 0, 1, 2, 0])
    >>> cats = ["狗", "猫", "鸟"]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def my_label_encode(labels):
    """手写标签编码:按字母顺序分配整数编号"""
    # 去重并按字母顺序排序得到类别列表
    categories = sorted(set(labels))
    # 构建类别到整数的映射字典
    mapping = {cat: idx for idx, cat in enumerate(categories)}
    # 将原始标签转换为整数编码
    encoded = np.array([mapping[lab] for lab in labels])
    return encoded, categories


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常情况
    labels = ["猫", "狗", "猫", "鸟", "狗"]
    encoded, cats = my_label_encode(labels)
    print("测试1 - 编码结果:", encoded)
    print("测试1 - 类别列表:", cats)

    # 测试 2: 只有一个类别
    encoded2, cats2 = my_label_encode(["苹果", "苹果", "苹果"])
    print("测试2 - 单一类别:", encoded2, cats2)
