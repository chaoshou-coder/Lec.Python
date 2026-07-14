"""
[难度: ⭐⭐⭐]
[所属知识点: find() + 切片]
[预计完成时间: 15 分钟]

题目描述:
    输入一个 URL(如 https://example.com/path),用 find 和切片
    分别提取协议、域名、路径,并打印结果。

示例:
    >>> url = "https://example.com/path/to/page"
    协议: https
    域名: example.com
    路径: /path/to/page
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
url = input("请输入 URL: ")
# 提取协议
protocol_end = url.find("://")
protocol = url[:protocol_end]
# 提取域名(从 :// 后到下一个 /)
host_start = protocol_end + 3
path_pos = url.find("/", host_start)
if path_pos == -1:
    host = url[host_start:]
    path = ""
else:
    host = url[host_start:path_pos]
    path = url[path_pos:]
print(f"协议: {protocol}")
print(f"域名: {host}")
print(f"路径: {path}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 带路径
    u1 = "https://example.com/path/to/page"
    print(f"测试1 URL: {u1}")

    # 测试 2: 不带路径
    u2 = "https://www.baidu.com"
    print(f"测试2 URL: {u2}")

    # 测试 3: http 协议
    u3 = "http://test.site/api/v1"
    print(f"测试3 URL: {u3}")
