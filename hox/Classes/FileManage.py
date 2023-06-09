import os
import shutil


class FileManageClass:
    def __init__(self, prefix) -> None:
        self.prefix: str = prefix
    
    def PromptCheck(self, userprompt) -> int:
        splitPrompt = userprompt.split()
        ifHelp = (splitPrompt[0] == f'{self.prefix}f' and len(splitPrompt) == 1 or splitPrompt[0] == f'{self.prefix}file' and len(splitPrompt) == 1)
        if ifHelp:
            self.fileHelp()
            return 1

        match splitPrompt[1]:
            case 'move' | 'mv':
                if len(splitPrompt) == 4:
                    self.moveFile(userprompt)
                    return 1

                elif len(splitPrompt) > 3:
                    print(f'Unknown argument {splitPrompt[-1]} for the directory in the file move branch')
                    return 2

                elif len(splitPrompt) < 4:
                    print(f'Not enough arguments to satisfy the function -> {self.prefix}f(file) mv(move) <file dir> '
                          f'<to dir>')
                    return 2

            case 'view' | 'v':
                if len(splitPrompt) == 3:
                    print(self.viewFile(userprompt))
                    return 1

                elif len(splitPrompt) < 3:
                    print(f'Not enough arguments to satisfy the function -> {self.prefix}f(file) v(view) <file dir>')
                    return 2

                elif len(splitPrompt) > 3:
                    print(f'Unknown argument {splitPrompt[-1]} for the directory in the file view branch')
                    return 2

            case 'copy' | 'c':
                if len(splitPrompt) < 4:
                    print(
                        f'Not enough arguments to satisfy the function -> {self.prefix}f(file) c(copy) <from file '
                        f'dir>'
                        f' <to file dir>')
                    return 2

                elif len(splitPrompt) == 4:
                    self.fileToFile(userprompt)
                    return 1

            case 'del' | 'dl':
                if len(splitPrompt) < 3:
                    print(f'Not enough arguments to satisfy the function -> {self.prefix}f(file) dl(del) <file dir>')
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
        {self.prefix}f(file) c(copy) <from file dir> <to file dir> -> copies a file to another
        {self.prefix}f(file) v(view) <file dir> -> allows you to view a file
        {self.prefix}f(file) mv(move) <from file dir> <to file dir> -> allows you to move a file
        {self.prefix}f(file) dl(del) <file dir> -> allows you to delete a file''')

        return 1

    @staticmethod
    def moveFile(args: str) -> int:
        args: list = args.split()
        src: str = args[2]
        dst: str = args[3]

        if not os.path.isabs(src):
            src = os.path.join(os.getcwd(), src)

        if not os.path.isabs(dst):
            dst = os.path.join(os.getcwd(), dst)

        try:
            dst_folder = os.path.dirname(dst)
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)

            shutil.move(src, dst)
            print('Successfully moved the file!')
            return 1

        except FileNotFoundError:
            print(f"File not found: {src}")
            return 2

        except PermissionError:
            print(f"Permission denied: {src} or {dst}")
            return 2

        except IsADirectoryError:
            print(f"Source is a directory: {src}")
            return 2

        except shutil.Error as e:
            print(f"Error occurred while moving the file: {e}")
            return 2

        except Exception as e:
            print(f"An unknown error occurred: {e}")
            return 2

    @staticmethod
    def fileToFile(args: str) -> int:
        args = args.split()

        try:
            with open(args[2], 'r') as initFile, open(args[3], 'w') as endFile:
                contents: str = initFile.read()
                endFile.write(contents)

            print('Successfully copied the file')
            return 1

        except FileNotFoundError:
            print(f"The file '{args[2]}' doesn't exist! Double-check the file path.")
            return 2

        except PermissionError:
            print(f"Permission denied. Unable to copy file '{args[2]}'.")
            return 2

        except IsADirectoryError:
            print(f"Cannot copy directory. Expected a file, but got '{args[2]}'.")
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
            return f"The file '{FilePathSplit[2]}' doesn't exist! Double-check the file path."

        except PermissionError:
            return f"Permission denied. Unable to view file '{FilePathSplit[2]}'."

        except IsADirectoryError:
            return f"'{FilePathSplit[2]}' is a directory, not a file."

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

        except IsADirectoryError:
            return f"'{FilePath[2]}' is a directory, not a file."

        except Exception as e:
            return f"An error occurred while deleting the file '{FilePath[2]}': {str(e)}"
