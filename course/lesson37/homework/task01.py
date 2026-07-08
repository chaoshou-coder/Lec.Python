"""
[难度: ⭐⭐]
[所属知识点: snapshot_download]
[预计完成时间: 10 分钟]

使用 snapshot_download 下载 Qwen/Qwen2-0.5B-Instruct
仓库中所有 *.md 文件(README等),打印本地缓存路径。
注意:运行需联网。

示例:
    >>> main()
    下载完成,缓存路径: /Users/xxx/.cache/huggingface/...
"""

from huggingface_hub import snapshot_download

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def main():
    # 提示:使用 snapshot_download,传入 repo_id 与
    # allow_patterns=["*.md"],返回值为本地缓存路径
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 下载 *.md 并打印路径
    path = main()
    if path:
        print("测试1通过,路径长度:", len(path))

    # 测试 2: 列出下载的 .md 文件名
    # 提示:用 pathlib.Path(path).rglob("*.md")
    import glob
    from pathlib import Path
    if path:
        md_files = list(Path(path).rglob("*.md"))
        print("找到 md 文件数:", len(md_files))
        for f in md_files[:3]:
            print(" -", f.name)
    pass
