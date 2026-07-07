"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 自定义异常]
[预计完成时间: 20 分钟]

题目描述:
定义一个自定义异常 `InvalidEmailError`,继承自 Exception。
编写一个函数 `validate_email(email)`,检查 email 是否包含 '@':
- 如果包含 '@',返回邮箱字符串
- 如果不包含 '@',抛出 InvalidEmailError("邮箱格式不合法")

示例:
    >>> validate_email("test@example.com") → 返回 "test@example.com"
    >>> validate_email("invalid.com") → 抛出 InvalidEmailError
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 合法邮箱
    # 测试 2: 不含 @ 的邮箱
    # 测试 3: 空字符串
    pass
