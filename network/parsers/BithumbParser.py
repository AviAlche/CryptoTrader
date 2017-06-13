from network.utils.FiatCurrencyAPI import FiatCurrencyAPI


class BithumbParser():

    _headersDict = {"last" : "lastprice" ,
                  "av" : "last24hourspriceavarage",
                   "low" : "lowestAsk"}
    _fiatCurrency = "KRW"
    _fiatCurrencies = FiatCurrencyAPI().getCurrencies()

    def __init__(self) -> None:
        super().__init__()


    def parseTickers(self,tickers):
        print("Bithumb Tickers Data:")
        tickers = self.convertPairs(tickers)
        self.alignKeyValue(tickers)
        self.convetHeaders(tickers)
        self.convertPricesToUSD(tickers)
        for pair,attributes in tickers.items():
            print(pair + ":" + str(attributes))

    def convertPairs(self,tickers):
        validPairTickers = {}
        for pair, attributes in tickers.items():
            validPairTickers[pair+"_USD"] = tickers[pair]
        return validPairTickers

    def convetHeaders(self,tickers):
        for pair,attributes in tickers.items():
            for header,value in attributes.items():
                if (self._headersDict.__contains__(header)):
                    tickers[pair][self._headersDict[header]] = value
                else:
                    tickers[pair][header] = value

    def alignKeyValue(self, tickers):
        for key, value in tickers.items():
            tickers[key.upper()] = value["data"]

    def convertPricesToUSD(self,tickerData):
        for tickerKey, tickerValue in tickerData.items():
            for k, v in tickerValue.items():
                if("price" in k):
                    v = float(v)/self._fiatCurrencies["USD"+self._fiatCurrency]