from classes.Classes import CMD
from classes.Classes import CommandFunctions


def main() -> int:
    prefix = '/'
    CMD(
        functions=CommandFunctions(prefix=prefix),
        prefix=prefix
    ).Cmd()
    return 1


if __name__ == '__main__':
    main()
