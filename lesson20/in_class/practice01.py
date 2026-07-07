"""
[难度: ⭐⭐]
[所属知识点: 基类]
[预计完成时间: 10 分钟]

题目描述:
定义一个基类 Animal,包含 name 属性和 speak() 方法,
speak() 返回字符串 "..."。

示例:
    >>> a = Animal("某动物")
    >>> a.speak()
    '...'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 创建 Animal 实例并调用 speak
    a1 = Animal("某动物")
    print(a1.speak())

    # 测试 2: 名字为空字符串
    a2 = Animal("")
    print(a2.name)
    print(a2.speak())

    # 测试 3: 验证返回类型
    a3 = Animal("测试")
    result = a3.speak()
    print(f"返回类型: {type(result)}")
