"""
[难度: ⭐⭐]
[所属知识点: Dockerfile 多阶段构建]
[预计完成时间: 10 分钟]

生产镜像要尽可能小。请实现
generate_dockerfile 函数,返回一段多阶段构建文本:
- 第一阶段 python:3.11 构建依赖,命名 AS build
- 第二阶段 python:3.11-slim 作为最终镜像
- 用 COPY --from=build 拷贝构建产出
调用后用 "AS build" 与 "COPY --from" 验证。

示例:
    >>> df = generate_dockerfile()
    >>> "AS build" in df and "COPY --from" in df
    True
    >>> "python:3.11-slim" in df
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def generate_dockerfile():
    """返回多阶段 Dockerfile 文本。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    # 测试 1: 关键指令存在
    df = generate_dockerfile()
    assert "AS build" in df
    assert "COPY --from" in df
    print("测试 1 通过: 多阶段指令正确")

    # 测试 2: 基础镜像正确
    assert "python:3.11" in df
    assert "python:3.11-slim" in df
    print("测试 2 通过: 基础镜像配置正确")
