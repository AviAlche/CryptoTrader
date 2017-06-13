from network.fetchers.Bit2cClient import Bit2cClient
from network.fetchers.Bit2cFetcher import Bit2cFetcher
from network.fetchers.BitfinexClient import BitfinexClient
from network.fetchers.BitfinexFetcher import BitfinexFetcher
from network.fetchers.BithumbClient import BithumbClient
from network.fetchers.ExtendClient import ExtendClient
from network.fetchers.PoloniexClient import PoloniexClient
from network.fetchers.PoloniexFetcher import PoloniexFetcher
from network.fetchers.OKCoinClient import OKCoinClient
from network.fetchers.YunbiClient import YunbiClient
from network.parsers.Bit2cParser import Bit2cParser
from network.parsers.BitfinexParser import BitfinexParser
from network.parsers.BithumbParser import BithumbParser
from network.parsers.OKCoinParser import OKCoinParser
from network.parsers.PoloniexParser import PoloniexParser
from network.parsers.YunbiParser import YunbiParser
from network.utils.FiatCurrencyAPI import FiatCurrencyAPI


def main():


    print("All exchanges tickers:")
    #
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
    okcoinData = okcoinParser.parseTickers(okcoinClient.getTickers())
    print("###############################################")

    yunbiClient = YunbiClient()
    yunbiParser = YunbiParser()
    yunbiData = yunbiParser.parseTickers(yunbiClient.getTickers())
    print("###############################################")

    bithumbClient = BithumbClient()
    bithumbParser = BithumbParser()
    bithumbData = bithumbParser.parseTickers(bithumbClient.getTickers())
    print("###############################################")


    # currencyAPI = FiatCurrencyAPI()
    # x = currencyAPI.getCurrencies()


main()