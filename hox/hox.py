import sys
from Classes.Runtime import ClassCMD

def main() -> int:
    ClassCMD(
        prefix=sys.argv[1] if len(sys.argv) > 1 else '/',
        logs=False,
    ).MainLoop()
    return 1

if __name__ == '__main__':
    main()
