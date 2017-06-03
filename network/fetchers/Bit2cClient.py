import hashlib
import hmac
import time
import json
import urllib

from network.fetchers.Client import Client

class Bit2cClient(Client):

    _Url = "https://bit2c.co.il"
    _EXCHANGES = "/Exchanges"
    _ORDERS = "/Order"
    _relevantPairs = {"BTN_NIS": 0,
                      "LTC_BTC": 1,
                      "LTC_NIS": 2}

    def __init__(self,APIKey = None, Secret = None):
        Client.__init__(self,APIKey, Secret)
        self.nonce = int(time.time())



    def query(self, command, req={}):

        if (command == self._EXCHANGES):
            ret = urllib.request.urlopen(urllib.request.Request(self._Url + self._EXCHANGES))
            return json.loads(ret.read())
        elif (command == "returnOrderBook"):
            ret = urllib.request.urlopen(urllib.request.Request(
                'https://poloniex.com/public?command=' + command + '&currencyPair=' + str(req['currencyPair'])))
            return json.loads(ret.read())
        elif (command == "returnMarketTradeHistory"):
            ret = urllib.request.urlopen(urllib.request.Request(
                'https://poloniex.com/public?command=' + "returnTradeHistory" + '&currencyPair=' + str(
                    req['currencyPair'])))
            return json.loads(ret.read())
        else:
            req['command'] = command
            req['nonce'] = int(time.time() * 1000)
            post_data = urllib.request.urlencode(req)

            sign = hmac.new(self.Secret, post_data, hashlib.sha512).hexdigest()
            headers = {
                'Sign': sign,
                'Key': self.APIKey
            }

            ret = urllib.request.urlopen(urllib.request.Request('https://poloniex.com/tradingApi', post_data, headers))
            jsonRet = json.loads(ret.read())
            return self.post_process(jsonRet)

    # def balance(self):
    #     qString = "nonce=" + str(self.nonce)
    #     sign = self.ComputeHash(qString)
    #     url = self.Url + "Account/Balance"
    #     response = self.query(qString, url, sign)
    #     _json = json.loads(response.decode("utf-8"))
    #     # Balance(_json['BalanceNIS'], _json['BalanceLTC'], _json['BalanceBTC'])
    #
    # def getTrades(self, Pair, since=0, date=0):
    #     url = self.Url + "Exchanges/" + str(Pair) + "/trades.json"
    #     response = self.DownloadString(url)
    #     _json = json.loads(response.decode("utf-8"))
    #     ExchangesTrades = []
    #     # for jsonObj in _json:
    #         # exTrade = ExchangesTrade(jsonObj['date'], jsonObj['price'], jsonObj['amount'], jsonObj['tid'])
    #         # ExchangesTrades.append(exTrade)
    #     return ExchangesTrades

    def getTicker(self, Pair=_relevantPairs["BTN_NIS"]):
        ret = urllib.request.urlopen(
            urllib.request.Request(self._Url + self._EXCHANGES + "/" + str(Pair) + "/Ticker.json"))
        return json.loads(ret.read())


    def getTickers(self):
        ticker = {}
        for pairName, pairNum in self._relevantPairs.items():
            ticker[pairName] = self.getTicker(pairNum)
        return ticker

