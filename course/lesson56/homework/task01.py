"""
[难度: ⭐⭐]
[所属知识点: requirements.txt 管理]
[预计完成时间: 10 分钟]

题目描述:
编写 freeze_deps 函数,接收包名字典 {name:version},
返回 requirements.txt 文本,每行格式为 "package==version"。
需含 httpx==0.27.0 与 pydantic==2.5.0。

示例:
    >>> freeze_deps({"httpx": "0.27.0", "pydantic": "2.5.0"})
    'httpx==0.27.0\\npydantic==2.5.0'
    >>> freeze_deps({})
    ''
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def freeze_deps(packages: dict) -> str:
    """将包名字典转换为 requirements.txt 文本"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 包含两个包的字典
    pkgs = {"httpx": "0.27.0", "pydantic": "2.5.0"}
    result = freeze_deps(pkgs)
    assert "httpx==0.27.0" in result, "缺少 httpx"
    assert "pydantic==2.5.0" in result, "缺少 pydantic"
    print("测试 1 通过:", repr(result))

    # 测试 2: 空字典返回空字符串
    assert freeze_deps({}) == "", "空字典应返回空串"
    print("测试 2 通过: 空字典返回空串")
