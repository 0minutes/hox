import os
from Classes import handler


class ClassCMD:
    def __init__(self, prefix: str, filemanage) -> None:
        self.prefix: str = prefix
        self.file = filemanage

    def MainLoop(self) -> None:
        os.system('cls')
        while True:
            handler.Handler(self.prefix, input(f'<{self.prefix}> ')).matchCom()
