"""
[难度: ⭐⭐⭐]
[所属知识点: __len__ + __iter__ 协议]
[预计完成时间: 12 分钟]

题目描述:
    定义 `Playlist` 类,表示播放列表。
    同时实现 `__len__` 和 `__iter__`:
    - `__len__`:返回歌曲数,支持 `len(playlist)`
    - `__iter__`:支持 `for song in playlist`

    **注意**:只有 `__len__` 不够!
    `for` 循环需要 `__iter__`。

    定义函数 `count_long_songs(playlist, min_len)`,
    返回时长超过 min_len 的歌曲数。

示例:
    >>> playlist = Playlist(
    ...     [("晴天", 280), ("稻香", 220)]
    ... )
    >>> print(len(playlist))
    2
    >>> for song in playlist:
    ...     print(song)
    ('晴天', 280)
    ('稻香', 220)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Playlist:
    def __init__(self, songs):
        self.songs = songs  # 每个元素是 (歌名, 时长)

    def __len__(self):
        pass

    def __iter__(self):
        pass

# def count_long_songs(playlist, min_len): ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    pl = Playlist([("晴天", 280), ("稻香", 220)])

    # __len__ 测试
    assert len(pl) == 2

    # __iter__ 测试
    songs = [s for s in pl]
    assert len(songs) == 2
    assert songs[0][0] == "晴天"

    # 边界:空播放列表
    empty = Playlist([])
    assert len(empty) == 0
    assert list(empty) == []

    print("✅ 所有测试通过")
