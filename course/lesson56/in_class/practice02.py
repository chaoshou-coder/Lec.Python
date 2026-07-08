"""
[难度: ⭐⭐]
[所属知识点: st.chat_message 聊天界面]
[预计完成时间: 10 分钟]

题目描述:
用 st.chat_message + st.chat_input 写聊天 UI,
用 session_state 保存历史,chat_message 渲染 assistant 回复。
实现函数 build_chat_app(),返回 app 源字符串。
验证历史列表长度与渲染数量。

示例:
    >>> src = build_chat_app()
    >>> 'st.chat_message' in src
    True
    >>> 'session_state' in src
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def build_chat_app():
    """返回聊天界面 Streamlit app 的源码字符串。"""
    src = (
        "import streamlit as st\n"
        "\n"
        "if 'history' not in st.session_state:\n"
        "    st.session_state.history = []\n"
        "\n"
        "prompt = st.chat_input('说点什么...')\n"
        "if prompt:\n"
        "    st.session_state.history.append(('user', prompt))\n"
        "    st.session_state.history.append(\n"
        "        ('assistant', f'你说了: {prompt}')\n"
        "    )\n"
        "\n"
        "for role, msg in st.session_state.history:\n"
        "    with st.chat_message(role):\n"
        "        st.write(msg)\n"
    )
    return src

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 必须包含聊天组件与 session_state
    code = build_chat_app()
    assert 'st.chat_message' in code, '缺少 st.chat_message'
    assert 'st.chat_input' in code, '缺少 st.chat_input'
    assert 'session_state' in code, '缺少 session_state'
    print('测试 1 通过: 包含聊天组件与 session_state')

    # 测试 2: 必须包含遍历历史的 for 循环
    assert 'for' in code, '缺少 for 循环遍历历史'
    assert 'history' in code, '缺少 history 列表'
    print('测试 2 通过: 包含遍历历史的循环')
