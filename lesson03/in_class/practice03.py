"""
[难度: ⭐⭐⭐]
[所属知识点: 字符串正反查找]
[预计完成时间: 15 分钟]

题目描述:
  输入一句名言和一个关键字,分别使用 find() 和 rfind()
  查找该关键字在名言中第一次出现和最后一次出现的位置。

示例:
    >>> 名言 "hello hello hello",关键 字 "hello"
    首次位置: 0,末次位置: 12
    >>> 名言 "千里之行始于足下",关键字 "之"
    首次位置: 2,末次位置: 6
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
quote = "hello hello hello"
keyword = "hello"
first_pos = quote.find(keyword)
last_pos = quote.rfind(keyword)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 关键字出现多次
    quote_1 = "hello hello hello"
    key_1 = "hello"
    first_1 = quote_1.find(key_1)
    last_1 = quote_1.rfind(key_1)
    print(f"首次位置: {first_1},末次位置: {last_1}")
    assert first_1 == 0
    assert last_1 == 12

    # 测试 2: 中文关键字
    quote_2 = "千里之行始于足下"
    key_2 = "之"
    first_2 = quote_2.find(key_2)
    last_2 = quote_2.rfind(key_2)
    print(f"首次位置: {first_2},末次位置: {last_2}")
    assert first_2 == 2
    assert last_2 == 6

    # 测试 3: 关键字只出现一次
    quote_3 = "学而时习之"
    key_3 = "习"
    first_3 = quote_3.find(key_3)
    last_3 = quote_3.rfind(key_3)
    print(f"首次位置: {first_3},末次位置: {last_3}")
    assert first_3 == last_3

    # 测试 4: 关键字不存在
    quote_4 = "hello world"
    key_4 = "python"
    first_4 = quote_4.find(key_4)
    last_4 = quote_4.rfind(key_4)
    print(f"首次位置: {first_4},末次位置: {last_4}")
    assert first_4 == -1
    assert last_4 == -1

    print("所有测试通过!")
