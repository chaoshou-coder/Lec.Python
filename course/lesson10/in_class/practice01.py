"""
[难度: ⭐⭐]
[所属知识点: 数据结构设计(商品库/购物车)]
[预计完成时间: 15 分钟]

题目描述:
    设计购物车项目的底层数据结构。

    1. 商品库: 用字典存储商品信息
       - 键: 商品编号(int)
       - 值: 字典 {"name": 名称, "price": 单价}

    2. 购物车: 用列表存储选购记录
       - 每项: {"id": 编号, "name": 名称,
               "price": 单价, "qty": 数量}

    请根据示例完成数据结构初始化。

示例:
    >>> print(products[1]['name'])
    苹果
    >>> print(len(cart))
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 商品库: 编号 → 商品信息字典
products = {
    1: {"name": "苹果", "price": 5.0},
    2: {"name": "香蕉", "price": 3.5},
    3: {"name": "橙子", "price": 4.0},
    4: {"name": "葡萄", "price": 8.0},
    5: {"name": "西瓜", "price": 12.0},
}

# 购物车: 已选商品列表
# 每项包含 id, name, price, qty
cart = [
    {"id": 1, "name": "苹果", "price": 5.0, "qty": 2},
    {"id": 3, "name": "橙子", "price": 4.0, "qty": 3},
]

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 商品库查询
    for pid, info in products.items():
        print(f"{pid}: {info['name']} ¥{info['price']}")
    # 测试 2: 购物车遍历
    print(f"购物车共 {len(cart)} 种商品")
    for item in cart:
        print(f"  {item['name']} x{item['qty']}")
