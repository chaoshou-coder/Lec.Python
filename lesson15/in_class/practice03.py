"""
[难度: ⭐⭐⭐]
[所属知识点: os.mkdir() / os.rmdir()]
[预计完成时间: 15 分钟]

题目描述:
    请用 os.mkdir() 在当前目录下创建一个名为 'test_dir'
    的新文件夹;创建后用 os.path.exists() 检查是否存在;
    最后用 os.rmdir() 删除它,再次检查确认已删除。

示例:
    >>> import os
    >>> os.mkdir('test_dir')
    >>> os.path.exists('test_dir')
    True
    >>> os.rmdir('test_dir')
    >>> os.path.exists('test_dir')
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 创建目录后检查存在
    # 测试 2: 删除目录后检查不存在
    # 测试 3: 创建已存在的目录应报错
    pass
