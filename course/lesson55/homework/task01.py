"""
[难度: ⭐⭐]
[所属知识点: Function Calling schema]
[预计完成时间: 10 分钟]

场景: 手工构建 OpenAI 格式的 function calling
tool schema dict, 含 name、description、parameters
(type/required/properties), 验证字段类型正确。

示例:
    >>> schema = {
    ...     "name": "get_weather",
    ...     "description": "获取城市天气",
    ...     "parameters": {
    ...         "type": "object",
    ...         "required": ["city"],
    ...         "properties": {
    ...             "city": {"type": "string"}
    ...         }
    ...     }
    ... }
    >>> schema["name"]
    'get_weather'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
get_weather_schema = {
    "name": "get_weather",
    "description": "获取指定城市的实时天气",
    "parameters": {
        "type": "object",
        "required": ["city"],
        "properties": {
            "city": {
                "type": "string",
                "description": "中文城市名"
            }
        }
    }
}

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: name 字段
    assert get_weather_schema["name"] == "get_weather"
    print("测试 1 通过: name =", get_weather_schema["name"])
    # 测试 2: parameters.type
    assert get_weather_schema["parameters"]["type"] == "object"
    print("测试 2 通过: type = object")
    # 测试 3: required 包含 city
    assert "city" in get_weather_schema["parameters"]["required"]
    print("测试 3 通过: city 为必填")
    # 测试 4: properties.city.type
    prop = get_weather_schema["parameters"]["properties"]["city"]
    assert prop["type"] == "string"
    print("测试 4 通过: city 类型 string")
