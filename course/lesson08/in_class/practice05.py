"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Playlist 类完整实现]
[预计完成时间: 15 分钟]

题目描述:
    完善 `Playlist` 类,要求同时支持:
    - `len(playlist)` —— 返回歌曲数
    - `for song in playlist` —— 遍历
    - `playlist[i]` —— 索引取某首歌(`__getitem__`)
    - `playlist + playlist` —— 合并两列表(`__add__`)

    每首歌是一个字符串(歌名)。

示例:
    >>> p1 = Playlist(["晴天", "稻香"])
    >>> p2 = Playlist(["七里香"])
    >>> print(len(p1))        # 2
    >>> print(p1[0])          # 晴天
    >>> p3 = p1 + p2
    >>> print(len(p3))        # 3
    >>> for s in p3: print(s)
    晴天
    稻香
    七里香
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    # 请补全 __len__ / __iter__ / __getitem__ / __add__
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Playlist(["晴天", "稻香"])
    p2 = Playlist(["七里香"])

    # __len__
    assert len(p1) == 2

    # __iter__
    assert [s for s in p1] == ["晴天", "稻香"]

    # __getitem__
    assert p1[0] == "晴天"
    assert p1[1] == "稻香"

    # __add__
    p3 = p1 + p2
    assert len(p3) == 3
    assert p1[0] == "晴天"  # p1 未修改
    print("✅ 所有测试通过")
