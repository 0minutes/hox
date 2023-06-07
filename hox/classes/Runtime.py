import os

class ClassCMD:
    def __init__(self, prefix: str, filemanage) -> None:
        self.prefix: str = prefix
        self.core_commands: list = [
            f'{self.prefix}help',
            f'{self.prefix}f',
        ]
        self.file = filemanage
        self.file.core_commands = self.core_commands

    def Handler(self, userprompt: str) -> int:
        if userprompt == f'{self.prefix}help':
            print(f'''COMMANDS LIST
                {self.prefix}help ->
                {self.prefix}f    -> shows help for all the file commands''')
            return 1

        if self.file.PromptCheck(userprompt) == 0:
            os.system(userprompt)

        return 1

    def Cmd(self) -> None:
        os.system('cls')
        while True:
            user_input = input(f'<{self.prefix}> ')
            self.Handler(user_input)
