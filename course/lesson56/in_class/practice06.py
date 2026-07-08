"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 教学红线 —— Docker 网络隔离]
[预计完成时间: 20 分钟]

场景: 实现 DockerCompose 类模拟 Docker 网络隔离。
services dict 存放服务,add_service 方法加入服务,
network 默认隔离,不同网络的服务无法互通。
红线: 演示 service A 无法访问 service B 时的正确做法 ——
用自定义 network 连接它们,验证显式加入同一网络后可达。
重点在于正确配置网络,而非触发错误。
注意: 本类仅做纯模拟,不调用任何 Docker 命令。

示例:
    >>> compose = DockerCompose()
    >>> compose.add_service("web")
    >>> compose.add_service("db")
    >>> assert compose.can_reach("web", "db") is False
    >>> compose.connect("web", "db")
    >>> assert compose.can_reach("web", "db") is True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class DockerCompose:
    """模拟 Docker Compose 网络拓扑(纯本地模拟)。"""

    def __init__(self):
        # 服务字典: {服务名: {"name": ..., "network": ...}}
        self.services = {}
        # 网络字典: {网络名: set(服务名, ...)}
        self.networks = {}

    def add_service(self, name: str, network: str = None):
        """添加服务,未指定网络则分配独立私有网络。"""
        pass

    def can_reach(self, name_a: str, name_b: str) -> bool:
        """判断两服务是否互通(是否在同一网络)。"""
        return False

    def connect(self, name_a: str, name_b: str, network: str = None):
        """正确做法: 将两服务连入同一自定义网络。"""
        pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认隔离,不同网络服务不可达
    compose = DockerCompose()
    compose.add_service("web")
    compose.add_service("db")
    assert compose.can_reach("web", "db") is False, (
        "未连接前 web 与 db 应不可达"
    )

    # 测试 2: 显式连接后可达
    compose.connect("web", "db")
    assert compose.can_reach("web", "db") is True, (
        "连接后 web 与 db 应可达"
    )

    # 测试 3: 指定共享网络,从开始就可达
    compose2 = DockerCompose()
    compose2.add_service("api", network="shared")
    compose2.add_service("cache", network="shared")
    assert compose2.can_reach("api", "cache") is True, (
        "同一共享网络应直接互通"
    )

    print("全部测试通过!")
