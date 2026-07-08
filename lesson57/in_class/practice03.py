"""
[难度: ⭐⭐]
[所属知识点: 结构化日志]
[预计完成时间: 10 分钟]

服务上线后,排错总靠 grep 文本,非常痛苦。
请用 python-json-logger 的 JsonFormatter 配置 logger,
每行日志包含 trace_id、level、message 字段。
调用后把日志写入字符串缓冲区,再用 json.loads 解析,
验证 trace_id 与 level 字段存在。

示例:
    >>> import io, logging
    >>> logger = setup_json_logger("demo")
    >>> logger.info("登录成功", extra={
    ...     "trace_id": "abc123"
    ... })
    >>> # 读取缓冲区并用 json.loads 解析
    >>> record = read_log_buffer(buf)
    >>> record["message"]
    '登录成功'
"""

from pythonjsonlogger import jsonlogger
import logging
import io

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

log_buffer = None


def setup_json_logger(name="app"):
    """配置并返回 JSON 格式日志 Logger。"""
    pass


def read_log_buffer():
    """读取并返回最后一行日志文本。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    import json

    # 测试 1: 日志为合法 JSON,含关键字段
    logger = setup_json_logger("test1")
    logger.info("用户登录",
                extra={"trace_id": "trace-001"})
    line = read_log_buffer()
    record = json.loads(line)
    assert record["message"] == "用户登录"
    assert record["trace_id"] == "trace-001"
    assert "level" in record
    print("测试 1 通过:", record)

    # 测试 2: warning 级别日志
    logger.warning("磁盘空间不足",
                   extra={"trace_id": "trace-002"})
    line2 = read_log_buffer()
    rec2 = json.loads(line2)
    assert rec2["level"] == "warning"
    print("测试 2 通过:", rec2)
