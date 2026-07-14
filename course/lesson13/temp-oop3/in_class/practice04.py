"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Plugin(abc.ABC) 插件系统]
[预计完成时间: 15 分钟]

题目描述:
    定义抽象类 `Plugin(abc.ABC)`,
    包含两个抽象方法:
    - `name()`:返回插件名字
    - `run(data)`:处理数据并返回结果

    定义两个子类:
    - `UpperPlugin`:run 返回 data.upper()
    - `ReversePlugin`:run 返回 data[::-1]

    定义函数 `run_plugins(plugins, data)`,
    循环调用每个插件的 run(),
    打印 "插件名: 结果"。

    体会:新增插件(如 `TrimPlugin`)时,
    只需添加一个类,**无需修改任何现有代码**。

示例:
    >>> plugins = [UpperPlugin(), ReversePlugin()]
    >>> run_plugins(plugins, "hello")
    upper: HELLO
    reverse: olleh
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Plugin(abc.ABC):
    # 请定义 name() 和 run(data) 抽象方法
    pass

class UpperPlugin(Plugin):
    pass

# class ReversePlugin(Plugin): ...
# def run_plugins(plugins, data): ...

# plugins = [UpperPlugin(), ReversePlugin()]
# run_plugins(plugins, "hello")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    plugins = [UpperPlugin(), ReversePlugin()]
    results = [(p.name(), p.run("hello")) for p in plugins]
    # UpperPlugin
    assert results[0] == ("upper", "HELLO")
    # ReversePlugin
    assert results[1] == ("reverse", "olleh")

    # 新增插件无需改 run_plugins
    class TrimPlugin(Plugin):
        def name(self): return "trim"
        def run(self, data): return data.strip()

    plugins2 = plugins + [TrimPlugin()]
    assert plugins2[2].run("  hi  ") == "hi"
    print("✅ 所有测试通过")
