# TODO: 0 == Unsuccessfully 1 = success 2 = error


class HelpClass:
    def __init__(self, prefix: str, filemanage) -> None:
        self.prefix: str = prefix
        self.fileHelp = filemanage(self.prefix).fileHelp

    def helpFunc(self, userprompt) -> int:
        promptSplit: any = userprompt.split()

        match len(promptSplit):
            case 1:
                print(f'''COMMANDS LIST
                    {self.prefix}h(help) <command> -> shows the current messages or displays help of a provided command
                    {self.prefix}f(file) <command> -> shows help for all the file commands or executes a given command
                        ''')
                return 1

            case 2:
                match promptSplit[1]:
                    case 'f' | 'file':
                        self.fileHelp()
                        return 1

                    case default:
                        print(f'unknown command {promptSplit[1]}')
                        return 2

            case default:
                return 2
