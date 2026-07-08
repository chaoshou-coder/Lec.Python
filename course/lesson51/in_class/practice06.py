"""
[难度: ⭐⭐⭐]
[所属知识点: 教学红线 — API Key 硬编码 vs .env 调试]
[预计完成时间: 15 分钟]

你接手了一篇"能跑"的 FastAPI 代码, 但同事把 API Key 写死在了代码里,
这是重大安全隐患。请找出硬编码位置, 用 python-dotenv 替换,
并新增 /config(GET) 路由返回当前加载的 Key 后四位(脱敏显示)。
修改量已标出在 TODO 处, 不要改动其他代码。

示例:
    >>> # 修改前: API_KEY = "sk-live-abcdef123456"
    >>> # 修改后: 从 .env 的 API_KEY 读取
    >>> # GET /config → {"key_suffix": "*" * 8 + "23456"}
"""

import os
from fastapi import FastAPI

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# TODO: 导入 load_dotenv 并加载 .env
# TODO: 把下面这行硬编码改成从环境变量读取
API_KEY = "sk-live-abcdef123456"  # 教学红线: 硬编码, 必须改掉

def mask_key(k: str) -> str:
    """只显示最后 4 位, 其余用 * 替代"""
    if len(k) <= 4:
        return "*" * len(k)
    return "*" * (len(k) - 4) + k[-4:]

@app.get("/config")
def config():
    # TODO: 返回脱敏后的 key
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    # 测试 0: 写入临时 .env
    with open(".env", "w", encoding="utf-8") as f:
        f.write("API_KEY=sk-live-abcdef123456\n")
    # NOTE: 学员需在自己代码里调用 load_dotenv()
    # 下面 reload 模块以获取修改后的值
    import importlib, sys
    client = TestClient(app)
    r = client.get("/config")
    assert r.status_code == 200
    suffix = r.json()["key_suffix"]
    # 测试 1: 后缀应为 *******3456
    assert suffix.endswith("23456") or suffix.endswith("3456")
    # 测试 2: 前段应为 *
    assert suffix.startswith("*")
    # 测试 3: 清理
    os.remove(".env")
    print("练习 6 通过")
