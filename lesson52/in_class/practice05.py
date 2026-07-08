"""
[难度: ⭐⭐⭐]
[所属知识点: Chain-of-Thought 思维链提示]
[预计完成时间: 15 分钟]

CoT 的原理是让模型"一步步思考"再给出答案, 大幅提升推理类任务准确率。
请补全 make_cot_prompt 函数: 接收一道数学题, 拼接上经典 CoT 指令
"Let's think step by step", 再调用模型并返回推理文本。

示例:
    >>> prompt = make_cot_prompt("12 * 8 = ?")
    >>> # prompt 末尾应含 "Let's think step by step"
    >>> ans = cot_answer("12 * 8 = ?")
    >>> # ans 中会含逐步计算说明与最终答案 96
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

COT_SUFFIX = "Let's think step by step."


def make_cot_prompt(question: str) -> str:
    """把题目拼上 CoT 后缀"""
    # TODO: 返回 f"{question}\n{COT_SUFFIX}"
    return ""


def cot_answer(question: str) -> str:
    """调用模型并返回 CoT 推理结果"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user",
                   "content": make_cot_prompt(question)}],
    )
    # TODO: 返回模型生成的纯文本
    return ""


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 拼接是否包含 CoT 后缀
    p = make_cot_prompt("1+1=?")
    assert COT_SUFFIX in p
    print("CoT 后缀 OK")

    # 测试 2: 调用模型返回非空
    ans = cot_answer("15 * 4 = ?")
    assert isinstance(ans, str) and len(ans) > 0
    print(f"CoT 回答: {ans[:60]}...")

    # 测试 3: 复杂题也能返回长推理
    ans2 = cot_answer(
        "一个水池每小时注水 5 吨, 放掉 2 吨,"
        "10 小时后水池共多少吨水?"
    )
    assert len(ans2) > len(ans)
    print(f"复杂题长度: {len(ans2)}")
