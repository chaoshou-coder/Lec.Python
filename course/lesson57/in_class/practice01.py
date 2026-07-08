"""
[难度: ⭐]
[所属知识点: uvicorn 命令行启动]
[预计完成时间: 5 分钟]

小张要给 FastAPI 项目写一行启动命令。
请实现 generate_run_cmd 函数,接收 app 模块名、host、
port,返回完整的 uvicorn 命令行字符串。
可选参数含 --reload、--workers 2,格式示例如下:
"uvicorn app:app --host 0.0.0.0 --port 8000 --reload"

示例:
    >>> generate_run_cmd("app", "0.0.0.0", 8000)
    'uvicorn app:app --host 0.0.0.0 --port 8000'
    >>> generate_run_cmd("main", "127.0.0.1", 8080,
    ...                  reload=True, workers=2)
    'uvicorn main:app --host 127.0.0.1 --port 8080 '
    '--reload --workers 2'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def generate_run_cmd(module, host, port,
                     reload=False, workers=None):
    """生成 uvicorn 命令行字符串。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    # 测试 1: 仅必填参数
    cmd = generate_run_cmd("app", "0.0.0.0", 8000)
    assert "uvicorn app:app" in cmd
    assert "--host 0.0.0.0" in cmd
    assert "--port 8000" in cmd
    print("测试 1 通过:", cmd)

    # 测试 2: 带 reload 与 workers
    cmd2 = generate_run_cmd("main", "127.0.0.1", 8080,
                            reload=True, workers=2)
    assert "--reload" in cmd2
    assert "--workers 2" in cmd2
    print("测试 2 通过:", cmd2)
