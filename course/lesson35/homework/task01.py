"""
[难度: ⭐⭐]
[所属知识点: HF Pipeline 中文新闻分类]
[预计完成时间: 10 分钟]

加载 uer/roberta-base-finetuned-chinanews-chinese
的 text-classification pipeline,对一条中文新闻
做分类,打印 (label, score)。需要联网下载模型。

示例:
    >>> result = classify_news("苹果公司发布新款手机")
    >>> print(result)
    [{'label': '科技', 'score': 0.95}]
"""

from transformers import pipeline

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def classify_news(text):
    """用 pipeline 对中文新闻做分类"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 科技新闻
    r1 = classify_news("苹果公司发布新款手机")
    print("result1:", r1)
    # 测试 2: 体育新闻
    r2 = classify_news("中国男足晋级世界杯")
    print("result2:", r2)
    pass
