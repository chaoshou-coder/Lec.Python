"""
[难度: ⭐⭐]
[所属知识点: 健康检查端点]
[预计完成时间: 10 分钟]

运维要求服务暴露 /healthz,返回整体健康摘要。
请实现 health_check 函数,接收各子服务状态 dict,
例如 {"db_ok": True, "cache_ok": True}。
若全部正常,返回 {"status": "ok", "detail": {...}};
任意一项为 False,status 置 "error",并保留 detail。

示例:
    >>> health_check({"db_ok": True, "cache_ok": True})
    {'status': 'ok', 'detail': {'db_ok': True,
     'cache_ok': True}}
    >>> health_check({"db_ok": False})
    {'status': 'error', 'detail': {'db_ok': False}}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def health_check(services):
    """根据各子服务状态返回整体健康摘要。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    # 测试 1: 全部正常
    r1 = health_check({"db_ok": True, "cache_ok": True})
    assert r1["status"] == "ok"
    assert r1["detail"]["db_ok"] is True
    print("测试 1 通过:", r1)

    # 测试 2: db 异常
    r2 = health_check({"db_ok": False,
                       "cache_ok": True})
    assert r2["status"] == "error"
    print("测试 2 通过:", r2)

    # 测试 3: 全空视为 ok
    r3 = health_check({})
    assert r3["status"] == "ok"
    print("测试 3 通过:", r3)
