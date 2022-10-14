
import grequests

from src.packages.Cache import Cache
from src.packages.Abstract import AbstractProvider


class Falabella(AbstractProvider):
    def __init__(self) -> None:
        super().__init__()
        self.categorias = ["cat9360001", "cat16400010", "cat7090034", "cat16510006", "cat1008", "cat1005", "cat01", "cat2026", "CATG10005",
                           "CATG10005", "cat8620074", "CATG10006", "CATG10011", "cat6930002", "cat7330051", "cat13550007", "cat7450065", "cat2008", "cat7660002"]
        self.url = "https://www.falabella.com/s/browse/v1/listing/cl?channel=web&page=1&categoryId={0}&sortBy=derived.price.search%2Cdesc&f.range.derived.variant.discount=50%25+dcto+y+m%C3%A1s"

        self.name = "Falabella"
        self.cache = Cache(self.name)
        self.HEADERS = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "okhttp/4.9.1",
        }

    def genUrls(self) -> list:
        return [self.url.format(c) for c in self.categorias]

    def getData(self) -> list:
        rs = (grequests.get(u, headers=self.HEADERS) for u in self.genUrls())
        rq = grequests.map(rs)
        return [r.json()["data"]["results"][0]
                for r in rq if 'results' in r.json()["data"] and r.status_code == 200]

    def getOffers(self) -> list:
        if self.cache.fetchFromCache():
            return self.cache.get()
        offers = []
        for product in self.getData():
            offers.append(self.createOffer(self.name, product["displayName"], product["discountBadge"]
                                           ['label'][1:], product["prices"][0]["price"][0], product["url"], product["mediaUrls"]))

        self.cache.set(offers)

        return offers
