from datetime import datetime

class AbstractProvider:
    def __init__(self) -> None:
        if self.__class__ is AbstractProvider:
            raise NotImplementedError("Abstract class can't be instantiated")

    def getData(self) -> list:
        raise NotImplementedError("Abstract method can't be called")

    def getOffers(self) -> list:
        raise NotImplementedError("Abstract method can't be called")

    def createOffer(self, provider, name: str, discount: str, price: str, url: str, mediaUrl: list) -> dict:
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
