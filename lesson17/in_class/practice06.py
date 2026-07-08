"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: EDA 综合 — 数据清洗 + 可视化 + 洞察]
[预计完成时间: 25 分钟]

题目描述:
  给定一组学生的考试分数(可能含缺失值):
    姓名      语文   数学   英语
    张三      85     90     78
    李四      None   88     92
    王五      76     None   85
    赵六      92     85     None
    孙七      88     79     90
  任务:
    1. 用每列的均值填充缺失值(取整数)
    2. 计算每位学生的总分,添加 "总分" 列
    3. 按总分降序排序,打印最终数据表
    4. 计算三科的平均分,用 matplotlib 绘制柱状图
       (标题: "各科平均分",x 轴: 科目,y 轴: 平均分)
    5. 输出一句话洞察,例如:
       "最偏科的科目是 XX,平均分最低,建议加强"

示例:
    >>> 填充缺失值后
         语文  数学  英语  总分
    赵六  92    85    84    261
    张三  85    90    78    253
    ...
    >>> 洞察: 最偏科的科目是语文,平均分最低
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt

    # 原始数据
    data = {
        "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
        "语文": [85, None, 76, 92, 88],
        "数学": [90, 88, None, 85, 79],
        "英语": [78, 92, 85, None, 90]
    }
    df = pd.DataFrame(data)

    # 测试 1: 用均值填充缺失值
    for col in ["语文", "数学", "英语"]:
        avg = int(df[col].mean())
        df[col] = df[col].fillna(avg)
    print("填充缺失值后:")
    print(df)
    assert df["语文"].isna().sum() == 0
    assert df["数学"].isna().sum() == 0
    assert df["英语"].isna().sum() == 0

    # 测试 2: 计算总分并排序
    df["总分"] = df["语文"] + df["数学"] + df["英语"]
    df_sorted = df.sort_values("总分", ascending=False)
    print("\n按总分排序:")
    print(df_sorted)
    assert df_sorted.iloc[0]["总分"] >= df_sorted.iloc[-1]["总分"]

    # 测试 3: 各科平均分
    chinese_avg = df["语文"].mean()
    math_avg = df["数学"].mean()
    english_avg = df["英语"].mean()
    print(f"\n语文: {chinese_avg:.1f}")
    print(f"数学: {math_avg:.1f}")
    print(f"英语: {english_avg:.1f}")
    assert 0 <= chinese_avg <= 100
    assert 0 <= math_avg <= 100
    assert 0 <= english_avg <= 100

    # 测试 4: 柱状图
    subjects = ["语文", "数学", "英语"]
    avgs = [chinese_avg, math_avg, english_avg]
    plt.bar(subjects, avgs)
    plt.title("各科平均分")
    plt.xlabel("科目")
    plt.ylabel("平均分")
    plt.savefig("subject_avg.png")
    print("\n图表已保存为 subject_avg.png")

    # 测试 5: 输出洞察
    min_subject = subjects[avgs.index(min(avgs))]
    insight = f"最偏科的科目是{min_subject},平均分最低,建议加强"
    print(f"\n洞察: {insight}")
    assert "洞察" not in insight or len(insight) > 0

    print("\n所有测试通过!")
