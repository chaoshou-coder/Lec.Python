"""
[难度: ⭐⭐⭐⭐]
[所属知识点: find() 与切片]
[预计完成时间: 20 分钟]

题目描述:
  输入一个 URL,提取其中的协议部分和域名部分。
  例如:输入 "https://example.com/path",
  应提取协议 "https" 和域名 "example.com"。
  要求使用 find() 定位关键位置,再用切片提取。

示例:
    >>> "https://example.com/path" → 协议 "https",域名 "example.com"
    >>> "http://www.baidu.com" → 协议 "http",域名 "www.baidu.com"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
url = "https://example.com/path"
protocol_end = url.find(":")
protocol = url[:protocol_end]
domain_start = protocol_end + 3
domain_end = url.find("/", domain_start)
if domain_end == -1:
    domain = url[domain_start:]
else:
    domain = url[domain_start:domain_end]

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 带路径的 URL
    url_1 = "https://example.com/path"
    end_1 = url_1.find(":")
    proto_1 = url_1[:end_1]
    start_1 = end_1 + 3
    slash_1 = url_1.find("/", start_1)
    dom_1 = url_1[start_1:slash_1]
    print(f"协议: {proto_1},域名: {dom_1}")
    assert proto_1 == "https"
    assert dom_1 == "example.com"

    # 测试 2: 不带路径的 URL
    url_2 = "http://www.baidu.com"
    end_2 = url_2.find(":")
    proto_2 = url_2[:end_2]
    start_2 = end_2 + 3
    slash_2 = url_2.find("/", start_2)
    if slash_2 == -1:
        dom_2 = url_2[start_2:]
    else:
        dom_2 = url_2[start_2:slash_2]
    print(f"协议: {proto_2},域名: {dom_2}")
    assert proto_2 == "http"
    assert dom_2 == "www.baidu.com"

    # 测试 3: 带端口号的 URL
    url_3 = "https://localhost:8080/api"
    end_3 = url_3.find(":")
    proto_3 = url_3[:end_3]
    start_3 = end_3 + 3
    slash_3 = url_3.find("/", start_3)
    dom_3 = url_3[start_3:slash_3]
    print(f"协议: {proto_3},域名: {dom_3}")
    assert proto_3 == "https"
    assert dom_3 == "localhost:8080"

    print("所有测试通过!")
