import time
from utils.logger import log_info


def calculate_runtime(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        minutes = int(execution_time // 60)
        seconds = int(execution_time % 60)
        log_info(f'*** 共用时{minutes}分{seconds}秒 ***')

    return wrapper


def get_time() -> None:
    print(time.strftime('%x (%d/%m/%y)')) # 09/23/24 (23/09/24)


if __name__ == '__main__':
    pass
