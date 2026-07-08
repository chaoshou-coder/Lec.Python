"""
[难度: ⭐⭐⭐⭐]
[所属知识点: ML 项目全流程]
[预计完成时间: 20 分钟]

在动手写模型之前, 先规划流程是良好的工程习惯。请你实现
ml_project_plan(problem_type, data_info) 函数, 根据问题类型
和数据集信息, 返回推荐的机器学习项目流程。

参数:
- problem_type: str, 取值为 "分类" / "回归" / "聚类"
- data_info: dict, 包含:
    - n_samples: int, 样本量
    - n_features: int, 特征数
    - has_label: bool, 是否有标签

返回值: dict, 包含以下键:
- "steps": list of str, 推荐步骤列表
    - 分类/回归: ["数据清洗","特征工程","划分数据集",
      "模型训练","模型评估"]
    - 聚类: ["数据清洗","特征工程","聚类分析","结果解释"]
- "eval_metric": list of str, 推荐评估指标
    - 分类: ["准确率","F1分数","召回率"]
    - 回归: ["均方误差","R2分数","平均绝对误差"]
    - 聚类: ["轮廓系数","Calinski-Harabasz指数"]
- "warning": str, 数据问题警告(多个警告用分号拼接):
    - n_samples < 100 → "样本量过少,模型可能欠拟合"
    - n_features > n_samples → "特征数大于样本量,需降维"
    - 分类或回归 且 has_label == False → "缺少标签列,无法进行监督学习"
    - 无警告时返回空字符串 ""

示例:
    >>> plan = ml_project_plan("分类",
    ...     {"n_samples":1000,"n_features":10,"has_label":True})
    >>> "准确率" in plan["eval_metric"]
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 分类任务, 正常数据 1000 样本 10 特征 有标签
    # eval_metric 包含 "准确率"
    # steps 包含 5 个元素
    plan = ml_project_plan("分类",
        {"n_samples": 1000, "n_features": 10, "has_label": True})
    assert "准确率" in plan["eval_metric"], \
        "分类任务 eval_metric 应包含准确率"
    assert len(plan["steps"]) == 5, \
        f"分类任务 steps 应为 5 步, 实际 {len(plan['steps'])}"
    assert plan["warning"] == "", \
        f"无警告时应返回空串, 实际 {plan['warning']}"
    print("测试 1 通过: 分类任务正常数据")

    # 测试 2: 回归任务, 异常数据 50 样本 200 特征 无标签
    # warning 应同时包含: "样本量过少", "特征数大于样本量",
    #   "缺少标签列"
    # eval_metric 包含 "均方误差"
    plan2 = ml_project_plan("回归",
        {"n_samples": 50, "n_features": 200, "has_label": False})
    assert "均方误差" in plan2["eval_metric"], \
        "回归任务 eval_metric 应包含均方误差"
    assert "样本量过少" in plan2["warning"], \
        "n_samples<100 时应警告样本量过少"
    assert "特征数大于样本量" in plan2["warning"], \
        "n_features>n_samples 时应警告需降维"
    assert "缺少标签列" in plan2["warning"], \
        "回归任务无标签时应警告缺少标签列"
    print("测试 2 通过: 回归任务异常数据三项警告")

    # 测试 3: 聚类任务, 500 样本 8 特征 无标签
    # eval_metric 包含 "轮廓系数"
    plan3 = ml_project_plan("聚类",
        {"n_samples": 500, "n_features": 8, "has_label": False})
    assert "轮廓系数" in plan3["eval_metric"], \
        "聚类任务 eval_metric 应包含轮廓系数"
    assert len(plan3["steps"]) == 4, \
        f"聚类任务 steps 应为 4 步, 实际 {len(plan3['steps'])}"
    print("测试 3 通过: 聚类任务")

    print("所有测试通过!")
    pass
