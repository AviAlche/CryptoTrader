import time
import json
import urllib

from network.fetchers.Client import Client

class BithumbClient(Client):

    _BaseUrl = "Https://api.bithumb.com"
    _singleTickerUrl = "/public/ticker"
    _symbols = ["BTC", "ETH", "DASH", "LTC", "ETC", "XRP"]

    def __init__(self):
        Client.__init__(self,None,None,self._baseUrl,None,self._singleTickerUrl)

    def getTickers(self):
        tickers = {}
        for symbol in self._symbols:
            tickers[symbol] = self.getTicker(symbol)
        return tickers



