"""
[难度: ⭐]
[所属知识点: openai SDK 安装与环境变量]
[预计完成时间: 5 分钟]

某 AI 工程师搭建 LLM 调用环境。要求:
1) 用 python-dotenv 从 .env 文件加载 OPENAI_API_KEY 与 OPENAI_BASE_URL
2) 用 openai 包创建 OpenAI 客户端实例 client
3) 打印客户端的 api_key 长度(不打印明文)

示例:
    >>> main()
    client 创建成功, api_key 长度: 32
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载 .env, 并创建 OpenAI 客户端
load_dotenv()
client = OpenAI()                          # 自动读取环境变量


def main() -> None:
    key = os.getenv("OPENAI_API_KEY", "")
    print(f"client 创建成功, api_key 长度: {len(key)}")


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 能正常创建 client 并打印长度
    main()
    # 测试 2: 验证 api_key 非空
    assert len(os.getenv("OPENAI_API_KEY", "")) > 0, "api_key 为空"
