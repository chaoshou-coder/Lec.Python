"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: Day06 分支 + Day05 循环 + 函数封装]
[预计完成时间: 30 分钟]

题目描述:
  把 Day07 综合题 06 的完整购物系统,用函数拆分成多个模块,
  让 main 函数只负责控制流程,具体逻辑分散到各个函数中。

要求实现的函数:
    - show_menu(): 显示菜单
    - browse_products(): 浏览商品
    - add_to_cart(): 添加商品到购物车
    - view_cart(): 查看购物车
    - remove_from_cart(): 删除购物车商品
    - checkout(): 结算(含会员折扣)
    - view_history(): 查看购物历史

规则:
    - 商品库、购物车、历史记录作为全局变量(或参数传递)
    - checkout 函数返回金额,同时记录历史
    - main 函数只写一个 while True 循环 + if/elif 分发命令

示例:
    调用方式与综合题 06 完全相同,但代码结构更清晰。
"""

# ======================
# 学员代码区
# ======================

import datetime

# 全局数据
products = [
    [1, "苹果", 5.50],
    [2, "牛奶", 12.80],
    [3, "面包", 7.00],
    [4, "鸡蛋", 1.00],
    [5, "巧克力", 15.50],
]
cart = []
history = []
order_count = 0


def show_menu():
    """显示菜单"""
    print("\n=== 购物系统 ===")
    print("1. 浏览商品")
    print("2. 添加商品到购物车")
    print("3. 查看购物车")
    print("4. 删除购物车商品")
    print("5. 结算")
    print("6. 查看购物历史")
    print("0. 退出")


def browse_products():
    """浏览商品"""
    print("商品列表:")
    for p in products:
        print(f"{p[0]}. {p[1]}  {p[2]:.2f} 元")


def add_to_cart():
    """添加商品到购物车"""
    pid = int(input("请输入商品编号: "))
    qty = int(input("请输入数量: "))
    found_product = None
    for p in products:
        if p[0] == pid:
            found_product = p
            break
    if found_product is None:
        print("商品编号不存在!")
        return
    found_cart = False
    for item in cart:
        if item[0] == found_product[1]:
            item[1] += qty
            found_cart = True
            break
    if not found_cart:
        cart.append([found_product[1], found_product[2], qty])
    print(f"已添加 {found_product[1]} x{qty}")


def view_cart():
    """查看购物车"""
    if len(cart) == 0:
        print("购物车为空!")
        return
    total = 0
    print("购物车:")
    for i in range(len(cart)):
        item = cart[i]
        sub = item[1] * item[2]
        total += sub
        print(f"{i + 1}. {item[0]} 单价:{item[1]:.2f}"
              f" 数量:{item[2]} 小计:{sub:.2f}")
    print(f"合计: {total:.2f}")


def remove_from_cart():
    """删除购物车商品"""
    if len(cart) == 0:
        print("购物车为空!")
        return
    num = int(input("请输入要删除的编号: "))
    if 1 <= num <= len(cart):
        removed = cart.pop(num - 1)
        print(f"已删除: {removed[0]}")
    else:
        print("该编号不存在!")


def checkout():
    """结算,返回最终金额"""
    global order_count
    if len(cart) == 0:
        print("购物车为空,无法结算!")
        return 0
    total = 0
    print("======== 结算清单 ========")
    for i in range(len(cart)):
        item = cart[i]
        sub = item[1] * item[2]
        total += sub
        print(f"{i + 1}. {item[0]} {item[1]:.2f} x"
              f" {item[2]} = {sub:.2f}")
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
    cart.clear()
    print(f"订单 #{order_count} 已生成!")
    return final


def view_history():
    """查看购物历史"""
    if len(history) == 0:
        print("暂无购物历史!")
        return
    print("购物历史:")
    for h in history:
        print(f"  订单#{h[0]}  {h[1]}  金额: {h[2]:.2f}")


def main():
    """主函数"""
    while True:
        show_menu()
        cmd = input("请输入命令: ")
        if cmd == "1":
            browse_products()
        elif cmd == "2":
            add_to_cart()
        elif cmd == "3":
            view_cart()
        elif cmd == "4":
            remove_from_cart()
        elif cmd == "5":
            checkout()
        elif cmd == "6":
            view_history()
        elif cmd == "0":
            print("欢迎下次光临!")
            break
        else:
            print("无效命令,请重新输入")


if __name__ == "__main__":
    main()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
# 测试 1: 完整流程
# 1 -> 2 -> 1 -> 3 -> 2 -> 2 -> 2 -> 3 -> 5 -> y -> 6 -> 0
# 预期: 浏览商品,添加两件,查看,结算,查看历史

# 测试 2: 重复添加累加数量
# 2 -> 1 -> 3 -> 2 -> 1 -> 2 -> 3 -> 5 -> n -> 0
# 预期: 苹果数量累加,原价结算

# 测试 3: 空购物车结算
# 5 -> 0
# 预期: 提示"购物车为空,无法结算!"

# 直接运行查看效果:
#   python task02.py
