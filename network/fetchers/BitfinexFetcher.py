from network.utils.BitfinexClient import Client

class BitfinexFetcher:

    _bitfinex=0

    def __init__(self, k=None, s=None):
        self._bitfinex = Client()

    def getBitfinexTicker(self):
        symbols = self._bitfinex.symbols()
        ticker = {}
        for symbol in symbols:
            symbol_key = symbol[0:3].upper()+"_"+symbol[3:6].upper()
            ticker[symbol_key] =  self._bitfinex.ticker(symbol)

        return ticker