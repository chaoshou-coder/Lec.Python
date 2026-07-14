"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 接口 — 多人协作契约]
[预计完成时间: 15 分钟]

题目描述:
    定义接口类 `Serializer(abc.ABC)`,
    包含两个抽象方法:
    - `serialize(obj)`:序列化对象
    - `deserialize(text)`:反序列化文本

    定义子类 `JsonSerializer`,简单模拟:
    - serialize:返回 "{"data": " + str(obj) + "}"
    - deserialize:简单返回原文

    定义函数 `save_and_load(serializer, data)`:
    - 先 serializer.serialize(data)
    - 再 serializer.deserialize(序列化结果)

    新增一个 serializer 时,
    只需实现这两个抽象方法即可用。

    体会:abc = **团队契约**,
    架构师定义接口,开发者各自实现。

示例:
    >>> s = JsonSerializer()
    >>> save_and_load(s, "hello")
    deserialize: {data: hello}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Serializer(abc.ABC):
    # 请定义 serialize / deserialize 抽象方法
    pass

class JsonSerializer(Serializer):
    pass

# def save_and_load(serializer, data): ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    s = JsonSerializer()
    serialized = s.serialize("hello")
    assert "hello" in serialized
    deserialized = s.deserialize(serialized)
    assert isinstance(deserialized, str)

    # 新增 XML serializer 无需改 save_and_load
    class XmlSerializer(Serializer):
        def serialize(self, obj):
            return f"<data>{obj}</data>"

        def deserialize(self, text):
            return text

    xml = XmlSerializer()
    assert "<data>" in xml.serialize("test")
    print("✅ 所有测试通过")
