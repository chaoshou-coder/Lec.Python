"""
[难度: ⭐⭐]
[所属知识点: 文本清洗 + jieba 分词]
[预计完成时间: 10 分钟]

给定以下 5 句电商评论(包含 URL、数字、标点、HTML 标签等噪声),
请编写 clean 与 tokenize pipeline:
  1. 使用正则表达式去除 URL、HTML 标签、数字、英文、标点符号,
     只保留中文字符;
  2. 对清洗后的每句用 jieba.lcut 进行分词;
  3. 打印每句的 token 数。

示例:
    >>> sentences = ["<p>好评!</p>..."]
    >>> # 清洗后: 好评 推荐
    >>> # token 数: 2
"""

import re
import jieba

# 含有噪声的 5 句电商评论
sentences = [
    "<p>好评! 推荐~  https://shop.com/item/12345</p>",
    "这件衣服质量2026很好, 价格只要99元!",
    "差评！物流极差，送到都破了😭😭",
    "Visit https://mall.cn/p/888 买它!!!",
    "【促销】#双11# 打折@所有人 快抢",
]

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def clean(text: str) -> str:
    """只保留中文字符, 其余全部去除。"""
    # 去除 HTML 标签
    text = re.sub(r"<[^>]+>", "", text)
    # 去除 URL
    text = re.sub(r"https?://\S+", "", text)
    # 去除非中文字符(保留汉字)
    text = re.sub(r"[^一-鿿]", "", text)
    return text


def tokenize(text: str) -> list:
    """对清洗后的文本调用 jieba.lcut 分词。"""
    return jieba.lcut(text)


def pipeline(sents: list) -> None:
    """清洗 + 分词 + 打印每句 token 数。"""
    for i, s in enumerate(sents, start=1):
        cleaned = clean(s)
        tokens = tokenize(cleaned)
        # 去除停用词: 单字且为"的/了/是"等(可留空)
        print(f"第{i}句 token 数: {len(tokens)} -> {tokens}")


# 运行清洗 + 分词 pipeline
pipeline(sentences)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 清洗后不应含 URL、数字、标点
    raw = "<p>推荐! https://a.com/123 价格99元</p>"
    out = clean(raw)
    assert "http" not in out, "URL 未清除"
    assert "99" not in out, "数字未清除"
    assert len(out) > 0, "清洗后不应为空"
    print(f"测试1通过: 清洗结果 = {out}")

    # 测试 2: 分词返回 list 且 token 数正确
    tokens = tokenize("好评推荐")
    assert isinstance(tokens, list), "分词应返回 list"
    assert len(tokens) >= 2, "token 数应 >= 2"
    print(f"测试2通过: 分词结果 = {tokens}")
