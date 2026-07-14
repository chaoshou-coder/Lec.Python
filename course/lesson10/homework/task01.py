"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 文件持久化(JSON 加载/保存)]
[预计完成时间: 25 分钟]

题目描述:
    为购物车项目添加 JSON 文件持久化功能。

    实现两个函数:
      1. save_cart(cart, filename)
         - 将购物车数据保存为 JSON 文件
      2. load_cart(filename)
         - 从 JSON 文件读取购物车数据
         - 文件不存在时返回空列表

    使用 json 模块,注意中文编码 ensure_ascii=False。

示例:
    >>> cart = [{"id": 1, "name": "苹果", "price": 5.0, "qty": 2}]
    >>> save_cart(cart, "cart.json")
    >>> new_cart = load_cart("cart.json")
    >>> print(new_cart)
    [{'id': 1, 'name': '苹果', 'price': 5.0, 'qty': 2}]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 提示: 需要导入
# import json
# import os

def save_cart(cart, filename):
    """保存购物车到 JSON 文件"""
    # 提示: with open(filename, 'w', encoding='utf-8') as f:
    #           json.dump(cart, f, ensure_ascii=False, indent=2)
    pass

def load_cart(filename):
    """从 JSON 文件加载购物车"""
    # 提示: 先判断 os.path.exists(filename)
    #       存在则读取,不存在返回 []
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    cart = [
        {"id": 1, "name": "苹果", "price": 5.0, "qty": 2},
        {"id": 2, "name": "香蕉", "price": 3.5, "qty": 3},
    ]
    # 测试 1: 保存
    save_cart(cart, "cart_test.json")
    print("已保存到 cart_test.json")
    # 测试 2: 加载
    loaded = load_cart("cart_test.json")
    print(f"加载结果: {loaded}")
    # 测试 3: 文件不存在
    empty = load_cart("not_exist.json")
    print(f"不存在: {empty}")
