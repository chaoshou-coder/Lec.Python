"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Few-shot 示例 + 结构化输出(JSON Mode)]
[预计完成时间: 20 分钟]

Few-shot 是通过在 prompt 中塞入若干示例, 让模型"依葫芦画瓢"。
请实现 extract_info 函数, 要求:
1) system prompt 给出 1 个 few-shot 示例
2) 再通过 response_format={"type": "json_object"} 强制 JSON 输出
3) 把 JSON 字符串解析为 dict 并返回

示例:
    >>> extract_info("订单 A123 总价 99 元")
    {"order_id": "A123", "amount": 99}
"""

# ======================
# 学员代码区(以 pass 作为占位符)import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def extract_info(text: str) -> dict:
    """few-shot + JSON mode 抽取结构化信息"""
    system_prompt = (
        "你是信息抽取助手。给定一句中文订单描述,"
        "请返回 JSON, 字段: order_id, amount。\n"
        '示例输入: "订单 X999 总价 300 元"\n'
        '示例输出: {"order_id": "X999", "amount": 300}'
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        # TODO: 强制返回 JSON 对象
    )
    raw = resp.choices[0].message.content
    # TODO: json.loads 后返回
    return {}


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 抽取正常描述
    d = extract_info("订单 A123 总价 99 元")
    assert "order_id" in d and "amount" in d
    print(f"抽取结果: {d}")

    # 测试 2: 多零金额
    d2 = extract_info("订单 B1 总价 1500 元")
    assert d2.get("amount") == 1500
    print(f"大额抽取: {d2}")

    # 测试 3: 可被 JSON 二次序列化(证明返回是合法 dict)
    import json
    s = json.dumps(d2, ensure_ascii=False)
    print(f"序列化: {s}")
