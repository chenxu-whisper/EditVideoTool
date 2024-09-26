""" Print color text """
__all__ = ['log_success',
           'log_info',
           'log_warning',
           'log_error']

class TextColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log_success(text: str) -> None:
    return print(TextColors.GREEN + text)


def log_info(text: str) -> None:
    return print(TextColors.WHITE + text)


def log_error(text: str) -> None:
    return print(TextColors.RED + text)


def log_warning(text: str) -> None:
    return print(TextColors.YELLOW + text)


if __name__ == '__main__':
    pass
