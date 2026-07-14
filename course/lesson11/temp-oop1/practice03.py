"""
[难度: ⭐⭐⭐]
[所属知识点: @property getter / setter 校验]
[预计完成时间: 12 分钟]

题目描述:
    定义一个 `Student` 类,表示学生。
    - 构造函数接收 `name` 和 `score`
    - `score` 用 `@property` 保护,合法范围为 0~100
    - setter 收到非法值时拒绝修改,并打印提示 "成绩必须在 0-100 之间"

示例:
    >>> s = Student("小明", 85)
    >>> print(s.score)
    85
    >>> s.score = 150
    成绩必须在 0-100 之间
    >>> print(s.score)
    85  (没变)
    >>> s.score = -5
    成绩必须在 0-100 之间
    >>> print(s.score)
    85  (没变)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Student:
    def __init__(self, name, score):
        self.name = name
        # 注意:赋值走 setter,用 self.score 而非 self._score
        self.score = score

    # 请补全 @property 和 @score.setter
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常赋值
    s = Student("小明", 85)
    assert s.score == 85

    # 测试 2: 超过 100 被拒绝
    original = s.score
    s.score = 150
    assert s.score == original, "超 100 应被拒绝"

    # 测试 3: 负数被拒绝
    s.score = -5
    assert s.score == original, "负数应被拒绝"

    # 测试 4: 边界:恰好 0 和 100 能通过
    s.score = 0
    assert s.score == 0
    s.score = 100
    assert s.score == 100
    print("✅ 所有测试通过")
