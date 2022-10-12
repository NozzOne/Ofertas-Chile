from src.packages.misc import datenow
from src.settings.Config import Config

class Cache:
    def __init__(self, name) -> None:
        self.name = name
        self.content = None
        self.lasUpdate = None
        # la expiracion de ofertas es 1 minuto menos que el timer asi no hay delay
        self.MAX_AGE = (Config().getTimer() - 1) * 60000

    def fetchFromCache(self):
        if not self.lasUpdate:
            return False
        return datenow() < self.lasUpdate + self.MAX_AGE

    def get(self):
        return self.content

    def set(self, content):
        self.content = content
        self.lasUpdate = datenow()
