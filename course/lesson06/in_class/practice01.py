"""
[难度: ⭐⭐]
[所属知识点: 单继承语法 class Child(Parent)]
[预计完成时间: 10 分钟]

题目描述:
    定义父类 `Vehicle`,表示交通工具。
    - 构造函数接收 `brand`(品牌)
    - 方法 `start()` 输出 "XXX 启动"
    定义子类 `Car`,继承 Vehicle。
    - 新增方法 `honk()` 输出 "XXX 按喇叭"

    创建一辆车,依次调用 start() 和 honk()。

示例:
    >>> car = Car("比亚迪")
    >>> car.start()
    比亚迪 启动
    >>> car.honk()
    比亚迪 按喇叭
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Vehicle:
    pass

# car = Car("比亚迪")
# car.start()
# car.honk()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    car = Car("比亚迪")
    assert car.brand == "比亚迪"
    # start 继承自 Vehicle
    # honk 是 Car 自己的
    print("✅ 所有测试通过")
