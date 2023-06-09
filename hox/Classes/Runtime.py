import os
from Classes import handler


class ClassCMD:
    def __init__(self, prefix: str) -> None:
        self.prefix: str = prefix

    def MainLoop(self) -> None:
        os.system('cls')
        while True:
            handler.Handler(self.prefix, input(f'<{self.prefix}> ')).matchCom()
