"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 评测报告聚合与对比]
[预计完成时间: 20 分钟]

写一个 EvalReport 类,包含:
1. add_metric(name, score) 记录指标
2. compare_before_after(before_dict, after_dict)
   对比微调前后指标,打印 ↑/↓ 和差值
测试: 微调前 PPL=5.2/BLEU=0.30/ROUGE=0.35,
      微调后 PPL=3.1/BLEU=0.42/ROUGE=0.48。

示例:
    >>> report.compare_before_after(before, after)
    PPL     ↓ 2.10
    BLEU    ↑ 0.12
    ROUGE   ↑ 0.13
"""

# ======================
# 学员代码区
# ======================
class EvalReport:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, score):
        # 记录指标
        pass

    def compare_before_after(self, before, after):
        # 遍历 after 中每个指标,
        # 与 before 对比,打印 ↑ 或 ↓ 及差值
        # 注意: PPL 越低越好,其余越高越好
        pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    report = EvalReport()

    # 测试 1: 记录指标
    report.add_metric("PPL", 5.2)
    report.add_metric("BLEU", 0.30)
    print(f"记录指标: {report.metrics}")

    # 测试 2: 微调前后对比
    before = {"PPL": 5.2, "BLEU": 0.30, "ROUGE": 0.35}
    after  = {"PPL": 3.1, "BLEU": 0.42, "ROUGE": 0.48}
    report.compare_before_after(before, after)

    # 测试 3: 包含新增指标
    b2 = {"PPL": 10.0}
    a2 = {"PPL": 8.0, "BLEU": 0.25}
    report.compare_before_after(b2, a2)
