""" Print color text """


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


class Log:
    success = 'green'
    error = 'red'
    warning = 'yellow'
    info = 'white'


text_color = TextColors()
log = Log()


def color_print(text:str, color:TextColors) -> None:
    if color == log.success:
        return print(TextColors.GREEN + text + text_color.WHITE)
    if color == log.warning:
        return print(TextColors.YELLOW + text + text_color.WHITE)
    if color == log.error:
        return print(TextColors.RED + text + text_color.WHITE)
    if color == log.info:
        return print(TextColors.WHITE + text + text_color.WHITE)
    if color == 'cyan':
        return print(TextColors.CYAN + text + text_color.WHITE)
    if color == 'blue':
        return print(TextColors.BLUE + text + text_color.WHITE)
    if color == 'magenta':
        return print(TextColors.MAGENTA + text + text_color.WHITE)


if __name__ == '__main__':
    pass
