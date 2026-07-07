# Day 51 · 环境管理 + Web 框架(FastAPI)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握 Python 基础、HTTP 概念(GET/POST)、PyTorch 训练;
>    假设已有 FastAPI 基础(本课程 Day 51 起快速复用)
> 关键问题: 如何把训练好的模型/AI 能力封装成 API 服务,供前端或
>    其他系统调用?本节搭建一个可运行、可测试、可部署的 API 服务骨架

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— HTTP 的 GET 和 POST 有什么区别?REST
    API 里的"资源"通常用什么词表达?(名词复数,如 `/users`)目的:唤醒
    Web 基础认知,为"路由设计"埋伏笔。
- **赏玩 demo**(3 分钟): 现场启动一个 FastAPI 服务,浏览器打开
    `http://localhost:8000/docs`,展示自动生成的交互式 API 文档 ——
    "你写几个 Python 函数,Swagger UI 就自动出现,不用手写前端"。

---

## 1. 第一讲(20 分钟) —— 虚拟环境与依赖管理

### 知识点 1.1 venv:项目隔离的"房间"

每个项目装一个"独立房间",A 项目用 Pytorch 2.0、B 项目用 2.5,
互不干扰。

```bash
# 创建虚拟环境(在项目根目录)
python -m venv .venv

# 激活(Mac/Linux)
source .venv/bin/activate

# 激活(Windows)
.venv\Scripts\activate

# 退出
deactivate
```

> 口诀:**一进房间就 activate,离开就 deactivate**。
>
> 🔴 教学红线(全局安装): 直接 `pip install fastapi` 装到全局,会导致
>    多个项目依赖冲突。必须先激活 venv 再装,确保依赖"住"在这个房间。

### 知识点 1.2 requirements.txt:依赖清单

把当前环境所有包导出成清单,别人(或服务器)照着装一份一模一样的。

```bash
# 导出依赖
pip freeze > requirements.txt

# 在新环境安装
pip install -r requirements.txt
```

### 知识点 1.3 `.env` 密钥管理

API Key 绝不能写死在代码里 —— 要放在 `.env` 文件,用 `python-dotenv`
读取,并把 `.env` 加入 `.gitignore`。

```env
# .env(不提交到 git!)
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://user:pw@localhost/db
```

```python
# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # 自动读取 .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

> 🔴 教学红线(API Key 硬编码): 把 `sk-xxx` 直接写进 `.py` 文件、提交
>    到 GitHub,会被机器人秒扫盗刷。必须 `.env` + `.gitignore`。养成习
>    惯:先 `git init`,第一个文件就写 `.gitignore`,里面加 `.env`。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 创建 venv、装 fastapi/uvicorn/
    python-dotenv,导出 requirements.txt,写一个读取 `.env` 的 `config.py`
    (⭐⭐,15 分钟)

> 巡场重点: 看学员是否在 venv 内执行 pip(终端提示符前有 `(.venv)`);
>    看 `.gitignore` 是否包含 `.env`。

---

## 3. 第二讲(25 分钟) —— FastAPI 入门

### 知识点 3.1 第一个 FastAPI 应用

FastAPI 用"路由 + 函数"映射 HTTP 请求,自动生成文档。

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="AI 应用服务")

# GET 请求:http://localhost:8000/
@app.get("/")
def root():
    return {"message": "Hello AI Engineer"}

# 带路径参数:http://localhost:8000/users/42
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

```bash
# 启动(热重载)
uvicorn main:app --reload
```

### 知识点 3.2 请求体(Pydantic 模型)

POST 请求的参数用 Pydantic 模型定义,自动做类型校验 + 文档生成。

```python
from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    # 必填字段 + 文档说明
    message: str = Field(..., description="用户输入的消息")
    temperature: float = Field(0.7, ge=0.0, le=2.0)
    # 可选字段
    user_id: Optional[str] = None

@app.post("/chat")
def chat(req: ChatRequest):
    # req 已经过类型校验,可直接用
    return {"reply": f"你说了: {req.message}"}
```

> Pydantic 自动校验:如果客户端传 `"temperature": "abc"`,FastAPI 返回
>    友好的 422 错误(指出哪个字段类型错),不用手写 if 判断。

### 知识点 3.3 自动文档(/docs 和 /redoc)

启动后访问:
- `/docs` —— Swagger UI,可在浏览器直接点"Try it out"发请求
- `/redoc` —— 更清晰的静态文档

> 调试 API 再也不用 Postman 手写参数 —— 直接浏览器里点。

### 知识点 3.4 响应模型

用 `response_model` 约束输出结构,隐藏内部字段:

```python
class ChatResponse(BaseModel):
    reply: str
    tokens_used: int

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    return ChatResponse(reply="你好", tokens_used=42)
```

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 实现 `/models` 接口(GET),返回
    模型列表;实现 `/predict` 接口(POST),接受 `{"input": "..."}` 返回
    `{"output": "..."}`(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否定义 Pydantic 模型而非用 `dict`;看 `/docs` 是否
>    能正常打开并测试。

---

## 5. 第三讲(20 分钟) —— 异步端点 + 依赖注入

### 知识点 5.1 async def:异步不阻塞

调用 LLM API 通常要等 1-5 秒,用 `async def` 让等待期间处理其他请求,
避免"排队等公交车"。

```python
import httpx

@app.post("/chat")
async def chat(req: ChatRequest):
    # httpx 支持异步,等 LLM 响应时不阻塞其他请求
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.openai.com/v1/chat/completions",
            json={"model": "gpt-4o", "messages": [
                {"role": "user", "content": req.message}
            ]},
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            timeout=30.0,
        )
    return resp.json()
```

> 注意:`async def` 内必须用 `await`,且调用的库必须支持异步(httpx,不是
>     requests)。如果业务全是 CPU 计算,不要用 async,反而慢。

### 知识点 5.2 依赖注入(DI):共用逻辑抽离

多个接口都要"校验 API Key",用 `Depends()` 抽出来:

```python
from fastapi import Depends, Header, HTTPException

# 依赖函数:从请求头取 token 并校验
async def verify_token(authorization: str = Header(...)):
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=401, detail="无效 token")
    return authorization

# 在路由中使用依赖
@app.get("/admin", dependencies=[Depends(verify_token)])
def admin():
    return {"msg": "管理员页面"}
```

> DI 的价值:鉴权/数据库连接/配置加载等共用逻辑,抽一处定义、多处复用,
>    测试时也方便替换。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 把 `/chat` 改为 `async def`,用
    依赖注入实现一个"限流"(每分钟 5 次)的 counter,超限返回 429
    (⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否在 `async def` 内正确使用 `await`;看限流逻辑是
>    否用了全局变量(单进程可行,多进程要改 Redis)。

---

## 7. 小项目(45 分钟) —— API 服务骨架

搭一个完整的 AI 应用 API 骨架:

```
project/
├── .env                  # API Key(API Key 不提交)
├── .gitignore
├── requirements.txt
├── config.py             # 读取 .env
├── main.py               # FastAPI 入口
├── routers/
│   ├── chat.py           # /chat 路由
│   └── health.py         # /health 健康检查
└── schemas.py            # Pydantic 模型
```

实现:
- `/health` 返回 `{"status": "ok"}`(部署时必用)
- `/chat` 接受消息,返回 mock 回复(明天接入真实 LLM)
- 启动时打印"加载配置成功,Key 长度: xx"(不打印 Key 本身!)

```python
# main.py
from fastapi import FastAPI
from routers import chat, health

app = FastAPI(title="AI 应用服务 v0.1")
app.include_router(health.router, tags=["健康检查"])
app.include_router(chat.router, prefix="/api", tags=["聊天"])
```

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 忘记激活 venv,依赖装到全局,另一项目装包时报版本冲突
  2. 把 `OPENAI_API_KEY=sk-xxx` 直接写在 `.py` 文件里,push 到 GitHub
  3. 在 `async def` 里用同步的 `requests`,整个服务卡死
- **作业说明**: 课后 `homework/task01.py` —— 用依赖注入实现"请求日志"
    (打印 method + path + 耗时),下节课前 10 分钟复盘。

---

## 易错点

1. **venv 没激活**: `which python` 检查,应指向 `.venv/bin/python`。
2. **`.env` 提交进 git**: `.gitignore` 第一行就写 `.env`。
3. **async 内用 requests**: 会报 `TypeError`,应改成 `httpx.AsyncClient`。
4. **Pydantic 模型返回 ORM**: 直接 `return db_obj` 报错,要用
    `response_model` 或手动转 dict。
5. **路由顺序**: `@app.get("/users/{id}")` 写在 `@app.get("/users/me")`
    之后会导致 `/users/me` 被当 `{id}="me"` 捕获 —— 静态路由放前面。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(中间件, ⭐⭐)**: 实现 CORSMiddleware,允许前端
    `http://localhost:3000` 跨域访问 API —— 真实前后端分离必备。
- **(版本化路由, ⭐⭐⭐)**: 用 `prefix="/api/v1"` 和 `prefix="/api/v2"`
    挂两套路由,体会 API 版本管理思路。
- **(环境切换, ⭐⭐⭐⭐)**: 用 `ENV=development/production` 切换配置,
    开发环境打印详细日志、生产环境关闭 `/docs`。
