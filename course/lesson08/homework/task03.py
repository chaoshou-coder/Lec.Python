"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合类设计(Temperature 温度转换)]
[预计完成时间: 30 分钟]

题目描述:
    设计 Temperature 类,用 @property 保护摄氏温度(绝对零度
    -273.15 以上),提供 fahrenheit 属性返回华氏温度,
    提供 __str__ 友好输出。体会"把现实概念封装成类"。

示例:
    >>> t = Temperature(25)
    >>> print(t.fahrenheit)
    77.0
    >>> print(t)
    Temperature(25.0°C = 77.0°F)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Temperature:
    # 绝对零度常量
    ABS_ZERO = -273.15

    def __init__(self, celsius):
        self.celsius = celsius  # 走 setter 校验

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < self.ABS_ZERO:
            raise ValueError(
                f"温度不能低于绝对零度 {self.ABS_ZERO}°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    def __str__(self):
        return (f"Temperature({self._celsius:.1f}°C "
                f"= {self.fahrenheit:.1f}°F)")

t = Temperature(25)
print(t)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常转换
    t1 = Temperature(25)
    print(f"测试1: {t1.fahrenheit:.1f}")  # 77.0

    # 测试 2: 冰点
    t2 = Temperature(0)
    print(f"测试2: {t2.fahrenheit:.1f}")  # 32.0

    # 测试 3: 沸点
    t3 = Temperature(100)
    print(f"测试3: {t3.fahrenheit:.1f}")  # 212.0

    # 测试 4: 低于绝对零度抛异常
    try:
        Temperature(-300)
        print("测试4: 未抛异常(错)")
    except ValueError as e:
        print(f"测试4: {e}")

    # 测试 5: 修改摄氏温度后华氏自动更新
    t1.celsius = 30
    print(f"测试5: {t1.fahrenheit:.1f}")  # 86.0

    # 测试 6: __str__ 输出
    print(f"测试6: {t1}")
