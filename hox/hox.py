from classes.Runtime import ClassCMD
from classes.FileManage import FileManageClass
import sys


def main() -> int:
    ClassCMD(
        prefix=sys.argv[1] if len(sys.argv) > 1 else '/',
        filemanage=FileManageClass(
            prefix=sys.argv[1] if len(sys.argv) > 1 else '/',
            core_commands=None
        ),
    ).Cmd()
    return 1


if __name__ == '__main__':
    main()
