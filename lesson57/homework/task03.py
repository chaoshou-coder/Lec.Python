"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整可观测性工具包]
[预计完成时间: 20 分钟]

一线排错需要日志、指标、健康检查三合一。
请实现 Observability 类:
- log_request(method, path, status, duration_ms)
- get_metrics() 返回 Prometheus 文本
- health() 返回 {"status": "ok"|"error"}

模拟三次请求后,验证:
1. counter http_requests_total 累加为 3
2. health() 在状态码均 <400 时返回 ok
3. 出现 500 时 health() 返回 error

示例:
    >>> obs = Observability()
    >>> obs.log_request("GET", "/", 200, 12)
    >>> obs.log_request("GET", "/", 200, 15)
    >>> obs.log_request("GET", "/", 200, 9)
    >>> "http_requests_total 3" in obs.get_metrics()
    True
    >>> obs.health()["status"]
    'ok'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

class Observability:
    """整合日志、指标、健康检查的可观测性工具包。"""

    def __init__(self):
        self.requests = []
        self.counter_total = 0

    def log_request(self, method, path,
                    status, duration_ms):
        """记录一次请求。"""
        pass

    def get_metrics(self):
        """返回 Prometheus 文本格式指标。"""
        pass

    def health(self):
        """基于最近请求返回健康状态。"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    obs = Observability()
    obs.log_request("GET", "/", 200, 12)
    obs.log_request("GET", "/", 200, 15)
    obs.log_request("GET", "/", 200, 9)
    # 测试 1
    assert "http_requests_total 3" in obs.get_metrics()
    print("测试 1 通过: counter 累计正确")

    # 测试 2
    assert obs.health()["status"] == "ok"
    print("测试 2 通过: health ok")

    # 测试 3
    obs.log_request("GET", "/fail", 500, 50)
    assert obs.health()["status"] == "error"
    print("测试 3 通过: health 异常检测正确")
