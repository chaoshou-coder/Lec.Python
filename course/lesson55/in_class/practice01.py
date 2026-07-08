"""
[难度: ⭐]
[所属知识点: LangChain 安装与 PromptTemplate]
[预计完成时间: 5 分钟]

场景: 使用 langchain_core.prompts.PromptTemplate
创建模板 "请用一句话解释:{topic}",
调用 format(topic="AI") 返回完整 prompt。

示例:
    >>> from langchain_core.prompts import PromptTemplate
    >>> prompt = PromptTemplate(
    ...     input_variables=["topic"],
    ...     template="请用一句话解释:{topic}"
    ... )
    >>> prompt.format(topic="AI")
    '请用一句话解释:AI'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="请用一句话解释:{topic}"
)
result = prompt.format(topic="AI")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 填入 "AI"
    assert result == "请用一句话解释:AI"
    print("测试 1 通过:", result)
    # 测试 2: 填入其他词
    r2 = prompt.format(topic="Python")
    assert r2 == "请用一句话解释:Python"
    print("测试 2 通过:", r2)
