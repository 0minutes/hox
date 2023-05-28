import os


class CommandHandler:
    def __init__(self, prefix: str, functions) -> None:
        self.functions = functions
        self.prefix = prefix
        self.core_commands = [
            f'{self.prefix}help',

            f'{self.prefix}f',
        ]

    def Handler(self, prompt: str) -> int:

        splitPrompt = prompt.split()

        if prompt.startswith('/'):
            if splitPrompt[0] in self.core_commands:

                if splitPrompt[0] == f'{self.prefix}f':

                    if len(splitPrompt) == 1:
                        self.functions.file()
                        return 1

                    match splitPrompt[1]:
                        case 'view':
                            if len(splitPrompt) < 3:
                                print(f'Not enough arguments to satisfy the function -> {self.prefix}f view <file dir>')
                                return 0
                            elif len(splitPrompt) == 3:
                                print(self.functions.viewFile(prompt))
                                return 1

                            elif len(splitPrompt) > 3:
                                print(f'Unknown argument {splitPrompt[-1]} for the directory in the file view branch')
                                return 0

                        case 'copy':
                            if len(splitPrompt) < 4:
                                print(
                                    f'Not enough arguments to satisfy the function -> {self.prefix}f copy <from file '
                                    f'dir>'
                                    f'<to file dir>')
                                return 0

                            elif len(splitPrompt) == 4:
                                self.functions.fileToFile(prompt)
                                return 1

                        case 'del':
                            if len(splitPrompt) < 3:
                                print(f'Not enough arguments to satisfy the function -> {self.prefix}f del <file dir>')
                                return 0

                            elif len(splitPrompt) == 3:
                                print(self.functions.delFile(prompt))
                                return 1

                            elif len(splitPrompt) > 3:
                                print(f'Unknown arguments \'{splitPrompt[-1]}\' for the directory in the file del '
                                      f'branch')
                                return 0

                        case default:
                            print(f'Unknown subcommand \'{prompt.split()[1]}\' for the file management branch')
                            return 0

        os.system(prompt)
        return 1

    def Cmd(self) -> None:
        while True:
            prompt: str = input(f'<{self.prefix}> ')
            self.Handler(prompt)


class CommandFunctions:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix

    def help(self):
        print(f'''COMMANDS LIST
        {self.prefix}help ->
        {self.prefix}f    -> shows help for all the file commands''')

    def file(self) -> None:
        print(f'''FILE MANAGEMENT:
        {self.prefix}f copy <from file dir> <to file dir> -> copies a file to another
        {self.prefix}f view <file dir> -> allows you to view a file
        {self.prefix}f del <file dir> -> allows you to delete a file''')

    @staticmethod
    def fileToFile(args: str) -> int:

        args = args.split()

        if len(args) < 2:
            return 0

        with open(args[2], 'r') as InitFile, open(args[3], 'w') as EndFile:
            contents: str = InitFile.read()
            EndFile.write(contents)
            print('Successfully copied the file')
            return 1

    @staticmethod
    def viewFile(filepath: str) -> str:
        FilePathSplit = filepath.split()

        try:
            with open(FilePathSplit[2], 'r') as file:
                contents: str = file.read()
                return contents

        except FileNotFoundError:
            return f"The file direction '{FilePathSplit[2]}' doesn't exist! Double check it!"

        except PermissionError:
            return f"Permission denied. Unable to view file '{FilePathSplit[2]}'."

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    @staticmethod
    def delFile(filepath: str) -> str:
        FilePath = filepath.split()

        try:
            os.remove(FilePath[2])
            return f"File '{FilePath[2]}' deleted successfully."

        except FileNotFoundError:
            return f"File '{FilePath[2]}' does not exist."

        except PermissionError:
            return f"Permission denied. Unable to delete file '{FilePath[2]}'."

        except Exception as e:
            return f"An error occurred while deleting the file '{FilePath[2]}': {str(e)}"


def main() -> int:
    prefix = '/'
    CommandHandler(functions=CommandFunctions(prefix=prefix), prefix=prefix, ).Cmd()

    return 1


if __name__ == '__main__':
    main()
