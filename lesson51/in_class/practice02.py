"""
[难度: ⭐⭐]
[所属知识点: requirements.txt 依赖管理]
[预计完成时间: 10 分钟]

虚拟环境已激活, 现在需要把项目依赖写入 requirements.txt 文件, 当前项目需要
fastapi==0.115.0、uvicorn==0.30.6、pydantic==2.9.2、python-dotenv==1.0.1。
请补全依赖文件和一键安装命令, 然后再冻结当前环境到 freeze.txt。

示例:
    >>> # requirements.txt 内容示例
    fastapi==0.115.0
    >>> pip install -r requirements.txt
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
requirements_lines = [
    # TODO: 补全 4 个依赖及其版本号
    "",
    "",
    "",
    "",
]

# TODO: 写出通过 requirements.txt 安装依赖的命令 (1 行)
install_cmd = ""

# TODO: 写出冻结当前环境到 freeze.txt 的命令 (1 行)
freeze_cmd = ""

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 列表中应有 4 条依赖
    nonempty = [l for l in requirements_lines if l.strip()]
    assert len(nonempty) == 4
    # 测试 2: 必须包含 fastapi 与 uvicorn
    text = "\n".join(requirements_lines)
    assert "fastapi" in text and "uvicorn" in text
    # 测试 3: 安装命令必须引用 requirements.txt
    assert "requirements.txt" in install_cmd
    # 测试 4: 冻结命令必须输出到 freeze.txt
    assert "freeze" in freeze_cmd and "freeze.txt" in freeze_cmd
    print("练习 2 通过")
