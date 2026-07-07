"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 列表增删与循环菜单]
[预计完成时间: 20 分钟]

题目描述:
  实现一个简易购物车程序,功能菜单如下:
    1. 添加商品
    2. 删除商品
    0. 退出
  每次操作后打印当前购物车内容。
     - 添加: 输入商品名,使用 append() 加入列表;
     - 删除: 输入商品名,使用 remove() 移除;
     - 退出: 结束程序,打印最终购物车。

示例:
    >>> 1 → "苹果"
    >>> 1 → "香蕉"
    >>> 2 → "苹果"
    >>> 0
    输出: 当前购物车: ['香蕉']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
cart = []
while True:
    print("\n1.添加商品 2.删除商品 0.退出")
    choice = input("请选择操作:")
    if choice == "1":
        item = input("请输入要添加的商品:")
        cart.append(item)
        print(f"当前购物车: {cart}")
    elif choice == "2":
        item = input("请输入要删除的商品:")
        cart.remove(item)
        print(f"当前购物车: {cart}")
    elif choice == "0":
        print(f"最终购物车: {cart}")
        break
    else:
        print("输入无效,请重新选择")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 添加两个商品
    cart_1 = []
    actions_1 = [("1", "苹果"), ("1", "香蕉")]
    for act, val in actions_1:
        if act == "1":
            cart_1.append(val)
    print(f"当前购物车: {cart_1}")
    assert cart_1 == ["苹果", "香蕉"]

    # 测试 2: 添加后删除
    cart_2 = ["苹果", "香蕉", "橘子"]
    cart_2.remove("香蕉")
    print(f"当前购物车: {cart_2}")
    assert cart_2 == ["苹果", "橘子"]

    # 测试 3: 空购物车删除后状态
    cart_3 = []
    cart_3.append("西瓜")
    cart_3.remove("西瓜")
    print(f"当前购物车: {cart_3}")
    assert cart_3 == []

    print("所有测试通过!")
