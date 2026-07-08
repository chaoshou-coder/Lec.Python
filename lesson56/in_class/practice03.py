"""
[难度: ⭐⭐]
[所属知识点: Dockerfile 编写]
[预计完成时间: 10 分钟]

场景: 实现生成 Dockerfile 内容的函数,包含 python:3.11-slim、
WORKDIR、COPY requirements、RUN pip install、COPY . .、
CMD uvicorn app:app --host 0.0.0.0 --port 8000。
验证各关键指令均存在。

示例:
    >>> content = generate_dockerfile()
    >>> 'FROM python:3.11-slim' in content
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def generate_dockerfile():
    """生成标准 Python 项目 Dockerfile 内容"""
    # 学员在此编写 Dockerfile 各行指令
    return """FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证返回内容包含基础镜像与工作目录
    content = generate_dockerfile()
    assert 'FROM python:3.11-slim' in content, \
        "缺少基础镜像 FROM python:3.11-slim"
    assert 'WORKDIR /app' in content, \
        "缺少工作目录 WORKDIR /app"
    assert 'COPY requirements.txt .' in content, \
        "缺少依赖复制 COPY requirements.txt ."
    print("测试1通过: 基础指令齐全")

    # 测试 2: 验证安装依赖、复制代码、启动命令
    assert 'RUN pip install' in content, \
        "缺少依赖安装 RUN pip install"
    assert 'COPY . .' in content, \
        "缺少全量复制 COPY . ."
    assert 'CMD' in content, "缺少 CMD 指令"
    assert '"app:app"' in content, "缺少 app:app"
    assert '--host", "0.0.0.0"' in content, "缺少 host 参数"
    assert '--port", "8000"' in content, "缺少 port 参数"
    print("测试2通过: 运行指令齐全")

    # 测试 3: 边界验证——确保内容为非空字符串
    assert isinstance(content, str), "返回值应为字符串"
    assert len(content.strip()) > 0, "Dockerfile 不应为空"
    print("测试3通过: 返回类型与长度合法")

    print("全部测试通过!")
