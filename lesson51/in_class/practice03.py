"""
[难度: ⭐⭐]
[所属知识点: python-dotenv 读取 .env 文件]
[预计完成时间: 10 分钟]

项目根目录下有 .env 文件, 内容如下:
    API_KEY=sk-test-abc123
    MODEL_NAME=qwen-max
请用 python-dotenv 库中的 load_dotenv 与 os.environ 读取这两个值,
并把它们赋值给全局变量 api_key 与 model_name, 最后打印确认。
(教学红线提示: API Key 永远不要出现在代码里, 必须走 .env。)

示例:
    >>> # 假设 .env 已存在
    >>> python practice03.py
    API_KEY=sk-test-abc123
    MODEL_NAME=qwen-max
"""

import os

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# TODO: 导入 load_dotenv (1 行)
pass

def load_config():
    """加载 .env 并返回 (api_key, model_name)"""
    # TODO: 调用 load_dotenv 加载 .env 文件
    pass
    # TODO: 通过 os.environ.get 读取两个变量
    api_key = ""
    model_name = ""
    return api_key, model_name

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 先写入临时 .env 供测试
    with open(".env", "w", encoding="utf-8") as f:
        f.write("API_KEY=sk-test-abc123\nMODEL_NAME=qwen-max\n")
    k, m = load_config()
    # 测试 2: 值应正确读取
    assert k == "sk-test-abc123"
    assert m == "qwen-max"
    # 测试 3: 清理测试文件
    os.remove(".env")
    print("练习 3 通过")
