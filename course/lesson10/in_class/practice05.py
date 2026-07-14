"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 删除 + 修改数量]
[预计完成时间: 25 分钟]

题目描述:
    实现两个购物车操作函数:

    1. remove_from_cart(cart, product_id)
       - 按编号删除商品
       - 不存在时打印提示

    2. update_qty(cart, product_id, new_qty)
       - 修改指定商品的数量
       - new_qty 为 0 时自动删除该商品
       - 不存在时打印提示

示例:
    >>> cart = [{"id": 1, "name": "苹果", "price": 5.0, "qty": 2}]
    >>> remove_from_cart(cart, 1)
    >>> print(cart)
    []
    >>> update_qty(cart, 1, 5)
    商品 1 不存在
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def remove_from_cart(cart, product_id):
    """按编号删除商品"""
    # 提示: 遍历 cart,找到匹配项后 del 或 remove
    pass

def update_qty(cart, product_id, new_qty):
    """修改商品数量,为 0 时删除"""
    # 提示: 遍历找到商品
    #       if new_qty <= 0: 删除
    #       else: 更新 qty
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    cart = [
        {"id": 1, "name": "苹果", "price": 5.0, "qty": 2},
        {"id": 2, "name": "香蕉", "price": 3.5, "qty": 3},
    ]
    # 测试 1: 删除商品
    remove_from_cart(cart, 1)
    print(f"删除后: {cart}")
    # 测试 2: 修改数量
    update_qty(cart, 2, 5)
    print(f"修改后: {cart}")
    # 测试 3: 数量为 0 自动删除
    update_qty(cart, 2, 0)
    print(f"清零后: {cart}")
    # 测试 4: 不存在的商品
    remove_from_cart(cart, 99)
