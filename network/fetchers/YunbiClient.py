import hashlib
import hmac
import time
import json
import urllib

from network.fetchers.Client import Client

class YunbiClient(Client):

    _baseUrl = "https://yunbi.com"
    _allTickersUrl = "/api/v2/tickers.json"
    _symbolsUrl = "/api/v2/markets.json"

    def __init__(self):
        Client.__init__(self,None,None,self._baseUrl,self._allTickersUrl,None)




