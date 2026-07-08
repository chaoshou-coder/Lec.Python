# Day 56 · UI + Docker

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 55 已构建 Agent;Day 54 有 RAG 系统;Day 51 有 FastAPI
>    骨架;具备基本 Linux 命令行操作
> 关键问题: 如何把"命令行"变成"用户能用的界面",并把整个应用打包
    成容器,让它在任何机器都能跑?本节完成容器化部署第一步

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— Agent 为什么必须设 max_iterations?
    工具函数里是 raise 还是 return 错误?目的:唤醒 Agent 稳定性认知,
    为今天"应用要跑在服务器,需要容器"埋伏笔。
- **赏玩 demo**(3 分钟): 现场展示一个 Streamlit 聊天界面 —— 用户
    在浏览器发消息,Agent 流式回复,旁边还能看推理轨迹。"今天你也能
    做出来"。

---

## 1. 第一讲(20 分钟) —— Streamlit 快速原型

### 知识点 1.1 安装与 5 分钟上手

```bash
pip install streamlit
```

```python
# app.py
import streamlit as st

st.title("我的 AI 助手")

# 简单输入输出
user_input = st.text_input("请输入问题")
if st.button("发送"):
    st.write(f"你说的是: {user_input}")

# 进度条
import time
if st.button("模拟耗时操作"):
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        bar.progress(i + 1)
    st.success("完成!")
```

```bash
streamlit run app.py
# 自动打开 http://localhost:8501
```

> Streamlit 特点:**纯 Python,不写一行 HTML/CSS,组件都是函数调用**。
>    适合数据类应用、内部工具、原型,不适合高并发生产。

### 知识点 1.2 核心组件速查

```python
# 文本
st.title("标题")
st.header("章节")
st.markdown("**粗体** 和 $LaTeX$")

# 输入
name = st.text_input("名字", placeholder="请输入 pwd")
age = st.slider("年龄", 0, 120, 25)
agree = st.checkbox("同意条款")
color = st.selectbox("颜色", ["红", "绿", "蓝"])

# 布局
col1, col2 = st.columns(2)
col1.metric("温度", "22℃", "+2℃")
col2.metric("湿度", "60%", "-5%")

# 文件上传
uploaded = st.file_uploader("上传文件", type=["pdf", "txt"])
if uploaded:
    content = uploaded.read().decode("utf-8")
```

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 做"AI 计算器":输入数学表达式,
    用 `eval(受限版)` 计算并显示结果;加一个"历史记录"侧边栏
    (⭐⭐,15 分钟)

> 巡场重点: 看学员是否处理了 `eval` 的安全问题(课上提示:真实项目应
>    用 `numexpr` 库);看是否用了 `st.session_state` 维护历史。

---

## 3. 第二讲(25 分钟) —— 聊天界面

### 知识点 3.1 chat_message:多轮对话 UI

```python
import streamlit as st

# 初始化会话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 接收输入
if prompt := st.chat_input("请输入..."):
    # 添加用户消息
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # 模拟助手回复
    with st.chat_message("assistant"):
        st.markdown("这是回复")
    st.session_state.messages.append(
        {"role": "assistant", "content": "这是回复"}
    )
```

> `st.session_state` 是 Streamlit 的"全局变量",刷新页面不清空。用它存
>    聊天历史、用户配置等跨轮次数据。

### 知识点 3.2 streaming:逐字输出

流式输出要用 `st.write_stream`:

```python
import time

def response_generator(question):
    # 假设这是 LLM 的流式响应
    full_response = f"这是 '{question}' 的详细答案"
    for char in full_response:
        yield char
        time.sleep(0.02)

with st.chat_message("assistant"):
    st.write_stream(response_generator(prompt))
```

> 🔴 教学红线(流式输出忘记处理): 如果用 `st.write(full_text)` 直接打
>    全文,用户会等 5 秒看到一大段 —— 必须用 `st.write_stream` 且后
>    端接口也是 stream=True。

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 把 Day 52 的流式 LLM 调用接入
    Streamlit:用户输入 → 流式显示 LLM 回复,聊天历史保存在
    `session_state`(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否调用了真实 LLM 接口(而非 mock 的
>    `time.sleep`);看是否用了 `write_stream`。

---

## 5. 第三讲(25 分钟) —— Docker 基础

### 知识点 5.1 Docker 三件套

| 概念 | 类比 | 作用 |
|---|---|---|
| 镜像(Image) | 菜谱 | 定义应用运行环境 |
| 容器(Container) | 做好的菜 | 镜像的运行实例 |
| Dockerfile | 菜谱草稿 | 描述怎么做这道菜 |

> "Build once, run anywhere" —— 在笔记本开发完了,生产环境照跑。

### 知识点 5.2 Dockerfile:AI 应用的镜像定义

```dockerfile
# 基于官方 Python 精简版镜像
FROM python:3.11-slim

# 设置容器内工作目录
WORKDIR /app

# 复制依赖清单并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用源码
COPY . .

# 暴露端口(文档作用)
EXPOSE 8000

# 启动命令(容器启动时执行)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 知识点 5.3 构建与运行

```bash
# 构建镜像(注意最后的 .)
docker build -t ai-app:0.1 .

# 运行容器
docker run -d \
  --name my-ai-app \
  -p 8000:8000 \
  --env-file .env \
  ai-app:0.1

# 查看日志
docker logs -f my-ai-app

# 停止/删除
docker stop my-ai-app && docker rm my-ai-app
```

> 🔴 教学红线(容器内访问本地服务): 容器内 `localhost` 指的是容器自
>    己,不是宿主机。连接宿主机的数据库/Redis,用 `host.docker.internal`
>    (Mac/Win)或 `--network host`(Linux)。

### 知识点 5.4 docker-compose:多服务编排

```yaml
# docker-compose.yml
version: "3.9"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - chroma    # 等 chroma 启动后再启动

  chroma:
    image: chromadb/chroma:latest
    ports:
      - "8001:8000"
    volumes:
      - chroma_data:/chroma/chroma  # 持久化

volumes:
  chroma_data:
```

```bash
# 一键启动所有服务
docker compose up -d

# 查看状态
docker compose ps

# 停掉所有服务
docker compose down
```

> docker-compose 把"启动 N 个容器的命令"写成一个文件,执行 `up` 就行,
>    适合本地开发 + 小团队。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 写一个 Dockerfile 把 Day 54 的
    RAG 应用容器化,构建镜像并启动,用 `curl` 测试 `/health` 接口
    (⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否在 Dockerfile 里复制了 `.env`(绝对不行!);看是
>    否用了 `--env-file .env` 在运行时传密钥。

---

## 7. 小项目(45 分钟) —— AI 应用容器化

把整个应用(API + Chroma + Streamlit)容器化:

```
my_ai_app/
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── main.py          # FastAPI
│   └── requirements.txt
└── web/
    ├── Dockerfile
    ├── app.py           # Streamlit
    └── requirements.txt
```

验收 checklist:
- [ ] `docker compose up -d` 启动后,`curl localhost:8000/health` 返回 ok
- [ ] `localhost:8501` 能看到 Streamlit 聊天界面
- [ ] 容器重启后数据不丢失(Chroma 用 volume 持久化)
- [ ] `.env` 不打包进镜像(`.dockerignore` 里写 `.env`)

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. Streamlit 里直接用 `st.write(全量文本)`,3 秒后一次性出现,
     而不是逐字显示
  2. Dockerfile 里 `COPY . .` 把 `.env` 也打包进镜像,push 到私有仓
     后 Key 泄漏
  3. Docker 容器内写 `localhost:5432` 连不通宿主机数据库,应该用
     `host.docker.internal:5432`
- **作业说明**: 课后 `homework/task01.py` —— 把前面任意一个 AI 应用
    (RAG 或 Agent)容器化,`docker compose up` 即可启动,下节课复盘。

---

## 易错点

1. **Streamlit 中 time.sleep 会阻塞整个页面**:耗时操作用 `st.spinner`
    包裹,或异步执行。
2. **session_state 初始化**:进页面第一件事就是 `if "key" not in st.session_state`。
3. **Docker 内 localhost 不是宿主机**:用 `host.docker.internal`。
4. **`.env` 进镜像**:`.dockerignore` 里加 `.env`,密钥用 `--env-file`
    运行时传入。
5. **容器数据不持久**:数据库/向量库必须挂 volume,否则容器一删数据就没。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(Gradio 替代, ⭐⭐)**: 用 Gradio(gr.ChatInterface)10 行代码
    实现聊天 UI,适合只做原型验证的场景。
- **(多阶段构建, ⭐⭐⭐)**: Dockerfile 用 `FROM ... AS builder` 分
    两阶段,最终镜像不含编译工具,体积从 1.2G 降到 200M。
- **(健康检查, ⭐⭐⭐)**: docker-compose 里给 api 服务加
    `healthcheck`,让编排器在服务挂掉时自动重启。
