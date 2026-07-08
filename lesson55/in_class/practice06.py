"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Agent max_iterations 安全限制]
[预计完成时间: 20 分钟]

场景: 实现安全 Agent 循环: 在 while 循环中
执行 agent step。教学红线 "Agent 无限循环
(没设 max_iterations)"——务必设置 max_iter = 3,
超出返回 "超出迭代上限"。

示例:
    >>> max_iter = 3
    >>> iteration = 0
    >>> while iteration < max_iter:
    ...     iteration += 1
    ...     # 执行一步 agent step
    ...     done = agent_step()
    ...     if done:
    ...         break
    >>> if iteration >= max_iter and not done:
    ...     print("超出迭代上限")
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def mock_agent_step(step: int) -> str:
    """模拟 agent 单步, 返回动作结果"""
    # 模拟一直不结束, 测试 max_iter 保护
    return "continue"


def safe_agent_loop(max_iter: int = 3) -> str:
    """带 max_iterations 保护的 Agent 循环"""
    iteration = 0
    done = False
    trajectory = []
    while iteration < max_iter:
        iteration += 1
        result = mock_agent_step(iteration)
        trajectory.append(f"第 {iteration} 步: {result}")
        if result == "final_answer":
            done = True
            break
    if not done:
        return "超出迭代上限"
    return "任务完成"


result = safe_agent_loop(max_iter=3)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 不终止时返回上限提示
    assert result == "超出迭代上限"
    print("测试 1 通过:", result)
    # 测试 2: 迭代次数未超过 max_iter
    r2 = safe_agent_loop(max_iter=1)
    assert r2 == "超出迭代上限"
    print("测试 2 通过: max_iter=1 也触发上限")
    # 测试 3: 正常结束场景
    def done_step(s):
        return "final_answer"

    it = 0
    done_flag = False
    while it < 3:
        it += 1
        if done_step(it) == "final_answer":
            done_flag = True
            break
    assert done_flag is True
    print("测试 3 通过: 正常结束不触发上限")
