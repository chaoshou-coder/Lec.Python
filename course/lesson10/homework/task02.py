"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 历史订单]
[预计完成时间: 30 分钟]

题目描述:
    为购物车项目添加历史订单功能。

    实现以下函数:
      1. save_order(cart, filename)
         - 将当前购物车作为订单保存到文件
         - 订单包含: 时间戳、商品列表、总金额
      2. view_orders(filename)
         - 读取并打印所有历史订单

    订单文件格式: 每行一个 JSON 对象(追加写入)

示例:
    >>> cart = [{"id": 1, "name": "苹果", "price": 5.0, "qty": 2}]
    >>> save_order(cart, "orders.jsonl")
    >>> view_orders("orders.jsonl")
    订单 1: 2026-07-14 10:30:00
      苹果 x2 = 10.00
      总计: 10.00
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 提示: 需要导入
# import json
# from datetime import datetime

def save_order(cart, filename):
    """保存订单到文件"""
    # 1. 计算总金额
    # 2. 构造订单字典(时间戳 + 商品 + 总计)
    # 3. 追加写入文件(jsonl 格式)
    pass

def view_orders(filename):
    """查看所有历史订单"""
    # 1. 逐行读取文件
    # 2. json.loads 解析每行
    # 3. 格式化打印
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    cart1 = [
        {"id": 1, "name": "苹果", "price": 5.0, "qty": 2},
    ]
    cart2 = [
        {"id": 2, "name": "香蕉", "price": 3.5, "qty": 4},
    ]
    # 测试 1: 保存两笔订单
    save_order(cart1, "orders_test.jsonl")
    save_order(cart2, "orders_test.jsonl")
    print("已保存 2 笔订单")
    # 测试 2: 查看订单
    view_orders("orders_test.jsonl")
