"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 预训练模型选型 Model Selection]
[预计完成时间: 20 分钟]

实现 ModelSelector 类,有 recommend(task) 方法,
根据任务名返回一个字典:
{
  "model_name": "xxx/yyy",
  "load_class": "AutoModelForXxx",
  "reason": "一句话理由"
}
至少覆盖以下 5 个任务: "文本分类", "命名实体识别",
"文本生成", "问答", "翻译"。

示例:
    >>> sel = ModelSelector()
    >>> r = sel.recommend("文本分类")
    >>> print(r["model_name"])
    bert-base-chinese
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ModelSelector:
    def recommend(self, task):
        """根据任务名推荐预训练模型"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    sel = ModelSelector()
    tasks = [
        "文本分类", "命名实体识别", "文本生成",
        "问答", "翻译"
    ]
    # 测试 1: 遍历 5 个任务
    for t in tasks:
        r = sel.recommend(t)
        print(f"{t}: {r['model_name']}"
              f" | {r['load_class']}"
              f" | {r['reason']}")
    # 测试 2: 未知任务
    print(sel.recommend("图像分类"))
    pass
