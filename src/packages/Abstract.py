from datetime import datetime

# "AbstractProvider is an abstract class that can't be instantiated and has methods that can't be
# called."
# 
# The first thing to notice is that the class is marked as abstract by inheriting from the ABC class
class AbstractProvider:
    def __init__(self) -> None:
        if self.__class__ is AbstractProvider:
            raise NotImplementedError("Abstract class can't be instantiated")

    def getData(self) -> list:
        """
        The function `getData()` returns a list of data
        """
        raise NotImplementedError("Abstract method can't be called")

    def getOffers(self) -> list:
        """
        It raises an error if the function is called.
        """
        raise NotImplementedError("Abstract method can't be called")

    def createOffer(self, provider, name: str, discount: str, price: str, url: str, mediaUrl: list) -> dict:
        """
        It creates a dictionary with the parameters passed to it
        
        :param provider: The name of the provider
        :param name: The name of the product
        :type name: str
        :param discount: The discount percentage
        :type discount: str
        :param price: str, url: str, mediaUrl: list
        :type price: str
        :param url: The URL of the product page
        :type url: str
        :param mediaUrl: list
        :type mediaUrl: list
        :return: A dictionary with the following keys: provider, name, discount, price, url, mediaUrl,
        fecha.
        """
        return {
            "provider": provider,
            "name": name,
            "discount": discount,
            "price": price,
            "url": url,
            "mediaUrl": mediaUrl,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    @property
    def _name(self):
        return self.name
