"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 字符串title()]
[预计完成时间: 20 分钟]

题目描述:
    输入一个英文名字(如 "john smith"),用 title() 转成 "John Smith",
    并打印结果。

示例:
    >>> name = "john smith"
    输出: John Smith

"""

# ======================
# 学员代码区(以 pass 作为占位糖)
# ======================
name = input("请输入英文名字: ")
result = name.title()
print("格式化结果:", result)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 全小写
    print(f"测试1: {'john smith'.title()}")

    # 测试 2: 混合大小写
    print(f"测试2: {'jOhN sMiTH'.title()}")

    # 测试 3: 单个词
    print(f"测试3: {'hello'.title()}")

    # 测试 4: 空字符串
    print(f"测试4: {''.title()}")
