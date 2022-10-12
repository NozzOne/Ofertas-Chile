import os


class Config:
    def __init__(self) -> None:
        self.path = './data/config.ini'

    def existsFile(self) -> bool:
        return os.path.isfile(self.path)

    def checkFileConfig(self) -> None:
        if not self.existsFile():
            print("Archivo config.ini no encontrado, creando...")
            self.createFileConfig()

    def createFileConfig(self) -> None:
        with open(self.path, "w+") as file:
            file.write("[Settings]\n")
            file.write("Timer=5\n")
        print("Archivo config.ini creado con exito!")

    def getTimer(self) -> int:
        with open(self.path, "r") as file:
            for line in file:
                if line.startswith("Timer"):
                    return int(line.split("=")[1])
