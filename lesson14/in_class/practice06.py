"""
[难度: ⭐⭐⭐]
[所属知识点: Pandas groupby 分组聚合]
[预计完成时间: 15 分钟]

题目描述:
  给定以下销售数据 DataFrame:
    部门    销售额
    东区    100
    东区    200
    西区    150
    西区    250
    南区    300
  请使用 groupby 按 "部门" 分组,
  计算每个部门的 "销售额" 总和,
  并将结果按降序打印。

示例:
    >>> 分组聚合后
    部门
    西区    400
    南区    300
    东区    300
"""

# =======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import pandas as pd

    # 测试 1: 分组求和
    data = {
        "部门": ["东区", "东区", "西区", "西区", "南区"],
        "销售额": [100, 200, 150, 250, 300]
    }
    df = pd.DataFrame(data)
    result = df.groupby("部门")["销售额"].sum()
    print(result)
    assert result["东区"] == 300
    assert result["西区"] == 400
    assert result["南区"] == 300

    # 测试 2: 降序排序
    sorted_result = result.sort_values(ascending=False)
    print(sorted_result)
    assert sorted_result.iloc[0] == 400

    # 测试 3: 计算均值
    mean_result = df.groupby("部门")["销售额"].mean()
    print(mean_result)
    assert mean_result["东区"] == 150.0

    print("所有测试通过!")
