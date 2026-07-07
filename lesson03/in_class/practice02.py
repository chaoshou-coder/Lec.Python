"""
[难度: ⭐⭐]
[所属知识点: 字符串长度与数字判断]
[预计完成时间: 10 分钟]

题目描述:
  输入一个手机号,判断其是否合法。
  合法条件:长度必须是 11 位,且每一位都是数字。
  要求使用 len() 判断长度,使用 isdigit() 判断是否全为数字。

示例:
    >>> "13800138000" → True
    >>> "1380013800" → False
    >>> "1380013800a" → False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
phone = "13800138000"
is_valid = len(phone) == 11 and phone.isdigit()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 合法手机号
    phone_1 = "13800138000"
    result_1 = len(phone_1) == 11 and phone_1.isdigit()
    print(result_1)
    assert result_1 is True

    # 测试 2: 长度不足
    phone_2 = "1380013800"
    result_2 = len(phone_2) == 11 and phone_2.isdigit()
    print(result_2)
    assert result_2 is False

    # 测试 3: 包含非数字字符
    phone_3 = "1380013800a"
    result_3 = len(phone_3) == 11 and phone_3.isdigit()
    print(result_3)
    assert result_3 is False

    # 测试 4: 长度超过 11 位
    phone_4 = "138001380001"
    result_4 = len(phone_4) == 11 and phone_4.isdigit()
    print(result_4)
    assert result_4 is False

    print("所有测试通过!")
