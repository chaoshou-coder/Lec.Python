"""
[难度: ⭐⭐⭐]
[所属知识点: FastAPI 路由 + Pydantic 模型综合]
[预计完成时间: 15 分钟]

请为训练营的模型推理服务实现一个完整的 /chat 接口, 接口需满足:
1. POST /chat 接收 ChatRequest (history 列表 + message 字符串)
2. 校验: history 每条必须含 role 与 content 两个字段
3. 返回 ChatResponse, 包含 reply 字符串与 turns 整数
4. 业务规则: reply 直接返回 "echo: {message}" (占位)
5. turns = len(history) + 1

示例:
    >>> # POST /chat {"message":"你好","history":[]}
    >>> # → {"reply":"echo: 你好","turns":1}
    >>> # POST /chat {"message":"再见","history":[{"role":"user","content":"hi"}]}
    >>> # → {"reply":"echo: 再见","turns":2}
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ChatTurn(BaseModel):
    """单轮对话"""
    # TODO: 定义 role 与 content
    pass

class ChatRequest(BaseModel):
    """聊天请求"""
    message: str
    # TODO: 定义 history, 默认为空列表
    pass

class ChatResponse(BaseModel):
    """聊天响应"""
    # TODO: 定义 reply 与 turns
    pass

# TODO: 实现 POST /chat 路由
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    client = TestClient(app)
    # 测试 1: 无历史
    r = client.post("/chat", json={"message": "你好", "history": []})
    assert r.status_code == 200
    d = r.json()
    assert d["reply"] == "echo: 你好"
    assert d["turns"] == 1
    # 测试 2: 带历史
    r = client.post("/chat",
                    json={"message": "再见",
                          "history": [{"role": "user", "content": "hi"}]})
    d = r.json()
    assert d["reply"] == "echo: 再见"
    assert d["turns"] == 2
    # 测试 3: 字段缺失应 422
    r = client.post("/chat",
                    json={"message": "test",
                          "history": [{"role": "user"}]})
    assert r.status_code == 422
    print("作业 1 通过")
