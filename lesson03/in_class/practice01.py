"""
[难度: ⭐⭐]
[所属知识点: 字符串查找与切片]
[预计完成时间: 10 分钟]

题目描述:
  输入一个邮箱地址,提取其域名部分(即 @ 后面的内容)。
  例如:输入 "zhangsan@163.com",应提取出 "163.com"。
  要求使用 find() 定位 @ 位置,再用切片提取。

示例:
    >>> "zhangsan@163.com" → "163.com"
    >>> "lisi@gmail.com" → "gmail.com"
    >>> "wangwu@qq.com" → "qq.com"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
email = "zhangsan@163.com"
at_index = email.find("@")
domain = email[at_index + 1:]

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 常规邮箱
    email_1 = "zhangsan@163.com"
    pos_1 = email_1.find("@")
    result_1 = email_1[pos_1 + 1:]
    print(result_1)
    assert result_1 == "163.com"

    # 测试 2: 其他域名邮箱
    email_2 = "lisi@gmail.com"
    pos_2 = email_2.find("@")
    result_2 = email_2[pos_2 + 1:]
    print(result_2)
    assert result_2 == "gmail.com"

    # 测试 3: 边界 - @ 在最后一位
    email_3 = "test@abc.cn"
    pos_3 = email_3.find("@")
    result_3 = email_3[pos_3 + 1:]
    print(result_3)
    assert result_3 == "abc.cn"

    print("所有测试通过!")
