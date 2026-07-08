"""
[难度: ⭐⭐⭐]
[所属知识点: FastAPI + 中间件计时 + 访问日志]
[预计完成时间: 15 分钟]

生产环境需要观察每个请求的耗时。
请在 FastAPI app 中添加中间件,记录:
请求方法、路径、状态码、耗时毫秒,
并用 logging 打印 "GET / 200 12ms" 风格日志。
最后用 TestClient 调用根路径,验证日志输出含
"GET" 与 "ms" 关键字。

示例:
    >>> from fastapi.testclient import TestClient
    >>> client = TestClient(app)
    >>> _ = client.get("/")
    >>> logs = read_access_logs()
    >>> "GET /" in logs and "ms" in logs
    True
"""

import time
import logging
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

app = FastAPI()
access_logs = []


@app.get("/")
def root():
    return {"msg": "hello"}


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    """计算耗时,并写入 access_logs。"""
    pass


def read_access_logs():
    return "\n".join(access_logs)

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    client = TestClient(app)
    _ = client.get("/")
    logs = read_access_logs()
    assert "GET" in logs
    assert "ms" in logs
    print("测试 1 通过: 访问日志输出:", logs)

    _ = client.get("/")
    logs2 = read_access_logs()
    assert logs2.count("GET") >= 2
    print("测试 2 通过: 累计日志条数正确")
