import shutil
import cv2
from moviepy.editor import *
from utils.logger import *
from xr_fomat import *


def check_video_encoding(video_path:str) -> str|None:
    video = cv2.VideoCapture(video_path)
    if video.isOpened():
        fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
        encoding = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
        return encoding
    else:
        return None


def modify_video_extension(video_path:str, file_extension:str) ->None:
    for video in os.listdir(video_path):
        if os.path.isdir(os.path.join(video_path, video)):
            continue

        if not video.endswith(file_extension):
            change_extension = os.path.splitext(video)[0] + file_extension
            os.rename(os.path.join(video_path, video), os.path.join(video_path, change_extension))

    log_success('****** 视频拓展名已转成mp4格式 ******')


def check_horizontal_videos(video_path:str) ->None:
    for video in os.listdir(video_path):
        if os.path.isdir(os.path.join(video_path, video)):
            continue

        source_video = VideoFileClip(video_path + video)

        if source_video.size != list(xr.video_4k):
            log_warning(f'****** {source_video.filename} 视频分辨率不是4k，此分辨率为：{source_video.size} ******')
            source_video.close()


def check_vertical_videos(video_path:str) ->None:
    for video in os.listdir(video_path):
        if os.path.isdir(os.path.join(video_path, video)):
            continue

        source_video = VideoFileClip(video_path + video)

        if (source_video.size != list(xr.video_1080P)) and (source_video.size != list(xr.video_2160P)):
            log_warning(f'****** {source_video.filename} 视频宽长比不是9:16， 此分辨率为：{source_video.size} ******')
            source_video.close()


def check_video_format(video_path:str, error_path:str) ->None:
    error_list = []

    for video in os.listdir(video_path):
        if os.path.isdir(os.path.join(video_path, video)):
            continue

        source_video = VideoFileClip(video_path + video)

        # if source_video.size != list(xr.video_1080P):
        if source_video.size != list(xr.video_4k) and source_video.size != list(
                xr.video_1080P) and source_video.size != list(xr.video_2160P):
            log_warning(f'****** {source_video.filename} 视频分辨率不合规， 此分辨率为：{source_video.size} ******')
            error_list.append(video)

        source_video.close()

    try:
        if error_list != 0:
            for error in error_list:
                shutil.move(os.path.join(video_path, error), os.path.join(error_path, error))

        log_warning(f'****** 有 {len(error_list)} 条视频不合规 ******')
        log_success(f'****** 不合规的视频已移动至{error_path}文件夹中 ******')

    except FileNotFoundError as e:
        log_error(f'****** 未找到源文件或文件夹: {e} ******')
    except shutil.Error as e:
        log_error(f'****** 移动文件时出错: {e} ******')
    except Exception as e:
        log_error(f'****** 发生未知错误: {e} ******')


''' convert video '''


def output_horizontal_4k(video_clip:VideoFileClip, clip_path:str) ->None:
    video_clip = video_clip.resize(xr.video_4k)
    video_clip.write_videofile(clip_path, fps=xr.video_fps, codec=xr.video_codec)


def output_horizontal_to_vertical_1080p(video_clip:VideoFileClip, clip_path: str) ->None:
    video_clip = video_clip.crop(xr.crop_vertical_middle[0], xr.crop_vertical_middle[1],
                                 xr.crop_vertical_middle[2], xr.crop_vertical_middle[3])
    video_clip.write_videofile(clip_path, fps=xr.video_fps, codec=xr.video_codec)


def output_vertical_1080p(video_clip:VideoFileClip, clip_path:str) ->None:
    video_clip = video_clip.resize(xr.video_1080P)
    video_clip.write_videofile(clip_path, fps=xr.video_fps, codec=xr.video_codec)


def output_horizontal_icon(video_clip:VideoFileClip, clip_path:str) ->None:
    frame = video_clip.get_frame(1)
    video_clip.close()
    icon = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(clip_path, icon)


def output_vertical_icon(video_clip:VideoFileClip, clip_path:str) ->None:
    video_clip = video_clip.resize(0.15)
    frame = video_clip.get_frame(1)
    video_clip.close()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    icon = frame[110:200, 10:147]  # y、x  hard code
    cv2.imwrite(clip_path, icon)


def output_vertical_loop(video_clip:VideoFileClip, clip_path:str) ->None:
    video_clip = video_clip.resize(xr.video_1080P)
    video_clip = vfx.time_symmetrize(video_clip)
    video_clip = video_clip.subclip(0, video_clip.duration - 1 / xr.video_fps)
    video_clip.write_videofile(clip_path, fps=xr.video_fps, codec=xr.video_codec)


def output_gif(video_clip:VideoFileClip, clip_path:str) ->None:
    video_clip = video_clip.resize(xr.icon_resolution)
    video_clip.write_gif(clip_path, program='ffmpeg')


if __name__ == '__main__':
    pass