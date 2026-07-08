"""
[难度: ⭐⭐]
[所属知识点: 文本清洗 (正则表达式)]
[预计完成时间: 10 分钟]

题目: 网页评论爬虫数据清洗
爬虫抓到的评论里混杂着 URL、HTML 标签和标点符号,
会干扰分词效果。请写一个 clean_text(text) 函数,
依次去除这三类噪声,返回干净的纯文本。

清洗规则:
    1. 去除 URL (http/https 开头)
    2. 去除 HTML 标签 (< xxx >)
    3. 去除标点符号和特殊字符(保留中文、英文、数字)

示例:
    >>> s = "好评! <br>http://taobao.com 质量很好"
    >>> clean_text(s)
    "好评 质量很好"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import re


def clean_text(text):
    """清洗文本: 去 URL / HTML 标签 / 标点"""
    # 第 1 步: 去除 URL
    text = re.sub(r'https?://\S+', '', text)
    # 第 2 步: 去除 HTML 标签
    text = re.sub(r'<[^>]+>', '', text)
    # 第 3 步: 去除标点和特殊字符
    text = re.sub(r'[^\w一-鿿]', ' ', text)
    # 合并多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 混合噪声评论
    dirty1 = "差评!<a href='#'>点击</a>http://spam.com 假货!"
    clean1 = clean_text(dirty1)
    print("清洗前:", dirty1)
    print("清洗后:", clean1)
    assert "http" not in clean1
    assert "<" not in clean1
    assert "差评" in clean1
    assert "假货" in clean1

    # 测试 2: 纯文本无噪声
    dirty2 = "这个商品真的很不错"
    clean2 = clean_text(dirty2)
    print("清洗前:", dirty2)
    print("清洗后:", clean2)
    assert clean2 == "这个商品真的很不错"
