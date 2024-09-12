from utils.video_tool import *
from utils.helpers import calculate_runtime

""" common parameters """
input_path = r'./assets/video/inputs/'
input_nonstandard_path = r'./assets/video/inputs/nonstandard/'
output_horizontal_path = r'./assets/video/outputs/horizontal_screen/'
output_horizontal_to_vertical_path = r'./assets/video/outputs/horizontal_to_vertical_screen/'
output_vertical_path = r'./assets/video/outputs/vertical_screen/'
output_icon_path = r'./assets/video/outputs/icons/'
output_loop_path = r'./assets/video/outputs/loop/'

''' init global data '''
video_list = []


def check_folder_path():
    folder_paths = [input_path, input_nonstandard_path, output_horizontal_path, output_horizontal_to_vertical_path,
                    output_vertical_path, output_icon_path, output_loop_path]
    print(folder_paths)

    for folder_path in folder_paths:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            color_print(f'***** 文件夹 {folder_path} 已创建 ******', log.success)
        else:
            print(f'****** 文件夹 {folder_path} 已存在 ******', log.info)


def check_video():
    modify_video_extension(input_path, xr.video_extension)
    check_video_format(input_path, input_nonstandard_path)


def video_ready():
    global video_list

    for video in os.listdir(input_path):
        if os.path.isdir(os.path.join(input_path, video)):
            continue
        video_list.append(video)


def video_convert():
    global video_list
    horizontal_video = 0
    vertical_video = 0

    if len(video_list) == 0:
        return color_print('****** 没有要处理的视频，请检查 ******', log.warning)

    for video in video_list:
        source_video = VideoFileClip(input_path + video)
        video_name = os.path.splitext(video)[0]
        print(video_name)

        if source_video.size == list(xr.video_4k):
            output_horizontal_4k(source_video, output_horizontal_path + video_name + '_4k' + xr.video_extension)
            horizontal_video = horizontal_video + 1

            output_horizontal_to_vertical_1080p(source_video,
                                                output_horizontal_to_vertical_path + video_name + '_1080p' + xr.video_extension)
            vertical_video = vertical_video + 1

        if (source_video.size == list(xr.video_1080P)) or (source_video.size == list(xr.video_2160P)):
            output_vertical_1080p(source_video, output_vertical_path + video_name + '_1080p' + xr.video_extension)
            vertical_video = vertical_video + 1

        source_video.close()

    color_print(f'****** 共输出 {horizontal_video} 个横板视频和 {vertical_video} 个竖版视频 ******', log.success)


def video_to_icon():
    horizontal_icon = 0

    for video in os.listdir(output_horizontal_path):
        source_video = VideoFileClip(output_horizontal_path + video)
        output_horizontal_icon(source_video,
                               output_icon_path + os.path.splitext(video)[0] + '_icon' + xr.icon_extension[0])  # .png

        source_video.close()
        horizontal_icon = horizontal_icon + 1
    color_print(f'****** 成功导出 {horizontal_icon} 张基于横板视频的缩略图 ******', log.success)

    vertical_icon = 0
    for video in os.listdir(output_vertical_path):
        source_video = VideoFileClip(output_vertical_path + video)
        output_vertical_icon(source_video,
                             output_icon_path + os.path.splitext(video)[0] + '_icon' + xr.icon_extension[0])  # .png
        source_video.close()
        vertical_icon = vertical_icon + 1
    color_print(f'****** 成功导出 {vertical_icon} 张基于竖板视频的缩略图 ******', log.success)

    color_print(f'****** 共输出 {vertical_icon + vertical_icon} 张缩略图 ******', log.success)


def video_to_loop():
    video_loop_count = 0

    for video in os.listdir(output_loop_path):
        video_name = os.path.splitext(video)[0]
        source_video = VideoFileClip(output_loop_path + video)
        output_vertical_loop(source_video, output_loop_path + video_name + '_loop' + xr.video_extension)
        video_loop_count = video_loop_count + 1
        source_video.close()

    color_print(f'****** 共输出 {video_loop_count} 循环视频， ******', log.success)


''' test '''
# path = r'C:/Users/Admin/Desktop/nonstandard/'
# done = r'C:/Users/Admin/Desktop/done/'
# for video in os.listdir(path):
#     video_name = os.path.splitext(video)[0]
#     source_video = VideoFileClip(path + video)
#     video_clip = source_video.resize(xr.video_1080P)
#     print(video_name)
#     video_clip.write_videofile(done + video_name + '_1080' + xr.video_extension, fps=xr.fps, codec=xr.codec)
#     source_video.close()


@calculate_runtime
def main():
    check_folder_path()
    check_video()
    video_ready()
    video_convert()
    video_to_loop()
    video_to_icon()


if __name__ == '__main__':
    main()
