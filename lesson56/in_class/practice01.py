"""
[难度: ⭐]
[所属知识点: Streamlit 最小应用]
[预计完成时间: 5 分钟]

题目描述:
写一个最小 Streamlit app(保存为 py 文件),包含 st.title、
st.text_input、st.button、st.write 四个组件。
要求实现函数 build_minimal_app(),返回 app 源字符串。

示例:
    >>> src = build_minimal_app()
    >>> 'st.title' in src
    True
    >>> 'st.button' in src
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def build_minimal_app():
    """返回最小 Streamlit app 的源码字符串。"""
    src = (
        "import streamlit as st\n"
        "\n"
        "st.title('我的第一个应用')\n"
        "name = st.text_input('请输入姓名')\n"
        "if st.button('提交'):\n"
        "    st.write(f'你好, {name}')\n"
    )
    return src

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 返回值必须包含 st.title 与 st.write
    code = build_minimal_app()
    assert 'st.title' in code, '缺少 st.title'
    assert 'st.write' in code, '缺少 st.write'
    print('测试 1 通过: 包含 st.title 与 st.write')

    # 测试 2: 返回值必须包含 st.text_input 与 st.button
    assert 'st.text_input' in code, '缺少 st.text_input'
    assert 'st.button' in code, '缺少 st.button'
    print('测试 2 通过: 包含 st.text_input 与 st.button')
