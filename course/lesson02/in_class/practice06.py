"""
[难度: ⭐⭐]
[所属知识点: f-string 格式化输出]
[预计完成时间: 10 分钟]

题目描述:
  已知一本书的信息如下:
    书名 = "Python 入门"
    价格 = 59.8
    数量 = 3
  请使用 f-string 计算总价,并按以下格式输出:
    "购买 <数量> 本《<书名》,总价 <总价> 元"
  其中总价保留 2 位小数。

示例:
    >>> 运行程序
    购买 3 本《Python 入门》,总价 179.40 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本计算
    book = "Python 入门"
    price = 59.8
    qty = 3
    total = price * qty
    result = f"购买 {qty} 本《{book}》,总价 {total:.2f} 元"
    print(result)
    assert result == "购买 3 本《Python 入门》,总价 179.40 元"

    # 测试 2: 数量为 1
    book = "算法导论"
    price = 128.0
    qty = 1
    total = price * qty
    result = f"购买 {qty} 本《{book}》,总价 {total:.2f} 元"
    print(result)
    assert result == "购买 1 本《算法导论》,总价 128.00 元"

    # 测试 3: 价格为整数
    book = "数据结构"
    price = 45
    qty = 2
    total = price * qty
    result = f"购买 {qty} 本《{book}》,总价 {total:.2f} 元"
    print(result)
    assert result == "购买 2 本《数据结构》,总价 90.00 元"

    print("所有测试通过!")
