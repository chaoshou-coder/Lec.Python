"""
[难度: ⭐⭐]
[所属知识点: API Key 管理 + openai 客户端创建]
[预计完成时间: 10 分钟]

场景: 某工程师要构建可复用 LLM 客户端工厂。
请创建 create_llm_client 函数,从 .env 加载环境变量,
返回 OpenAI 客户端。要求:
- 必须提供 api_key(缺失时 raise ValueError)
- 可选 base_url(兼容第三方代理端点)
- 打印客户端 base_url 与 api_key 长度(隐藏明文)

教学红线(正面提醒):绝不在代码中硬编码 API Key,
必须用 .env 加载,保护密钥安全。

示例:
    >>> client = create_llm_client()
    base_url: https://api.openai.com/v1
    api_key 长度: 16
"""
import os
from dotenv import load_dotenv
from openai import OpenAI


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def create_llm_client():
    """从 .env 加载配置,创建并返回 OpenAI 客户端"""
    # TODO: 调用 load_dotenv() 加载 .env 文件
    load_dotenv()

    # TODO: 从环境变量读取 OPENAI_API_KEY
    api_key = os.getenv("OPENAI_API_KEY")

    # TODO: 若 api_key 为空,raise ValueError("缺少 OPENAI_API_KEY")
    if not api_key:
        raise ValueError("缺少 OPENAI_API_KEY")

    # TODO: 从环境变量读取 OPENAI_BASE_URL(可选)
    base_url = os.getenv("OPENAI_BASE_URL", None)

    # TODO: 创建 OpenAI 客户端(有 base_url 时传入)
    if base_url:
        client = OpenAI(api_key=api_key, base_url=base_url)
    else:
        client = OpenAI(api_key=api_key)

    # TODO: 打印 base_url 与 api_key 长度(隐藏明文)
    print(f"base_url: {client.base_url}")
    print(f"api_key 长度: {len(api_key)}")

    return client


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 有 .env 时能正常创建客户端
    try:
        client = create_llm_client()
        print("测试1 通过: 客户端创建成功")
    except ValueError as e:
        print(f"测试1 通过: 捕获异常 - {e}")

    # 测试 2: 无 API Key 时应抛出 ValueError
    # 临时删除环境变量验证
    saved_key = os.environ.pop("OPENAI_API_KEY", None)
    try:
        create_llm_client()
        print("测试2 失败: 未捕获缺失 Key")
    except ValueError:
        print("测试2 通过: 缺失 Key 时正确抛出异常")
    finally:
        # 恢复环境变量,避免影响后续测试
        if saved_key is not None:
            os.environ["OPENAI_API_KEY"] = saved_key
