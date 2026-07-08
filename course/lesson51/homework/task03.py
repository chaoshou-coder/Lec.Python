"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Pydantic 高级校验 + FastAPI 异常处理]
[预计完成时间: 20 分钟]

请为推理服务实现一个带自定义校验的 /train 接口。训练请求需满足:
1. dataset 字段: 字符串, 长度 1~100, 且必须以 .csv 或 .json 结尾
2. epochs 字段: 整数, 范围 [1, 100], 默认 10
3. lr (学习率) 字段: 浮点数, 范围 (0, 1], 默认 0.001
4. 任一校验失败返回 422, 成功返回 {"status": "training", "params": {...}}
5. 用 Pydantic 的 field_validator 校验 dataset 后缀

示例:
    >>> # POST /train {"dataset":"data.csv","epochs":5,"lr":0.01}
    >>> # → 200 {"status":"training","params":{...}}
    >>> # POST /train {"dataset":"data.txt","epochs":5,"lr":0.01}
    >>> # → 422 (后缀不合法)
"""

from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import Optional

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class TrainRequest(BaseModel):
    """训练请求"""
    dataset: str
    epochs: Optional[int] = 10
    lr: Optional[float] = 0.001

    # TODO: 为 dataset 添加 field_validator, 限制后缀
    pass

@app.post("/train")
def train(req: TrainRequest):
    # TODO: 返回 status 与 params
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    client = TestClient(app)
    # 测试 1: 合法 .csv
    r = client.post("/train",
                    json={"dataset": "train.csv", "epochs": 5,
                          "lr": 0.01})
    assert r.status_code == 200
    d = r.json()
    assert d["status"] == "training"
    assert d["params"]["epochs"] == 5
    # 测试 2: 合法 .json + 默认值
    r = client.post("/train",
                    json={"dataset": "train.json"})
    assert r.status_code == 200
    assert r.json()["params"]["epochs"] == 10
    assert r.json()["params"]["lr"] == 0.001
    # 测试 3: 非法后缀
    r = client.post("/train",
                    json={"dataset": "train.txt"})
    assert r.status_code == 422
    # 测试 4: 边界 lr = 0
    r = client.post("/train",
                    json={"dataset": "a.csv", "lr": 0})
    assert r.status_code == 422
    # 测试 5: 边界 epochs 超限
    r = client.post("/train",
                    json={"dataset": "a.csv", "epochs": 200})
    assert r.status_code == 422
    print("作业 3 通过")
