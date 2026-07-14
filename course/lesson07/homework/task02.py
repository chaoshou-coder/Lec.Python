"""
[难度: ⭐⭐⭐⭐]
[所属知识点: CSV 解析 — 不用 csv 模块,用 split]
[预计完成时间: 20 分钟]

题目描述:
  你收到一个 CSV 格式的文本文件 "grades.csv",每行是
  "姓名,语文,数学,英语"。请用 split(',') 解析每一行,
  计算每个人的总分,按总分从高到低排序,把结果写入
  "ranking.txt",每行格式: "排名 姓名 总分"。

要求:
  - 不用 csv 模块,只用 split(',')
  - 分数转 int 时可能失败,用 try/except ValueError 处理
  - 总分相同则按姓名排序
  - 结果写入 ranking.txt,每行 "1. 小明 285"

示例:
    >>> grades.csv 内容:
    小明,90,95,100
    小红,85,88,92
    小刚,70,65,80

    >>> ranking.txt 内容:
    1. 小明 285
    2. 小红 265
    3. 小刚 215
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import os
    src = "test_grades.csv"
    dst = "test_ranking.txt"

    # 创建测试 CSV
    with open(src, "w", encoding="utf-8") as f:
        f.write("小明,90,95,100\n")
        f.write("小红,85,88,92\n")
        f.write("小刚,70,65,80\n")

    # 模拟学员逻辑:读 CSV → 计算 → 排序 → 写 ranking
    rows = []
    with open(src, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            name = parts[0]
            try:
                scores = [int(x) for x in parts[1:]]
            except ValueError:
                continue  # 跳过无效行
            total = sum(scores)
            rows.append((name, total))
    # 按总分降序,总分相同按姓名升序
    rows.sort(key=lambda x: (-x[1], x[0]))
    with open(dst, "w", encoding="utf-8") as f:
        for i, (name, total) in enumerate(rows, 1):
            f.write(f"{i}. {name} {total}\n")

    # 验证
    with open(dst, "r", encoding="utf-8") as f:
        result = f.read().strip().split("\n")
    assert result[0] == "1. 小明 285"
    assert result[1] == "2. 小红 265"
    assert result[2] == "3. 小刚 215"

    # 测试:含无效行
    with open(src, "w", encoding="utf-8") as f:
        f.write("小明,90,95,100\n")
        f.write("坏数据,abc,def\n")  # 无效
        f.write("小红,85,88,92\n")
    # 重新跑逻辑(同上)
    rows = []
    with open(src, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            name = parts[0]
            try:
                scores = [int(x) for x in parts[1:]]
            except ValueError:
                continue
            total = sum(scores)
            rows.append((name, total))
    rows.sort(key=lambda x: (-x[1], x[0]))
    assert len(rows) == 2, "应跳过无效行,只剩 2 条"

    os.remove(src)
    os.remove(dst)
    print("task02 测试通过 ✓")
