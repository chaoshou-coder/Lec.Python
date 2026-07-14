"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 综合 — 读 JSON → 处理 → 写回 + 异常处理]
[预计完成时间: 13 分钟]

题目描述:
  你有一个 "config.json" 文件,内容是一个字典,包含 "name"
  和 "version" 字段。请读取它,把 version 值加 1,然后写回
  文件。整个过程需要防护两种异常:文件不存在时创建默认
  配置,JSON 格式错误时提示并退出。

要求:
  - 文件不存在:用 {"name": "app", "version": 1} 创建
  - JSON 解码错误:捕获 json.JSONDecodeError,提示"JSON 损坏"
  - 正常情况:version += 1 后写回
  - 所有文件操作使用 with + encoding="utf-8"

示例:
    >>> 运行程序(文件不存在时)
    配置文件不存在,已创建默认配置
    {"name": "app", "version": 1}

    >>> 运行程序(文件内容是 {"name": "app", "version": 3} 时)
    版本已更新为 4
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import json, os
    tmp = "test_config.json"

    # 测试 1: 文件不存在 → 创建默认配置
    if os.path.exists(tmp):
        os.remove(tmp)
    # 模拟学员逻辑:不存在则创建
    if not os.path.exists(tmp):
        default = {"name": "app", "version": 1}
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=False)
    with open(tmp, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    assert cfg["version"] == 1, "默认 version 应为 1"

    # 测试 2: 正常读取 → version + 1 → 写回
    with open(tmp, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    cfg["version"] += 1
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False)
    with open(tmp, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    assert reloaded["version"] == 2, "version 应更新为 2"

    # 测试 3: JSON 损坏 → 捕获 JSONDecodeError
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("{bad json!!!")
    caught = False
    try:
        with open(tmp, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError:
        caught = True
    assert caught, "应捕获 JSONDecodeError"

    os.remove(tmp)
    print("practice06 测试通过 ✓")
