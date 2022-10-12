from src.packages.Falabella import Falabella
from src.packages.Paris import Paris
from src.settings.Config import Config


class Packages:

    def __init__(self) -> None:
        self.falabella = Falabella()
        self.paris = Paris()
        self.providerNames = {
            'falabella': self.falabella,
            'paris': self.paris
        }
        self._timerMiliseconds = Config().getTimer() * 60000
        self._timerSeconds = Config().getTimer() * 60

    @property
    def miliseconds(self):
        return self._timerMiliseconds

    @property
    def seconds(self):
        return self._timerSeconds

    def getAll(self):
        return [self.falabella, self.paris]

    def getInstance(self, name):
        return getattr(self, name)
