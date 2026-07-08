"""
[难度: ⭐⭐]
[所属知识点: nginx 反向代理配置]
[预计完成时间: 10 分钟]

小王需要为后端 FastAPI 服务生成一份 nginx 反向代理配置。
请实现 nginx_conf 函数,返回一段 server 块文本:
监听 listen 80,proxy_pass 指向 http://127.0.0.1:8000,
并包含 proxy_set_header Host、X-Real-IP、X-Forwarded-For。
调用后用 "proxy_pass" 与端口验证字符串。

示例:
    >>> conf = nginx_conf("127.0.0.1", 8000)
    >>> "proxy_pass http://127.0.0.1:8000" in conf
    True
    >>> "X-Forwarded-For" in conf
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def nginx_conf(upstream_host="127.0.0.1",
               upstream_port=8000):
    """返回 nginx server 块配置文本。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    # 测试 1: 默认参数
    conf = nginx_conf()
    assert "listen 80" in conf
    assert "proxy_pass http://127.0.0.1:8000" in conf
    assert "Host" in conf
    print("测试 1 通过: 默认配置生成成功")

    # 测试 2: 自定义端口 9000
    conf2 = nginx_conf("127.0.0.1", 9000)
    assert "proxy_pass http://127.0.0.1:9000" in conf2
    assert ("X-Real-IP" in conf2
            and "X-Forwarded-For" in conf2)
    print("测试 2 通过: 自定义端口配置正确")
