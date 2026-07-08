"""
[难度: ⭐⭐]
[所属知识点: Tool 装饰器定义工具]
[预计完成时间: 10 分钟]

场景: 使用 @tool 装饰器定义 get_weather(city: str) -> str,
模拟返回 "{city} 今天晴 25°C"。
调用 get_weather("北京") 验证。

示例:
    >>> from langchain_core.tools import tool
    >>> @tool
    ... def get_weather(city: str) -> str:
    ...     '''返回指定城市的天气'''
    ...     return f"{city} 今天晴 25°C"
    >>> get_weather.invoke("北京")
    '北京 今天晴 25°C'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """返回指定城市的天气信息"""
    return f"{city} 今天晴 25°C"


result = get_weather.invoke("北京")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 北京
    assert result == "北京 今天晴 25°C"
    print("测试 1 通过:", result)
    # 测试 2: 上海
    r2 = get_weather.invoke("上海")
    assert r2 == "上海 今天晴 25°C"
    print("测试 2 通过:", r2)
    # 测试 3: 查看工具名称
    assert get_weather.name == "get_weather"
    print("测试 3 通过: 工具名为", get_weather.name)
