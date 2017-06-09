from network.fetchers.Bit2cClient import Bit2cClient
from network.fetchers.Bit2cFetcher import Bit2cFetcher
from network.fetchers.BitfinexClient import BitfinexClient
from network.fetchers.BitfinexFetcher import BitfinexFetcher
from network.fetchers.ExtendClient import ExtendClient
from network.fetchers.PoloniexClient import PoloniexClient
from network.fetchers.PoloniexFetcher import PoloniexFetcher
from network.fetchers.OKCoinClient import OKCoinClient
from network.parsers.Bit2cParser import Bit2cParser
from network.parsers.BitfinexParser import BitfinexParser
from network.parsers.OKCoinParser import OKCoinParser
from network.parsers.PoloniexParser import PoloniexParser


def main():

    print("All exchanges tickers:")

    polClient = PoloniexClient()
    polParser = PoloniexParser()
    polData = polParser.parseTickers(polClient.getTickers())
    print("###############################################")

    bit2cClient = Bit2cClient()
    bit2cParser = Bit2cParser()
    bit2cData = bit2cParser.parseTickers(bit2cClient.getTickers())
    print("###############################################")

    bitfinexClient = BitfinexClient()
    bitfinexParser = BitfinexParser()
    bitfinexData = bitfinexParser.parseTickers(bitfinexClient.getTickers())
    print("###############################################")

    okcoinClient = OKCoinClient()
    okcoinParser = OKCoinParser()
    # okcoinClient.ticker("btc_usd");
    okcoinData = okcoinParser.parseTickers(okcoinClient.getTickers())
    print("###############################################")


    # print(xbtce.ticker("ltc_usd"))
    # exClient = ExtendClient()
    # print("bla")
    # polo = PoloniexFetcher()
    # polo_data = polo.getTickers()
    # print(polo_data)
    # bitfinex = BitfinexFetcher()
    # bitfinex_data = bitfinex.getTickers()
    # print(bitfinex_data)
    # bit2c = Bit2cFetcher()
    # bit2c_data = bit2c.getTickers()
    # print(bit2c_data)

main()