"""
[难度: ⭐⭐]
[所属知识点: append() 与 while 循环]
[预计完成时间: 15 分钟]

题目描述:
  创建一个空列表,让用户循环输入朋友名字,
  用户每输入一个名字,就添加到列表中。
  当用户输入 "quit" 时,停止输入,并打印全部朋友名单。

示例:
    >>> 张三
    >>> 李四
    >>> quit
    全部朋友: ['张三', '李四']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
friends = []
while True:
    name = input("请输入朋友名字(输入 quit 退出):")
    if name == "quit":
        break
    friends.append(name)
print(f"全部朋友: {friends}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 手动模拟追加过程
    friends_1 = []
    inputs_1 = ["张三", "李四", "王五", "quit"]
    for item in inputs_1:
        if item == "quit":
            break
        friends_1.append(item)
    print(f"全部朋友: {friends_1}")
    assert friends_1 == ["张三", "李四", "王五"]

    # 测试 2: 边界 - 第一个输入就是 quit
    friends_2 = []
    inputs_2 = ["quit"]
    for item in inputs_2:
        if item == "quit":
            break
        friends_2.append(item)
    print(f"全部朋友: {friends_2}")
    assert friends_2 == []

    # 测试 3: 单个名字后退出
    friends_3 = []
    inputs_3 = ["小明", "quit"]
    for item in inputs_3:
        if item == "quit":
            break
        friends_3.append(item)
    print(f"全部朋友: {friends_3}")
    assert friends_3 == ["小明"]

    print("所有测试通过!")
