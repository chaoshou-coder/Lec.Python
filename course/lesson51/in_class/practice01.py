"""
[难度: ⭐]
[所属知识点: venv 环境创建与激活]
[预计完成时间: 5 分钟]

你正在准备开发一个 FastAPI 推理服务。为避免依赖污染系统 Python,
请使用标准库 venv 模块创建名为 fastapi_env 的虚拟环境, 并在终端激活。
Windows 与 macOS/Linux 激活命令不同, 请补全下方代码区和测试区的命令。

示例:
    >>> python -m venv fastapi_env  # 创建
    >>> source fastapi_env/bin/activate  # macOS/Linux 激活
    终端前缀出现 (fastapi_env) 即成功
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# TODO: 写出创建虚拟环境的命令 (1 行)
create_cmd = ""

# TODO: 写出 macOS/Linux 下激活命令 (1 行)
activate_unix = ""

# TODO: 写出 Windows 下激活命令 (1 行)
activate_win = ""

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 创建命令应包含 venv 与 fastapi_env
    assert "venv" in create_cmd and "fastapi_env" in create_cmd
    # 测试 2: 激活命令应包含 bin/activate (Unix)
    assert "activate" in activate_unix
    # 测试 3: 不应为空
    assert len(activate_win.strip()) > 0
    print("练习 1 通过")
