# 教学计划变更日志(无 git,原始做法:时间戳目录 + 本文档)

## v1.0.0 (2026-07-07)

### 产物
- 21 天教学计划(21 个 lesson 目录)
- 178 道习题(当堂练 120 + 课后作业 58)
- 3 个中型项目(购物车/图书 v1/图书 v2 OOP)
- Day01-Day7 全套 README
- Day08-Day21 slides.md(含主题标题)
- references.md 素材库(14 门课程/100+ 习题/25 项红线)

### 验收
- 21 个 README 实际内容(非占位模板)
- 178 道题 .py 文件全部写入
- 3 个 weekly_projects README 写入
- references.md 落盘(328 行 / 20 KB)

### 版本位置
- 完整备份:`.versions/lessons-v1-20260707-152921/`

---

## v1.1.0 (待定 — 迭代方案详见 iteration-v2-plan.md)

### 计划变更
- (+7 道题)补充装饰器/生成器/正则/日志/ABC 缺口
- (+178 test_NN.py)引入 MIT/Harvard 风格的自动评测脚本
- (调整)阶段复习日从 Day18 后移至 Day19,OOP 部分多 0.5 天

### 验收标准
- 178 个 `test_NN.py` 全部通过 `pytest -q`
- 7 道新题写入对应 lesson
- CHANGELOG.md 已更新 v1.1.0
- `.versions/lessons-v2-<时间戳>/` 已创建
