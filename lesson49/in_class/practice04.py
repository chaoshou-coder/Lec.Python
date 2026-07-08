"""
[难度: ⭐⭐]
[所属知识点: asyncio + aiohttp 异步请求]
[预计完成时间: 10 分钟]

题目描述:
使用 asyncio + aiohttp 同时请求 httpbin.org/get 共 3 次,
每次请求携带不同的查询参数(如 page=1/2/3),
使用 asyncio.gather 并发执行所有请求,
打印每个响应中取得的原请求 URL。

示例:
    >>> 运行后终端输出:
    请求 1 的响应 URL: https://httpbin.org/get?page=1
    请求 2 的响应 URL: https://httpbin.org/get?page=2
    请求 3 的响应 URL: https://httpbin.org/get?page=3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 import 导入所需模块
    try:
        import asyncio
        import aiohttp
        print("模块导入成功: asyncio, aiohttp")
    except ImportError as e:
        print(f"导入失败: {e}")

    # 测试 2: 检查 aiohttp 可用(模拟会话创建)
    async def check_aiohttp():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://httpbin.org/get?test=1"
                ) as resp:
                    data = await resp.json()
                    assert "url" in data, "响应缺少 url 字段"
                    print(f"aiohttp 测试请求成功, URL: {data['url']}")
        except Exception as e:
            print(f"aiohttp 请求失败: {e}")

    asyncio.run(check_aiohttp())
