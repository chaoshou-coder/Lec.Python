"""
[难度: ⭐⭐⭐⭐]
[所属知识点: DPO 数据构建 / HF Dataset]
[预计完成时间: 20 分钟]

写 DPODataBuilder 类，含三个方法：
- add_prompt(p): 添加 prompt
- add_pair(chosen, rejected): 添加成对回答
- build(): 构建 HF datasets.Dataset 并打印前 5 条

教学点：DPO 把 RM + PPO 简化成"三行数据"：
prompt + chosen + rejected，直接优化偏好。

示例:
    >>> builder = DPODataBuilder()
    >>> builder.add_prompt("什么是 DPO?")
    >>> builder.add_pair("DPO 是...", "DPO 就是...")
    >>> ds = builder.build()
    >>> ds[0]
    {'prompt': '什么是 DPO?', 'chosen': 'DPO 是...', 'rejected': ...}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 构建 6 条后 shape
    # builder = DPODataBuilder()
    # for i in range(6):
    #     builder.add_prompt(f"问题 {i}")
    #     builder.add_pair(f"好回答 {i}", f"差回答 {i}")
    # ds = builder.build()
    # assert len(ds) == 6
    # print("测试 1 通过: 6 条数据")

    # 测试 2: 字段完整
    # assert set(ds.column_names) == {'prompt', 'chosen', 'rejected'}
    # print("测试 2 通过: 字段 =", ds.column_names)
    pass
