"""
[难度: ⭐⭐⭐]
[所属知识点: 封装 sentiment pipeline 为类]
[预计完成时间: 15 分钟]

实现 SentimentAnalyzer 类,接收任意 HF 模型名,提供
predict(texts) 方法返回每句话的 label 列表。
注意:运行需联网下载模型。

示例:
    >>> analyzer.predict(["很好","很差"])
    ['LABEL_1', 'LABEL_0']
"""

from transformers import pipeline

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两条输入
    # 测试 2: 含中性/边界输入
    pass
