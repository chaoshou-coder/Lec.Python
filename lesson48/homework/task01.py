"""
[难度: ⭐⭐]
[所属知识点: REST API 分页请求]
[预计完成时间: 10 分钟]

题目描述:
调用 GitHub Search API 搜索 Python 仓库,按 stars 降序排列,
打印前 5 个仓库的 full_name 和 stargazers_count。
使用 params 字典传参(URL 查询字符串)。

请求地址: https://api.github.com/search/repositories
参数示例:
    params = {"q": "language:python", "sort": "stars",
              "order": "desc", "per_page": 5}
返回的 JSON 中,"items" 列表包含每个仓库的信息,
每个仓库的 "full_name" 和 "stargazers_count" 是所需字段。

示例:
    >>> results = search_top_python_repos()
    >>> # 输出(示例,实际数据随时间变化):
    >>> # 1. public-apis/public-apis - 200000 stars
    >>> # 2. xxx/yyy - 150000 stars
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 检查函数返回值为列表且长度为 5
    # result = search_top_python_repos()
    # assert isinstance(result, list) and len(result) == 5

    # 测试 2: 检查每个元素包含 full_name 和 stars 字段
    # for repo in result:
    #     assert "full_name" in repo and "stars" in repo

    pass
