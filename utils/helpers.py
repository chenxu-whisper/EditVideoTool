import time
from utils.logger import *


def calculate_runtime(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        minutes = int(execution_time // 60)
        seconds = int(execution_time % 60)
        color_print(f'*** 所有视频转换成功，共用时{minutes}分{seconds}秒 ***', log.info)

    return wrapper


if __name__ == '__main__':
    pass
