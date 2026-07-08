"""
[难度: ⭐⭐⭐⭐]
[所属知识点: CLI 问答程序]
[预计完成时间: 20 分钟]

写一个 CLI 问答程序 cli_qa.py:
1. 用户选择模型(从预设列表选)
2. 进入循环,用户输入问题
3. 支持命令:
   - /reset   : 清空对话历史
   - /bye     : 退出
   - /switch  : 切换模型
4. 调用 ollama.chat 获取回复并打印
5. try/except 捕获 Ollama 未运行/未安装,
   友好提示 "请先安装并启动 Ollama"。

示例:
    >>> 选择模型: 1
    已选择 qwen2.5:0.5b
    > 你好
    你好!有什么可以帮你?
    > /bye
    再见!
"""

# ======================
# 学员代码区
# ======================
def cli_qa():
    # 1. 预设模型列表
    models = [
        "qwen2.5:0.5b",
        "qwen2.5:1.5b",
        "qwen2.5:3b",
    ]

    # 2. 让用户选择模型
    # 3. 进入 while True 循环
    # 4. 处理 /reset /bye /switch
    # 5. 调用 ollama.chat
    # 6. try/except 友好提示
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程(交互式)
    try:
        cli_qa()
    except KeyboardInterrupt:
        print("\n用户中断退出")

    # 测试 2: 验证模型列表
    models = ["qwen2.5:0.5b", "qwen2.5:1.5b", "qwen2.5:3b"]
    print(f"可用模型: {models}")

    # 测试 3: 验证命令解析逻辑
    test_inputs = ["/reset", "/bye", "/switch", "你好"]
    for cmd in test_inputs:
        if cmd.startswith("/"):
            print(f"命令: {cmd}")
        else:
            print(f"问题: {cmd}")
