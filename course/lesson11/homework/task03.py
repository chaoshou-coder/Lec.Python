"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: **kwargs + 字典]
[预计完成时间: 25 分钟]

题目描述:
    定义一个函数 create_user(name, **info),返回一个用户字典,
    包含 name 和所有 info 键值对(合并为一个字典)。

示例:
    >>> create_user("张三", age=20, city="成都")
    {'name': '张三', 'age': 20, 'city': '成都'}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def create_user(name, **info):
    user = {"name": name}
    user.update(info)
    return user


# 示例调用
print(create_user("张三", age=20, city="成都"))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 多个属性
    print(f"测试1: {create_user('Alice', age=25, role='admin')}")

    # 测试 2: 只有 name
    print(f"测试2: {create_user('Bob')}")

    # 测试 3: 单个额外属性
    print(f"测试3: {create_user('Carol', level=5)}")
