from classes.Classes import CMD
from classes.FileManage import FileManage


def main() -> int:
    prefix = '/'
    CMD(
        file=FileManage(prefix=prefix),
        prefix=prefix
    ).Cmd()
    return 1


if __name__ == '__main__':
    main()
