import sys
from Classes.Runtime import ClassCMD
from Classes.FileManage import FileManageClass


def main() -> int:
    ClassCMD(
        prefix=sys.argv[1] if len(sys.argv) > 1 else '/',
        filemanage=FileManageClass(
            sys.argv[1] if len(sys.argv) > 1 else '/',
        ),
    ).MainLoop()
    return 1


if __name__ == '__main__':
    main()
