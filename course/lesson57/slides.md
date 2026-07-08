# Day 57 · 部署 + 监控

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 56 已容器化 AI 应用;具备基本 Linux 命令行知识;
>    了解 HTTP 与反向代理概念
> 关键问题: 如何让应用稳定跑在云平台,用户能真正访问到?上线后
    怎么知道它是否正常?本节完成应用上线 + 基础监控闭环

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— docker-compose 里 `depends_on` 的
    作用?容器内数据如何持久化?目的:唤醒容器编排认知,为今天"应用
    上云后如何保持稳定运行"埋伏笔。
- **赏玩 demo**(3 分钟): 展示一个部署在云上的应用 —— 浏览器输入
    域名返回 AI 回答,Grafana 面板显示"今天 1423 次请求,99.2%
    成功率"。"今天你也能做到"。

---

## 1. 第一讲(20 分钟) —— 云平台概览

### 知识点 1.1 主流云平台对比

| 平台 | 特点 | 适用 |
|---|---|---|
| AWS | 功能最全,市场份额最大 | 出海、大厂 |
| GCP | AI/ML 生态强 | 数据+K8s 重度 |
| 阿里云 | 国内合规、中文支持好 | 国内客户项目 |
| 腾讯云 | 游戏+社交生态强 | 国内中小项目 |
| 阿里云轻量 | 便宜,简单 | 学生/个人项目 |

> 本课程选用 **阿里云轻量应用服务器**(￥40/月,2 核 2G)作为实践平
>    台,操作命令在所有 Linux 上通用。

### 知识点 1.2 服务器上线流程概览

```
① 购买一台云服务器(CentOS / Ubuntu)
② SSH 登录 → 安装 Docker
③ 上传代码(git clone 或 scp)
④ docker compose up -d
⑤ 配置 nginx 反向代理(域名 → 容器端口)
⑥ 开通防火墙(只留 80/443)
⑦ 启动并验证
```

> 口诀:**买机器 → 装 Docker → 传代码 → 拉镜像 → 跑容器 → 配反代**。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 在阿里云轻量购买一台最低配
    服务器(已在课前完成),SSH 登录,装 Docker,上传 Day 56 的应用
    并启动(⭐⭐⭐,15 分钟)

> 巡场重点: 看学员是否用 `root` 登录后切换普通用户执行 docker;看是
>    否关掉了 SSH 密码登录(后续讲)。

---

## 3. 第二讲(25 分钟) —— FastAPI + Uvicorn + nginx

### 知识点 3.1 uvicorn:ASGI 服务器

Uvicorn 是 FastAPI 的"发动机",处理并发请求:

```bash
# 开发模式(单进程)
uvicorn main:app --reload

# 生产模式(多进程 + 预加载)
uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4 \          # worker 数 = CPU 核心数 × 2
  --access-log
```

> 开发用 `--reload`(代码修改自动重启),生产用 `--workers`(多进程并
>    发,充分利用多核)。

### 知识点 3.2 nginx 反向代理:域名进容器

用户访问 `example.com` → nginx(80 端口) → 转发给容器内的
`localhost:8000`。

```nginx
# /etc/nginx/conf.d/ai-app.conf
server {
    listen 80;
    server_name ai.example.com;

    # 静态文件由 nginx 直接返回,不经过后端
    location /static/ {
        alias /var/www/ai-app/static/;
    }

    # 其他请求反向代理到 FastAPI 容器
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # 流式响应必须关掉缓冲
        proxy_buffering off;
        proxy_read_timeout 300s;
    }
}
```

> 🔴 教学红线(proxy_buffering on 破坏流式): 默认 nginx 会缓冲整个
>    响应后再发给用户,导致"打字机效果"失效。Stream 类接口必须
>    `proxy_buffering off` + `proxy_read_timeout` 调大。

### 知识点 3.3 HTTPS(Certbot 免费证书)

```bash
# 安装 Certbot
sudo apt install certbot python3-certbot-nginx

# 自动申请 + 配置(把上面 80 端口配置自动加 443)
sudo certbot --nginx -d ai.example.com
# 证书 90 天自动续期(certbot 已加 cron)
```

> HTTPS 已经是标配 —— 不加密的 HTTP 会被浏览器标"不安全",且可被
>    抓包劫持 API Key。

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 写一个 nginx 配置文件,把
    `example.com/api/` 反代到 `localhost:8000`,`/static/` 直接返回;
    写 docker compose 让应用跑在 8000(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否在反代配置里保留了 `proxy_set_header`
>    (后端拿到的 Host 会是 127.0.0.1);看是否加了 `proxy_buffering off`。

---

## 5. 第三讲(25 分钟) —— 日志 + 健康检查 + CI/CD 概念

### 知识点 5.1 结构化日志

普通 `print` 查问题太慢,生产用 `logging` + JSON 格式:

```python
import logging
import json
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def log_request(path: str, status: int, duration_ms: float):
    # 结构化:方便 ELK / Loki 检索
    logging.info(json.dumps({
        "event": "request",
        "path": path,
        "status": status,
        "duration_ms": duration_ms,
    }))

# 输出:2026-07-08 10:30:00 INFO
#      {"event": "request", "path": "/chat", "status": 200, ...}
```

> 生产环境用 JSON 格式,可直接导入 Elasticsearch/Loki 做聚合分析,不用
>    `grep` 排查。

### 知识点 5.2 健康检查端点

```python
@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.1.0",
        "uptime_seconds": time.time() - START_TIME,
        "dependencies": {
            "llm_api": check_llm(),
            "vector_db": check_chroma(),
        }
    }
```

> 云平台会定期 GET `/health`,连续 3 次失败自动重启容器 —— 是应用稳
>    定性的最后一道防线。

### 知识点 5.3 CI/CD 概念(GitHub Actions 了解级别)

CI = 提交代码自动跑测试,CD = 自动部署到服务器:

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 运行测试
        run: pip install -r requirements.txt && pytest
      - name: 部署到服务器
        run: |
          ssh user@${{ secrets.HOST }} \
            "cd /app && git pull && docker compose up -d --build"
```

> 课上不深入写 —— 知道"把代码 push 到 main 分支,服务器自动拉取部署"
>    这个概念即可,实际工作里通常由 DevOps 配置。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在 Day 56 的应用上加 `/health`
    端点(返回 status + LLM 连通性),加结构化请求日志(打印 method +
    path + 耗时 ms),docker compose 加健康检查配置(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员的 `/health` 是否真实检测依赖(而不是永远返回
>    ok);看 docker-compose 里是否写了 `healthcheck` 配置块。

---

## 7. 小项目(45 分钟) —— 应用上线 + 健康检查

完成可上线部署的完整方案:

```
deploy/
├── nginx.conf           # 反代配置
├── docker-compose.yml   # 含 healthcheck
├── setup.sh             # 一键部署脚本
└── main.py              # 含 /health 和结构化日志
```

`setup.sh`:
```bash
#!/bin/bash
set -e
echo ">>> 安装 Docker"
curl -fsSL https://get.docker.com | sh
echo ">>> 拉代码"
git clone <your-repo> /app
cd /app
echo ">>> 启动"
docker compose up -d
echo ">>> 配置 nginx"
cp deploy/nginx.conf /etc/nginx/conf.d/
nginx -s reload
echo ">>> 启动完成,检查健康"
curl -s http://localhost:8000/health | python -m json.tool
```

验收清单:
- [ ] 服务器 IP 直接访问能通
- [ ] `/health` 返回 200 + 依赖状态
- [ ] 容器异常退出后自动重启(restart: always)
- [ ] 代码 push 后不用手动 ssh 部署(只做了解)

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. nginx 反代没关 proxy_buffering,流式接口变成一次性返回,CLS
     评分暴跌
  2. `/health` 永远返回 `{"status": "ok"}` 但没真检测依赖,服务挂了
     几分钟才被发现
  3. 把 `.env` 直接 scp 到服务器,SSH 历史泄漏了 API Key
- **作业说明**: 课后 `homework/task01.py` —— 把 Day 56 容器化的应用
    部署到阿里云轻量,同学互 ping `/health` 验证访问性。

---

## 易错点

1. **proxy_buffering off**: 流式接口必须关,否则逐字输出失效。
2. **健康检查 '/health' 要真检测**:别只做"返回 ok",要测 LLM/向量库。
3. **worker 数不要超过 2×CPU**: 4 核机器开 8 worker 最合适,开 100
    个反而上下文切换拖慢。
4. **敏感配置不进 git**: `.env` + `.dockerignore` 双重保险。
5. **防火墙只留 80/443**: SSH 端口改高位(如 22222),防爆破。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(ssl 安全加固, ⭐⭐)**: nginx 加上 TLS 1.3 only + HSTS,换
    SSL Labs A+ 评分 —— 面试加分项,运维基础。
- **(Prometheus 监控, ⭐⭐⭐⭐)**: 用 prometheus-fastapi-instrumentator
    库暴露请求量/延迟指标,Grafana 接入做图表。
- **(蓝绿部署, ⭐⭐⭐⭐⭐)**: docker-compose 起新旧两套服务,
    nginx 切换 upstream,实现零停机更新 —— 高级部署模式，了解即可。
