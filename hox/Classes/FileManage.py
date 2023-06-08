import os
from Classes import Runtime


class FileManageClass(Runtime.CmdCommands):
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def PromptCheck(self, userprompt) -> int:
        splitPrompt = userprompt.split()

        if not (userprompt.startswith(self.prefix) and splitPrompt[0] in self.core_commands):
            return 0

        if splitPrompt[0] == f'{self.prefix}f' and len(splitPrompt) == 1:
            self.fileHelp()
            return 1

        match splitPrompt[1]:
            case 'view':
                if len(splitPrompt) == 3:
                    print(self.viewFile(userprompt))
                    return 1

                elif len(splitPrompt) < 3:
                    print(f'Not enough arguments to satisfy the function -> {self.prefix}f view <file dir>')
                    return 2

                elif len(splitPrompt) > 3:
                    print(f'Unknown argument {splitPrompt[-1]} for the directory in the file view branch')
                    return 2

            case 'copy':
                if len(splitPrompt) < 4:
                    print(
                        f'Not enough arguments to satisfy the function -> {self.prefix}f copy <from file '
                        f'dir>'
                        f' <to file dir>')
                    return 2

                elif len(splitPrompt) == 4:
                    self.fileToFile(userprompt)
                    return 1

            case 'del':
                if len(splitPrompt) < 3:
                    print(f'Not enough arguments to satisfy the function -> {self.prefix}f del <file dir>')
                    return 2

                elif len(splitPrompt) == 3:
                    print(self.delFile(userprompt))
                    return 1

                elif len(splitPrompt) > 3:
                    print(f'Unknown arguments \'{splitPrompt[-1]}\' for the directory in the file del '
                          f'branch')
                    return 2

            case default:
                print(f'Unknown subcommand \'{userprompt.split()[1]}\' for the file management branch')
                return 2

        return 0

    def fileHelp(self) -> int:
        print(f'''FILE MANAGEMENT:
        {self.prefix}f copy <from file dir> <to file dir> -> copies a file to another
        {self.prefix}f view <file dir> -> allows you to view a file
        {self.prefix}f del <file dir> -> allows you to delete a file''')
        return 1

    def fileSort(self) -> None:
        # TODO: add file sorting
        pass

    @staticmethod
    def fileToFile(args: str) -> int:

        args = args.split()

        try:
            with open(args[2], 'r') as InitFile, open(args[3], 'w') as EndFile:
                contents: str = InitFile.read()
                EndFile.write(contents)
                print('Successfully copied the file')
                return 1

        except FileNotFoundError:
            print(f"The file direction '{args[2]}' doesn't exist! Double check it!")
            return 2

        except PermissionError:
            print(f"Permission denied. Unable to copy file '{args[2]}'.")
            return 2

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 2

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
