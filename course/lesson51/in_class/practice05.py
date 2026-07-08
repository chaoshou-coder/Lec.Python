"""
[难度: ⭐⭐⭐]
[所属知识点: Pydantic 模型校验 + 字段约束]
[预计完成时间: 15 分钟]

推理服务需要升级请求体校验: temperature 取值范围 [0.0, 2.0],
max_tokens 取值范围 [1, 4096], 且必须为正整数。请使用 Pydantic
的 Field 与类型注解, 为 PredictRequest 加上这两个带约束的字段,
并提供合理默认值 temperature=0.7、max_tokens=256。

示例:
    >>> # temperature=3.0 → 422 校验失败
    >>> # temperature=1.0, max_tokens=100 → 200 成功
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class PredictRequest(BaseModel):
    """带校验的请求体"""
    input: str
    # TODO: 定义 temperature, 范围 0~2, 默认 0.7
    # TODO: 定义 max_tokens, 范围 1~4096, 默认 256
    pass

@app.post("/predict")
def predict(req: PredictRequest):
    # 直接回显, 真实场景会调用模型
    return {"output": req.input,
            "temperature": req.temperature,
            "max_tokens": req.max_tokens}

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    client = TestClient(app)
    # 测试 1: 合法输入
    r = client.post("/predict",
                    json({"input": "hi", "temperature": 1.0,
                          "max_tokens": 100})
    assert r.status_code == 200
    d = r.json()
    assert d["temperature"] == 1.0 and d["max_tokens"] == 100
    # 测试 2: 边界 temperature 超限
    r = client.post("/predict",
                    json({"input": "hi", "temperature": 3.0}))
    assert r.status_code == 422
    # 测试 3: 边界 max_tokens = 0
    r = client.post("/predict",
                    json({"input": "hi", "max_tokens": 0}))
    assert r.status_code == 422
    print("练习 5 通过")
