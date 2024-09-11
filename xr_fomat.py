""" key parameters """


class XR:
    # video
    video_1080P = (1080, 1920)  # 9:16
    video_2160P = (2160, 3840)  # 9:16
    video_4k = (3840, 2160)  # 16:9
    video_resolution = [video_1080P, video_2160P, video_4k]
    video_fps = 30
    video_extension = '.mp4'
    video_codec = 'h264'  # h.264
    crop_vertical_left = (0, 0, 1080, 1920)  # 1080p the left side of the video
    crop_vertical_middle = (1380, 0, 2460, 1920)  # 1080p the middle side of the video
    crop_vertical_right = (2760, 0, 3840, 1920)  # 1080p the right side of the video

    # icon
    icon_resolution = (137, 90)
    icon_png = ('.png', '.jpg')
    icon_extension = ('.png', '.jpg')

    # frame
    frame_1080P = (1080, 1920)  # 9:16
    frame_2160P = (2160, 3840)  # 9:16
    frame_resolution = [frame_1080P, frame_2160P]
    frame_depth = "uint8"  # opencv  8bit

    # sequence
    sequence_resolution = (1080, 1920)
    sequence_fps = 24


xr = XR()


if __name__ == '__main__':
    pass
