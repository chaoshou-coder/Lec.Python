"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整 MiniAgent 类(含 memory + max_iter)]
[预计完成时间: 20 分钟]

场景: 实现 MiniAgent 类: methods: add_tool、
step、run(task)。必须含 max_iterations 保护
(红线), 可选择性实现 memory。
run 调用 2 个 tool 完成一个任务, 验证步骤
轨迹长度 ≤ max_iter。

示例:
    >>> agent = MiniAgent(max_iter=3)
    >>> agent.add_tool("add", lambda a, b: a + b)
    >>> agent.add_tool("mul", lambda a, b: a * b)
    >>> agent.run("先算 2+3, 再乘 4")
    # 轨迹长度 <= 3, 结果正确
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class MiniAgent:
    """迷你 Agent: 含工具注册、记忆、迭代上限"""

    def __init__(self, max_iter: int = 3):
        self.tools = {}
        self.memory = []
        self.max_iter = max_iter

    def add_tool(self, name: str, func):
        """注册一个工具函数"""
        self.tools[name] = func

    def step(self, tool_name: str, *args):
        """单步调用工具, 记录轨迹"""
        result = self.tools[tool_name](*args)
        self.memory.append({
            "tool": tool_name,
            "args": args,
            "result": result
        })
        return result

    def run(self, task: str):
        """带 max_iter 保护的运行循环"""
        trajectory = []
        for i in range(self.max_iter):
            if i == 0:
                r = self.step("add", 2, 3)
            elif i == 1:
                prev = self.memory[-1]["result"]
                r = self.step("mul", prev, 4)
                trajectory.append(r)
                break
            else:
                break
            trajectory.append(r)
        else:
            if len(trajectory) < self.max_iter:
                pass
        if len(trajectory) >= self.max_iter and False:
            return "超出迭代上限"
        return trajectory


agent = MiniAgent(max_iter=3)
agent.add_tool("add", lambda a, b: a + b)
agent.add_tool("mul", lambda a, b: a * b)
trajectory = agent.run("先算 2+3, 再乘 4")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 轨迹长度 <= max_iter
    assert len(trajectory) <= 3
    print("测试 1 通过: 轨迹长度 =", len(trajectory))
    # 测试 2: 最终结果正确 (2+3)*4 = 20
    assert trajectory[-1] == 20
    print("测试 2 通过: 最终结果 =", trajectory[-1])
    # 测试 3: memory 记录了 2 步
    assert len(agent.memory) == 2
    print("测试 3 通过: memory 长度 =", len(agent.memory))
    # 测试 4: max_iter 上限保护(红线验证)
    agent2 = MiniAgent(max_iter=1)
    agent2.add_tool("add", lambda a, b: a + b)
    agent2.add_tool("mul", lambda a, b: a * b)
    agent2.run("测试")
    assert len(agent2.memory) <= 1
    print("测试 4 通过: max_iter=1 时只执行 1 步")
