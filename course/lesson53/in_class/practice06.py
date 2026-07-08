"""
[难度: ⭐⭐⭐⭐]
[所属知识点: ChromaDB 集合创建 + 添加文档 + 查询]
[预计完成时间: 20 分钟]

场景: 用 chromadb.PersistentClient 创建名为 demo 的集合,
添加 3 条文档(手动提供 embedding),
query_texts=["苹果"], n_results=1 返回距离最近的文档名。

示例:
    >>> run_demo()
    最近文档: 苹果是一种水果
"""

import chromadb
import numpy as np


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def run_demo():
    """创建集合并完成添加与最近邻查询"""
    # TODO: 创建 PersistentClient(临时路径)
    # TODO: 创建名为 "demo" 的集合
    # TODO: 准备 3 条文档、id 与手动 embedding
    # TODO: 用 collection.add 添加
    # TODO: 用 collection.query 查询 "苹果",n_results=1
    # TODO: 打印并返回最近文档内容
    pass


def _embed(text: str) -> list:
    """简易嵌入函数: 用字符 unicode 求和做伪向量(仅演示)"""
    # TODO: 返回一个长度为 4 的 list[float],
    #       例如: sum(ord(c) for c in text) 拆分到 4 维
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import shutil, os

    # 清理可能残留的测试目录
    for p in ["_chroma_demo"]:
        if os.path.exists(p):
            shutil.rmtree(p)

    # 测试 1: 运行不报错,返回文档字符串
    result = run_demo()
    assert isinstance(result, str), "应返回字符串文档内容"
    print("测试 1 通过: 返回文档 =", result)

    # 清理测试产物
    if os.path.exists("_chroma_demo"):
        shutil.rmtree("_chroma_demo")
