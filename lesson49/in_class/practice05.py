"""
[难度: ⭐⭐⭐]
[所属知识点: ThreadPoolExecutor 线程池并发]
[预计完成时间: 15 分钟]

题目描述:
    用 ThreadPoolExecutor(max_workers=4) 并发请求
    httpbin.org/get?page=N(N=1,2,3,4),
    每个线程打印从响应 JSON 中取回的 "page" 参数值,
    主线程用 as_completed 等所有任务完成后打印"全部完成"。

示例:
    >>> 运行后终端输出(page 顺序可能乱序):
    请求 1 的 page 参数: 1
    请求 2 的 page 参数: 2
    请求 3 的 page 参数: 3
    请求 4 的 page 参数: 4
    全部完成
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证 ThreadPoolExecutor 模块可导入
    try:
        from concurrent.futures import (
            ThreadPoolExecutor, as_completed
        )
        import requests
        print("模块导入成功")
    except ImportError as e:
        print(f"导入失败: {e}")

    # 测试 2: 模拟线程池并发(用本地数据代替真实请求)
    print("--- 测试 2:并发执行 4 个任务 ---")

    def mock_fetch(page):
        """模拟请求返回 page 参数"""
        return page

    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {
            pool.submit(mock_fetch, i): i for i in range(1, 5)
        }
        for f in as_completed(futures):
            result = f.result()
            print(f"请求 {result} 的 page 参数: {result}")
            results.append(result)

    print("全部完成")
    assert len(results) == 4, f"应完成 4 个任务,实际 {len(results)}"
    assert set(results) == {1, 2, 3, 4}
    print("测试 2 通过:4 个任务全部完成")
