import os


class Config:
    def __init__(self) -> None:
        """
        This function is used to initialize the path of the config file
        """
        self.path = './data/config.ini'

    def existsFile(self) -> bool:
        """
        It returns a boolean value that indicates whether the file exists or not
        :return: The return value is a boolean value.
        """
        return os.path.isfile(self.path)

    def checkFileConfig(self) -> None:
        """
        If the file doesn't exist, create it
        """
        if not self.existsFile():
            print("Archivo config.ini no encontrado, creando...")
            self.createFileConfig()

    def createFileConfig(self) -> None:
        """
        It creates a file called config.ini and writes two lines to it
        """
        with open(self.path, "w+") as file:
            file.write("[Settings]\n")
            file.write("Timer=5\n")
        print("Archivo config.ini creado con exito!")

    def getTimer(self) -> int:
        """
        It opens the file, reads each line, and if the line starts with "Timer", it returns the integer
        value of the line after the "=" sign
        :return: The timer value.
        """
        with open(self.path, "r") as file:
            for line in file:
                if line.startswith("Timer"):
                    return int(line.split("=")[1])
