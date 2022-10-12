from src.packages.misc import datenow
from src.settings.Config import Config


class Cache:
    def __init__(self, name) -> None:
        """
        This function is a constructor for the class. It takes in a name and sets the name, content, and
        lastUpdate to None. It also sets the MAX_AGE to the value of the timer in the config file

        :param name: The name of the file
        """
        self.name = name
        self.content = None
        self.lasUpdate = None
        self.MAX_AGE = Config().getTimer() * 60000

    def fetchFromCache(self):
        """
        If the last update is not set, return false. Otherwise, return whether the current time is less
        than the last update plus the maximum age
        :return: The return value is a boolean.
        """
        if not self.lasUpdate:
            return False
        return datenow() < self.lasUpdate + self.MAX_AGE

    def get(self):
        """
        It returns the content of the object
        :return: The content of the file
        """
        return self.content

    def set(self, content):
        """
        It sets the content of the object to the content passed in, and sets the last update to the
        current date

        :param content: the content of the cache
        """
        self.content = content
        self.lasUpdate = datenow()

    def __repr__(self) -> str:
        return f"Cache({self.name})"
