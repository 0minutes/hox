import os
from Classes import help, FileManage
# TODO: 0 == Unsuccessfully 1 = success 2 = error


class Handler:
    def __init__(self, prefix: str, userprompt: str) -> None:
        self.prefix: str = prefix
        self.userprompt: str = userprompt

    def matchCom(self) -> int:
        promptSplit: list = self.userprompt.split()

        if self.userprompt.startswith(self.prefix):
            if promptSplit[0] == f'{self.prefix}quit' or promptSplit[0] == f'{self.prefix}q':
                return 2

            if promptSplit[0] == f'{self.prefix}help' or promptSplit[0] == f'{self.prefix}h':
                help.HelpClass(self.prefix, FileManage.FileManageClass).helpFunc(self.userprompt)
                return 1

            if promptSplit[0] == f'{self.prefix}file' or promptSplit[0] == f'{self.prefix}f':
                FileManage.FileManageClass(self.prefix).PromptCheck(self.userprompt)
                return 1

            else:
                print(f'Unknown command: {promptSplit[0]}')
                return 2

        else:
            os.system(self.userprompt)
            return 1
