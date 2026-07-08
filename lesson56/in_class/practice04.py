"""
[难度: ⭐⭐]
[所属知识点: docker-compose 编写]
[预计完成时间: 10 分钟]

场景: 实现生成 docker-compose.yml 内容的函数,包含 services:
web (build + ports 8000:8000 + volumes + env_file)。
验证输出字符串含关键指令与正确端口映射。

示例:
    >>> '8000:8000' in generate_compose()
    True
    >>> 'build: .' in generate_compose()
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def generate_compose():
    """生成标准 docker-compose.yml 内容"""
    # 学员在此编写 docker-compose.yml 字符串
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 返回非空字符串
    content = generate_compose()
    assert isinstance(content, str), "应返回字符串"
    assert len(content) > 0, "不应返回空串"
    print("测试 1 通过: 返回非空字符串")

    # 测试 2: 验证 web 服务关键字段齐全
    assert 'services' in content, "缺少 services"
    assert 'build' in content, "缺少 build 字段"
    assert 'ports' in content, "缺少 ports 字段"
    assert 'volumes' in content, "缺少 volumes 字段"
    assert 'env_file' in content, "缺少 env_file 字段"
    print("测试 2 通过: web 服务字段齐全")

    # 测试 3: 验证端口映射 8000:8000 存在
    assert '8000:8000' in content, (
        "缺少端口映射 8000:8000"
    )
    print("测试 3 通过: 端口映射存在")

    print("全部测试通过!")
