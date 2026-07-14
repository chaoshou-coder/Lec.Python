"""
[难度: ⭐⭐⭐⭐]
[所属知识点: @property 校验成绩 0-100 + 平均分方法]
[预计完成时间: 25 分钟]

题目描述:
    设计 Student 类,用 @property 保护成绩列表(每科 0-100),
    提供 average() 方法返回平均分。体会"数据校验 + 行为封装"。

示例:
    >>> s = Student("小红", [90, 85, 95])
    >>> print(s.average())
    90.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # 走 setter 校验

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, value):
        for s in value:
            if s < 0 or s > 100:
                raise ValueError("成绩必须在 0-100 之间")
        self._scores = list(value)

    def average(self):
        if not self._scores:
            return 0
        return sum(self._scores) / len(self._scores)

    def __str__(self):
        return (f"Student(姓名={self.name}, "
                f"成绩={self._scores}, "
                f"平均={self.average():.1f})")

s = Student("小红", [90, 85, 95])
print(s)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常平均分
    s1 = Student("小红", [90, 85, 95])
    print(f"测试1: {s1.average()}")  # 90.0

    # 测试 2: 空成绩返回 0
    s2 = Student("小明", [])
    print(f"测试2: {s2.average()}")  # 0

    # 测试 3: 超范围成绩抛异常
    try:
        Student("小刚", [90, 101])
        print("测试3: 未抛异常(错)")
    except ValueError as e:
        print(f"测试3: {e}")  # 成绩必须在 0-100 之间

    # 测试 4: 负数成绩抛异常
    try:
        Student("小李", [-5, 80])
        print("测试4: 未抛异常(错)")
    except ValueError as e:
        print(f"测试4: {e}")  # 成绩必须在 0-100 之间

    # 测试 5: 修改成绩后重算
    s1.scores = [100, 100, 100]
    print(f"测试5: {s1.average()}")  # 100.0

    # 测试 6: __str__ 输出
    print(f"测试6: {s1}")
