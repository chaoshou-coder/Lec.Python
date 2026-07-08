"""
[难度: ⭐⭐⭐⭐]
[所属知识点: .env 鉴权中间件 + 路由保护]
[预计完成时间: 20 分钟]

请实现一个简单的 API Key 鉴权中间件, 要求如下:
1. 启动时通过 load_dotenv 加载 .env 的 API_KEY
2. 每个请求若访问受保护路径, 必须携带 X-Token 请求头
3. X-Token 与服务端 API_KEY 一致则放行, 否则返回 401
4. GET /protected 受保护, GET /public 不受保护
5. 使用 FastAPI 的 middleware("http") 机制

示例:
    >>> # GET /public → 200 {"msg":"free"}
    >>> # GET /protected (无 X-Token) → 401 {"detail":"未授权"}
    >>> # GET /protected (X-Token 正确) → 200 {"msg":"secret"}
"""

import os
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# TODO: 加载 .env 并读取 API_KEY 到变量 VALID_TOKEN
pass

PROTECTED_PREFIX = "/protected"

# TODO: 注册 HTTP 中间件, 校验 X-Token
pass

@app.get("/protected")
def protected():
    return {"msg": "secret"}

@app.get("/public")
def public():
    return {"msg": "free"}

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    # 测试 0: 准备 .env
    with open(".env", "w", encoding="utf-8") as f:
        f.write("API_KEY=my-secret-token\n")
    client = TestClient(app)
    # 测试 1: 公开路径无需 token
    r = client.get("/public")
    assert r.status_code == 200
    assert r.json()["msg"] == "free"
    # 测试 2: 受保护路径无 token → 401
    r = client.get("/protected")
    assert r.status_code == 401
    # 测试 3: 受保护路径带错 token → 401
    r = client.get("/protected", headers={"X-Token": "wrong"})
    assert r.status_code == 401
    # 测试 4: 受保护路径带正确 token → 200
    r = client.get("/protected", headers={"X-Token": "my-secret-token"})
    assert r.status_code == 200
    assert r.json()["msg"] == "secret"
    os.remove(".env")
    print("作业 2 通过")
