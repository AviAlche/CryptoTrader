from network.utils.fbkheaRb import poloniex


class PoloniexFetcher:

    _poloniex = 0;

    def __init__(self,APIKey=None, Secret=None):
        self._poloniex = poloniex(APIKey, Secret)

    def getPoloniexTicker(self):
        return self._poloniex.returnTicker()


