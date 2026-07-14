"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Temperature 类(@property + 绝对零度校验 + 单位转换)]
[预计完成时间: 20 分钟,选做]

题目描述:
    定义一个 `Temperature` 类,用摄氏度为内部存储,
    同时提供华氏度的 property 访问。

    - 构造函数接收摄氏度 `celsius`
    - `celsius` 用 `@property` 保护,**禁止低于 -273.15**(绝对零度)
      非法赋值时打印 "低于绝对零度,已拒绝"
    - 提供 `fahrenheit` property(只读):
      - getter:返回华氏度 = celsius * 9 / 5 + 32
      - setter:接收华氏度,自动转换并校验

示例:
    >>> t = Temperature(25)
    >>> print(t.celsius)
    25
    >>> print(t.fahrenheit)
    77.0
    >>> t.fahrenheit = 32  # 设华氏 32°F = 摄氏 0°C
    >>> print(t.celsius)
    0.0
    >>> t.celsius = -300
    低于绝对零度,已拒绝
    >>> print(t.celsius)
    0.0  (没变)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # 走 setter 校验

    # 请补全 @celsius.setter / @fahrenheit (getter + setter)
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常创建
    t = Temperature(25)
    assert t.celsius == 25

    # 测试 2: 华氏 getter
    assert t.fahrenheit == 77.0

    # 测试 3: 华氏 setter 自动转摄氏
    t.fahrenheit = 32  # 32°F = 0°C
    assert t.celsius == 0.0

    # 测试 4: 拒绝绝对零度
    t.celsius = -300
    assert t.celsius == 0.0, "低于绝对零度应被拒绝"

    # 测试 5: 边界:恰好绝对零度
    t.celsius = -273.15
    assert t.celsius == -273.15
    print("✅ 所有测试通过")
