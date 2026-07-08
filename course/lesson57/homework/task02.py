"""
[难度: ⭐⭐⭐]
[所属知识点: 云平台部署清单]
[预计完成时间: 15 分钟]

每次上线都要自检,防遗漏。请实现
deployment_checklist 函数,返回五项部署检查项列表,
每项形如 {"item":..., "status": False, "check":...},
并编写 verify(checklist) 函数,把 status=True
的项数作为"已通过数"返回。

示例:
    >>> cl = deployment_checklist()
    >>> len(cl)
    5
    >>> cl[0]["item"]
    '环境变量已配置'
    >>> verify(cl)
    0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def deployment_checklist():
    """返回五项部署检查项列表。"""
    pass


def verify(checklist):
    """统计已通过项数。"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================

if __name__ == '__main__':
    # 测试 1: 列表长度与字段
    cl = deployment_checklist()
    assert len(cl) == 5
    assert all("item" in c and "status" in c
               for c in cl)
    print("测试 1 通过: 清单结构正确")

    # 测试 2: 默认通过数为 0
    assert verify(cl) == 0
    # 手动勾选前两项
    cl[0]["status"] = True
    cl[1]["status"] = True
    assert verify(cl) == 2
    print("测试 2 通过: verify 计数正确")
