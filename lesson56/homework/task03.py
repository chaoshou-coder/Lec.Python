"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Docker 多服务编排]
[预计完成时间: 20 分钟]

题目描述:
实现 MiniCompose 类,生成 docker-compose.yml 字典结构,
支持 add_service(含 networks)、add_network、validate(
检查各服务网络合法)。
调用 2 服务 1 网络,验证 to_yaml 输出含 networks 块。
演示正确多服务网络配置(非红线错误用法)。

示例:
    >>> mc = MiniCompose()
    >>> mc.add_network("shared")
    >>> mc.add_service("web", "nginx", networks=["shared"])
    >>> mc.add_service("api", "python:3.11", networks=["shared"])
    >>> mc.validate()
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class MiniCompose:
    """模拟 docker-compose 多服务编排(stdlib 实现)"""

    def __init__(self):
        """初始化 compose 结构"""
        self.data = {
            "version": "3.8",
            "services": {},
            "networks": {},
        }

    def add_network(self, name: str):
        """添加网络"""
        pass

    def add_service(self, name: str, image: str,
                    networks=None):
        """添加服务(含 image 与 networks)"""
        pass

    def validate(self) -> bool:
        """检查所有服务引用的网络都已声明"""
        pass

    def to_yaml(self) -> str:
        """以纯文本模拟 YAML 输出(无第三方依赖)"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正确多服务网络配置
    mc = MiniCompose()
    mc.add_network("shared")
    mc.add_service("web", "nginx", networks=["shared"])
    mc.add_service("api", "python:3.11",
                   networks=["shared"])
    assert mc.validate() is True
    out = mc.to_yaml()
    assert "networks" in out
    print("测试 1 通过: 正确配置验证成功")
    print(out)

    # 测试 2: 引用未声明网络应验证失败
    mc2 = MiniCompose()
    mc2.add_service("web", "nginx",
                    networks=["missing"])
    assert mc2.validate() is False
    print("测试 2 通过: 非法网络验证失败")
