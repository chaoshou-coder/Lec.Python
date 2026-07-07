"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 文档写作]
[预计完成时间: 45 分钟]

题目描述:
为图书管理系统编写 README.md,包含以下内容:
1. 功能介绍(系统能做什么)
2. 使用说明(如何安装、运行、使用各功能)
3. 类图(文字描述各类的职责和关系)
4. 示例代码(展示典型使用场景)
5. 已知限制或未来改进方向

要求:结构清晰,描述准确,示例可运行。

示例(文字类图):
    LibrarySystem
    ├── books: list[Book]
    ├── add_book(title, author)
    ├── remove_book(title)
    ├── borrow_book(title, borrower)
    ├── return_book(title)
    └── list_books()

    Book
    ├── title: str
    ├── author: str
    ├── is_borrowed: bool
    └── borrower: str | None
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 验证 README.md 是否存在且内容完整
    import os

    readme_path = "/Users/bang/Documents/learning/python/课件/重构计划/lesson21/homework/README.md"

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"README.md 存在,共 {len(content)} 字符")

        # 检查必要章节
        required = ["功能介绍", "使用说明", "类图", "示例"]
        for section in required:
            if section in content:
                print(f"✓ 包含章节: {section}")
            else:
                print(f"✗ 缺少章节: {section}")
    else:
        print("README.md 尚未创建,请完成 task02")
