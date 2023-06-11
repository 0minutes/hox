import os
import datetime
from Classes import handler


class ClassCMD:
    def __init__(self, prefix: str, logs: bool) -> None:
        self.prefix: str = prefix
        self.logFolder: str = os.getcwd() + '\logs'
        self.logFile = None
        self.logs: bool = logs
        self.CurrentDir: str = os.getcwd()

    def createLogFile(self) -> int:
        if self.logs:
            
            os.makedirs(self.logFolder, exist_ok=True)

            time_str = datetime.datetime.now().strftime('%H-%M-%S')
            log_File = os.path.join(self.logFolder, f'logs-{time_str}.txt')
            with open(log_File, 'w'):
                pass
            self.logFile = log_File
            return log_File


    def writeLogs(self, prompt: str) -> int:
        if self.logFile == None:
            logFile = self.createLogFile()
            with open(logFile, 'a') as file:
                file.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}]: {prompt}\n')
        
        else:
            with open(self.logFile, 'a') as file:
                file.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}]: {prompt}\n')

        return 0

    def MainLoop(self) -> int:
        os.system('cls')
        if self.logs == True:
            while True:
                prompt = input(f'<{self.prefix}> ')
                self.writeLogs(prompt=prompt)
                if (handler.Handler(self.prefix, input(f'<{self.prefix}> ')).matchCom()) == 2: return 0

        while True:
            if (handler.Handler(self.prefix, input(f'<{self.prefix}> ')).matchCom()) == 2: return 0
