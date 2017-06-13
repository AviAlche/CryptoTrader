import json
import urllib
import time


class Client():

    def __init__(self, APIKey = None, Secret = None, baseUrl="", allTickersUrl="", singleTickerUrl=""):
        self.APIKey = APIKey
        self.Secret = Secret
        self.nonce = int(time.time())
        self._BaseUrl = baseUrl
        self._allTickersUrl = allTickersUrl
        self._singleTickerUrl = singleTickerUrl

    def getTickers(self):
        ret = urllib.request.urlopen(urllib.request.Request(self._BaseUrl + self._allTickersUrl))
        return json.loads(ret.read())

    def getTicker(self, symbol = None):
        ret = urllib.request.urlopen(urllib.request.Request(self._BaseUrl + self._singleTickerUrl + "/" + symbol))
        return json.loads(ret.read())