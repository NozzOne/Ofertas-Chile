import grequests
import requests
import locale
import re

from bs4 import BeautifulSoup

from src.packages.Cache import Cache
from src.packages.Abstract import AbstractProvider


class Abcdin(AbstractProvider):
    locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

    def __init__(self) -> None:
        super().__init__()
        self.name = "Abcdin"
        self.cache = Cache(self.name)

        self.url = "https://www.abcdin.cl/ofertas?p={0}&product_list_limit=36"
        self.HEADERS = {
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.3",
        }
        self.totalPages = self.getTotalPAges()

    def getTotalPAges(self) -> int:
        # limit items per page 36
        r = requests.get(self.url.format(1), headers=self.HEADERS).text
        # total items
        items = re.search(
            r'<span class="toolbar-number">(\d+)</span>', r).group(1)
        return int(items) // 36 + 1

    def genUrls(self) -> list:
        return [self.url.format(i) for i in range(1, self.totalPages+1)]

    def getData(self) -> list:
        rs = (grequests.get(u, headers=self.HEADERS) for u in self.genUrls())
        return grequests.map(rs)

    def getOffers(self) -> list:
        if self.cache.fetchFromCache():
            return self.cache.get()
        offers = []
        try:
            for r in self.getData():
                soup = BeautifulSoup(r.text, "lxml")
                for product in soup.find_all("div", class_="product-item-info"):
                    discount = product.find(
                        "div", class_="amasty-label-text").text.strip()[1:]
                    info = product.find("a", class_="product-item-link")
                    url = info['href']
                    name = info.text.strip()
                    price = product.find(
                        "span", class_="price").text.strip()[1:]
                    # normalPrice = product.find("span", class_="price-wrapper").text.strip()[1:]
                    mediaUrl = product.find(
                        "img", class_="product-image-photo")['src']
                    offers.append(self.createOffer(
                        self.name, name, discount, price, url, mediaUrl))
        except Exception as e:
            pass
        self.cache.set(offers)
        return offers
