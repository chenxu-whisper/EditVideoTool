import os
import sys
import shutil
from moviepy.editor import VideoFileClip
from utils.video_tool import check_video_encoding
from utils.logger import *
from xr_fomat import xr

BASE_DIR = os.path.dirname(sys.argv[0])


def video_check():
    video_list: list[str] = []
    error_set: set[str] = set()
    nonstandard_path = os.path.join(BASE_DIR, 'nonstandard')

    for file in os.listdir(BASE_DIR):
        if file.endswith('.mp4'):
            video_list.append(file)

    if len(video_list) != 0:
        for video in video_list:
            video_path = BASE_DIR + '\\' + video
            source_video = VideoFileClip(video_path)

            if source_video.size != list(xr.video_1080P):
                color_print(f'****** {source_video.filename}视频分辨率不合规， 此分辨率为：{source_video.size} ******',
                            log.warning)
                error_set.add(source_video.filename)

            if source_video.fps != xr.video_fps:
                color_print(f'****** {source_video.filename}视频帧率不合规， 此帧率为：{source_video.fps}fps ******', log.warning)
                error_set.add(source_video.filename)

            if check_video_encoding(video) != xr.video_codec:
                color_print(
                    f'****** {source_video.filename}视频编码不合规， 此编码为：{check_video_encoding(video)} ******',
                    log.warning)
                error_set.add(source_video.filename)

            source_video.close()
    else:
        color_print(f'****** {BASE_DIR}路径下中没有mp4视频 *******', log.info)
        return

    try:
        if len(error_set) != 0:
            if not os.path.exists(nonstandard_path):
                os.mkdir(nonstandard_path)
            for error in error_set:
                shutil.move(error, nonstandard_path)

            color_print(f'****** 有{len(error_set)}条视频编码不合规 ******', log.warning)
            color_print(f'****** 不合规的视频已移动至{nonstandard_path}文件夹中 ******', log.success)
        else:
            color_print(f'****** {BASE_DIR}路径下的视频均合规 ******', log.success)

    except FileNotFoundError as e:
        color_print(f'****** 未找到源文件或文件夹: {e} ******', log.error)
    except shutil.Error as e:
        color_print(f'****** 移动文件时出错: {e} ******', log.error)
    except Exception as e:
        color_print(f'****** 发生未知错误: {e} ******', log.error)


def run():
    video_check()


if __name__ == '__main__':
    run()


print('...................')
input("按回车键退出...")
