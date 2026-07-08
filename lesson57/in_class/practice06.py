"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Prometheus 风格指标]
[预计完成时间: 20 分钟]

Prometheus 通过拉取文本接口采集指标。请实现
Metrics 类,内部维护 counter 与 histogram 数据,
并编写 expose 方法,返回合法的 Prometheus
exposure 文本格式,包含:
- http_requests_total 2
- request_duration_seconds_bucket{le="0.1"} 1

示例:
    >>> m = Metrics()
    m.counter("http_requests", "/")
    m.counter("http_requests", "/")
    m.histogram("request_duration_seconds", 0.05)
    out = m.expose()
    >>> "http_requests_total 2" in out
    True
    >>> 'le="0.1"' in out
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

class Metrics:
    """简易 Prometheus 指标收集器。"""

    def __init__(self):
        self.counters = {}
        self.histograms = {}

    def counter(self, name, label=""):
        """计数加一。"""
        pass

    def histogram(self, name, value,
                  buckets=(0.05, 0.1, 0.5, 1.0)):
        """记录一段耗时值。"""
        pass

    def expose(self):
        """返回 Prometheus 文本格式。"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    m = Metrics()
    m.counter("http_requests", "/")
    m.counter("http_requests", "/")
    m.histogram("request_duration_seconds", 0.05)
    out = m.expose()
    assert "http_requests_total 2" in out
    assert (
        'request_duration_seconds_bucket{le="0.1"} 1'
        in out
    )
    print("测试 1 通过:\n", out)

    m.histogram("request_duration_seconds", 0.2)
    out2 = m.expose()
    assert out2.count("request_duration_seconds_count") >= 1
    print("测试 2 通过: histogram 累计 count 正确")
