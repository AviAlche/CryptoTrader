

class BitfinexParser():

    headersDict = {"bid":"highestBid",
                   "ask":"lowestAsk",
                   "last_price":"lastprice"}

    def __init__(self) -> None:
        super().__init__()

    def parseTickers(self,tickers):
        print("Bitfinex Tickers Data:")
        correctDict = self.convetHeaders(tickers)
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