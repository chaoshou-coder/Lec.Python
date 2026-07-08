"""
[难度: ⭐⭐]
[所属知识点: FastAPI 路由 GET/POST 基础]
[预计完成时间: 10 分钟]

请使用 FastAPI 创建一个最简单的推理服务, 包含两个路由:
1. GET /  → 返回 {"status": "ok"} 健康检查
2. POST /predict → 接收 {"input": str}, 返回 {"output": str}
其中 predict 先把 input 原样返回(真实场景会调用模型推理)。
服务入口为 app, 使用 uvicorn 启动时可用 uvicorn practice04:app。

示例:
    >>> # GET / → 200 {"status":"ok"}
    >>> # POST /predict {"input":"hello"} → 200 {"output":"hello"}
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class PredictRequest(BaseModel):
    """请求体"""
    # TODO: 定义 input 字段 (str)
    pass

class PredictResponse(BaseModel):
    """响应体"""
    # TODO: 定义 output 字段 (str)
    pass

# TODO: 补全 GET / 路由
# TODO: 补全 POST /predict 路由

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    client = TestClient(app)
    # 测试 1: 健康检查
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
    # 测试 2: 预测接口正向
    r = client.post("/predict", json={"input": "你好"})
    assert r.status_code == 200
    assert r.json()["output"] == "你好"
    # 测试 3: 预测接口边界 (空字符串)
    r = client.post("/predict", json={"input": ""})
    assert r.status_code == 200
    assert r.json()["output"] == ""
    print("练习 4 通过")
