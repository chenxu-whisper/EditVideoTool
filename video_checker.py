import logging
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
                log_warning(f'****** {source_video.filename}视频分辨率不合规， 此分辨率为：{source_video.size} ******')
                error_set.add(source_video.filename)

            if source_video.fps != xr.video_fps:
                log_warning(f'****** {source_video.filename}视频帧率不合规， 此帧率为：{source_video.fps}fps ******')
                error_set.add(source_video.filename)

            if check_video_encoding(video) != xr.video_codec:
                log_warning(
                    f'****** {source_video.filename}视频编码不合规， 此编码为：{check_video_encoding(video)} ******')
                error_set.add(source_video.filename)

            source_video.close()
    else:
        log_info(f'****** {BASE_DIR}路径下中没有mp4视频 *******')
        return

    try:
        if len(error_set) != 0:
            if not os.path.exists(nonstandard_path):
                os.mkdir(nonstandard_path)
            for error in error_set:
                shutil.move(error, nonstandard_path)

            log_warning(f'****** 有{len(error_set)}条视频编码不合规 ******')
            log_success(f'****** 不合规的视频已移动至{nonstandard_path}文件夹中 ******')
        else:
            log_success(f'****** {BASE_DIR}路径下的视频均合规 ******')

    except FileNotFoundError as e:
        log_error(f'****** 未找到源文件或文件夹: {e} ******')
    except shutil.Error as e:
        log_error(f'****** 移动文件时出错: {e} ******')
    except Exception as e:
        log_error(f'****** 发生未知错误: {e} ******')


def main():
    video_check()


if __name__ == '__main__':
    main()

print('...................')
input("按回车键退出...")
