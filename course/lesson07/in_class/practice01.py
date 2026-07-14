"""
[难度: ⭐⭐]
[所属知识点: 鸭子类型多态]
[预计完成时间: 10 分钟]

题目描述:
    定义三个媒体类:`Audio`、`Video`、`Image`。
    它们**不需要继承同一个父类**,
    只需各自实现 `play()` 方法:
    - Audio 返回 "播放音频:XXX.mp3"
    - Video 返回 "播放视频:XXX.mp4"
    - Image 返回 "展示图片:XXX.png"

    定义函数 `play_media(media)`,
    调用 `media.play()`。

    循环列表 play_media,验证不同对象不同行为。

示例:
    >>> play_media(Audio("小苹果"))
    播放音频:小苹果.mp3
    >>> play_media(Video("流浪地球"))
    播放视频:流浪地球.mp4
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Audio:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

# class Video: ...
# class Image: ...
# def play_media(media): ...

# medias = [Audio("小苹果"), Video("流浪地球")]
# for m in medias:
#     print(play_media(m))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    assert play_media(Audio("小苹果")) == "播放音频:小苹果.mp3"
    assert play_media(Video("地球")) == "播放视频:地球.mp4"
    assert play_media(Image("风景")) == "展示图片:风景.png"

    # 混合列表
    medias = [Audio("A"), Video("B"), Image("C")]
    results = [play_media(m) for m in medias]
    assert len(results) == 3
    print("✅ 所有测试通过")
