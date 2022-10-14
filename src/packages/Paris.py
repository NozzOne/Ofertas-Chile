import grequests
import locale

from src.packages.Cache import Cache
from src.packages.Abstract import AbstractProvider



class Paris(AbstractProvider):
    locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')
    def __init__(self) -> None:
        super().__init__()
        self.name = "Paris"
        self.cache = Cache(self.name)
        self.categorias = ["electro", "tecnologia", "dormitorio", "muebles", "lineablanca",
                           "modamujer", "modahombre", "zapatos", "deportes", "masCategorias"]
        self.url = "https://cl-ccom-parisapp-plp.ecomm.cencosud.com/getServicePLP/0/0/200?sort=destacados&refine_1=cgid={0}"
        self.HEADERS = {
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.3",
            "apikey": "cl-ccom-parisapp-plp",
        }

    def genUrls(self) -> list:
        return [self.url.format(c) for c in self.categorias]

    def getDiscount(self, normal, price) -> str:
        return round((normal - price) / normal * 100)
    
    def fromatMoney(self, precio)->str:
        return locale.currency(precio, grouping=True, symbol=False)
    
    def getData(self) -> list:
        rs = (grequests.get(u, headers=self.HEADERS) for u in self.genUrls())
        rq = grequests.map(rs)
        return [r.json()["payload"]["data"]["hits"] for r in rq if r.status_code == 200]

    def getOffers(self) -> list:
        if self.cache.fetchFromCache():
            return self.cache.get()
        offers = []

        for products in self.getData():
            try:
                for product in products:
                    if "clp-list-prices" in product['prices'] and "image" in product:
                        discount = self.getDiscount(
                            product['prices']["clp-list-prices"], product["price"])
                        if discount > 50:
                            offers.append(self.createOffer(
                                self.name, product["product_name"], str(
                                    discount)+"%",
                                self.fromatMoney(product["price"]), "https://www.paris.cl/" +
                                product["product_id"] + ".html",
                                product["image"]["link"]))
            except Exception as e:
                continue
        self.cache.set(offers)
        return offers
