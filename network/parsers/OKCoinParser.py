

class OKCoinParser():

    headersDict = {"low" : "lowestAsk",
                   "high" : "highestBid",
                   "last" : "lastprice"}

    def __init__(self) -> None:
        super().__init__()

    def parseTickers(self,tickers):
        print("OKCoin Tickers Data:")
        correctDict = self.alignKeyValue(tickers)
        correctDict = self.convetHeaders(correctDict)
        for pair,attributes in correctDict.items():
            print(pair + ":" + str(attributes))

    def convetHeaders(self,tickers):
        valideDict = {}
        for pair,attributes in tickers.items():
            valideDict[pair] = {}
            for header,value in attributes.items():
                if(self.headersDict.__contains__(header)):
                    valideDict[pair][self.headersDict[header]] = value
                else:
                    valideDict[pair][header] = value
        return valideDict

    def alignKeyValue(self, tickers):
        correctDict = {}
        for key, value in tickers.items():
            correctDict[key.upper()] = value["ticker"]
        return correctDict