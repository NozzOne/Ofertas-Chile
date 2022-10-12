from src.packages.Falabella import Falabella
from src.packages.Paris import Paris
from src.settings.Config import Config


class Packages:
    def __init__(self) -> None:
        """
        It creates a new instance of the class Falabella and Paris, and then creates a dictionary with
        the keys 'falabella' and 'paris' and the values of the instances of the classes Falabella and
        Paris
        """
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
        """
        It returns the value of the variable _timerMiliseconds.
        :return: The miliseconds of the timer.
        """
        return self._timerMiliseconds

    @property
    def seconds(self):
        """
        It returns the value of the variable _timerSeconds.
        :return: The value of the _timerSeconds attribute.
        """
        return self._timerSeconds

    def getAll(self):
        """
        It returns a list of all the stores in the database
        :return: A list of the two objects.
        """
        return [self.falabella, self.paris]

    def getInstance(self, name):
        """
        It returns the attribute of the object that matches the name passed in

        :param name: The name of the instance to get
        :return: The instance of the class.
        """
        return getattr(self, name)
