


class YunbiParser():

    headersDict = {"last" : "lastprice" ,
                  "av" : "last24hourspriceavarage",
                   "low" : "lowestAsk"}

    def __init__(self) -> None:
        super().__init__()

    def parseTickers(self,tickers):
        print("Yunbi Tickers Data:")
        correctDict = self.alignKeyValue(tickers)
        correctDict = self.convetHeaders(correctDict)
        for pair,attributes in correctDict.items():
            print(pair + ":" + str(attributes))

    def convetHeaders(self,tickers):
        valideDict = {}
        for pair,attributes in tickers.items():
            validPairHeader = pair.upper()[0:3]+"_"+pair.upper()[3:6]
            valideDict[validPairHeader] = {}
            for header,value in attributes.items():
                if (self.headersDict.__contains__(header)):
                    valideDict[validPairHeader][self.headersDict[header]] = value
                else:
                    valideDict[validPairHeader][header] = value

        return valideDict

    def alignKeyValue(self, tickers):
        correctDict = {}
        for key, value in tickers.items():
            correctDict[key.upper()] = value["ticker"]
        return correctDict