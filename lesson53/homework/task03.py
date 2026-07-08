"""
[难度: ⭐⭐⭐⭐]
[所属知识点: ChromaDB 持久化 CRUD]
[预计完成时间: 20 分钟]

场景: 写完整的 ChromaDB 工作流:
创建集合,添加 5 条中文文档,查询、更新一条、删除一条,
并验证每一步通过。使用 chromadb.PersistentClient(path="./chroma_test")。

示例:
    >>> workflow()
    CRUD 全流程通过
"""

import os
import shutil

import chromadb
import numpy as np


DOCS = [
    ("1", "北京是中国的首都"),
    ("2", "上海是经济中心"),
    ("3", "广州是南方城市"),
    ("4", "深圳是科技之都"),
    ("5", "杭州有西湖美景"),
]


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def _fake_embed(text: str) -> list:
    """简易伪嵌入: 用字符 ascii 求和生成 4 维向量"""
    # TODO: 返回长度为 4 的 list[float]
    pass


def workflow():
    """完成创建、添加、查询、更新、删除全流程"""
    path = "./chroma_test"
    # 清理残留
    if os.path.exists(path):
        shutil.rmtree(path)

    # TODO: 创建 PersistentClient(path=path)
    # TODO: 创建集合 "docs"
    # TODO: 用 collection.add 添加 DOCS (带自构造 embedding)
    # TODO: 查询 query_texts=["首都"], n_results=1,应命中 id=1
    # TODO: 更新 id=1 的文档为 "北京是政治中心"
    # TODO: 删除 id=5
    # TODO: 用 collection.get 验证剩余 4 条
    # TODO: 打印并返回 "CRUD 全流程通过"
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    try:
        # 测试 1: 流程运行不报错
        result = workflow()
        assert result == "CRUD 全流程通过", "应返回成功字符串"
        print("测试 1 通过:", result)

        # 测试 2: 持久化目录已创建
        assert os.path.isdir("./chroma_test"), "持久化目录应存在"
        print("测试 2 通过: 持久化目录存在")
    finally:
        # 清理测试产物
        if os.path.exists("./chroma_test"):
            shutil.rmtree("./chroma_test")
