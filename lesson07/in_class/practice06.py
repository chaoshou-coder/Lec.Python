"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: Day01-Day06 大综合]
[预计完成时间: 30 分钟]

题目描述:
  综合之前所有练习,实现一个"完整购物系统"。

系统内置商品库(至少 5 种商品):
    编号 1: 苹果    - 5.50 元/个
    编号 2: 牛奶   - 12.80 元/盒
    编号 3: 面包    - 7.00 元/个
    编号 4: 鸡蛋    - 1.00 元/个
    编号 5: 巧克力 - 15.50 元/块

功能菜单:
    1. 浏览商品
    2. 添加商品到购物车
    3. 查看购物车
    4. 删除购物车商品
    5. 结算(会员 95 折)
    6. 查看购物历史
    0. 退出

要求:
    - 购物车用嵌套列表 [商品名, 单价, 数量]
    - 重复添加同名商品时,数量累加
    - 购物历史用列表记录每笔订单(订单号、时间、金额)
    - 结算后购物车清空,订单加入历史
    - 会员判断用 y/n 输入

示例:
    >>> 请输入命令: 1
    商品列表:
    1. 苹果    5.50 元
    2. 牛奶   12.80 元
    ...

    >>> 请输入命令: 2
    请输入商品编号: 1
    请输入数量: 3
    已添加 苹果 x3
"""

# ======================
# 学员代码区
# ======================

import datetime

# 内置商品库: [编号, 名称, 单价]
products = [
    [1, "苹果", 5.50],
    [2, "牛奶", 12.80],
    [3, "面包", 7.00],
    [4, "鸡蛋", 1.00],
    [5, "巧克力", 15.50],
]

# 购物车: 每个元素 [商品名, 单价, 数量]
cart = []

# 购物历史: 每个元素 [订单号, 时间, 金额]
history = []

# 订单计数器
order_count = 0

while True:
    # 显示菜单
    print("\n=== 购物系统 ===")
    print("1. 浏览商品")
    print("2. 添加商品到购物车")
    print("3. 查看购物车")
    print("4. 删除购物车商品")
    print("5. 结算")
    print("6. 查看购物历史")
    print("0. 退出")
    cmd = input("请输入命令: ")

    if cmd == "1":
        # 浏览商品
        print("商品列表:")
        for p in products:
            print(f"{p[0]}. {p[1]}  {p[2]:.2f} 元")

    elif cmd == "2":
        # 添加到购物车
        pid = int(input("请输入商品编号: "))
        qty = int(input("请输入数量: "))
        # 查找商品
        found_product = None
        for p in products:
            if p[0] == pid:
                found_product = p
                break
        if found_product is None:
            print("商品编号不存在!")
        else:
            # 查找购物车中是否已有
            found_cart = False
            for item in cart:
                if item[0] == found_product[1]:
                    item[1] += qty
                    found_cart = True
                    break
            if not found_cart:
                cart.append([found_product[1], found_product[2], qty])
            print(f"已添加 {found_product[1]} x{qty}")

    elif cmd == "3":
        # 查看购物车
        if len(cart) == 0:
            print("购物车为空!")
        else:
            total = 0
            print("购物车:")
            for i in range(len(cart)):
                item = cart[i]
                sub = item[1] * item[2]
                total += sub
                print(f"{i + 1}. {item[0]} 单价:{item[1]:.2f}"
                      f" 数量:{item[2]} 小计:{sub:.2f}")
            print(f"合计: {total:.2f}")

    elif cmd == "4":
        # 删除购物车商品
        if len(cart) == 0:
            print("购物车为空!")
        else:
            num = int(input("请输入要删除的编号: "))
            if 1 <= num <= len(cart):
                removed = cart.pop(num - 1)
                print(f"已删除: {removed[0]}")
            else:
                print("该编号不存在!")

    elif cmd == "5":
        # 结算
        if len(cart) == 0:
            print("购物车为空,无法结算!")
        else:
            total = 0
            print("======== 结算清单 ========")
            for i in range(len(cart)):
                item = cart[i]
                sub = item[1] * item[2]
                total += sub
                print(f"{i + 1}. {item[0]} {item[1]:.2f} x"
                      f" {item[2]} = {sub:.2f}")
            # 会员折扣
            is_member = input("是否是会员(y/n)? ")
            if is_member == "y":
                discount = total * 0.05
                final = total * 0.95
            else:
                discount = 0
                final = total
            print(f"原价合计: {total:.2f}")
            if is_member == "y":
                print(f"会员折扣: -{discount:.2f}")
            print(f"实付金额: {final:.2f}")
            # 记录历史
            order_count += 1
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append([order_count, now, final])
            # 清空购物车
            cart = []
            print(f"订单 #{order_count} 已生成!")

    elif cmd == "6":
        # 查看购物历史
        if len(history) == 0:
            print("暂无购物历史!")
        else:
            print("购物历史:")
            for h in history:
                print(f"  订单#{h[0]}  {h[1]}  金额: {h[2]:.2f}")

    elif cmd == "0":
        print("欢迎下次光临!")
        break

    else:
        print("无效命令,请重新输入")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 完整流程
    # 1 -> 2 -> 1 -> 3 -> 2 -> 2 -> 2 -> 3 -> 5 -> y -> 6 -> 0
    # 预期: 浏览商品,添加两件,查看,结算,查看历史

    # 测试 2: 重复添加累加数量
    # 2 -> 1 -> 3 -> 2 -> 1 -> 2 -> 3 -> 5 -> n -> 0
    # 预期: 苹果数量累加为 5,非会员原价结算

    # 测试 3: 空购物车结算
    # 5 -> 0
    # 预期: 提示"购物车为空,无法结算!"

    # 测试 4: 删除不正常编号
    # 2 -> 1 -> 3 -> 4 -> 9 -> 0
    # 预期: 提示"该编号不存在!"

    print("请直接运行本文件进行测试(需要交互输入)")
