from network.fetchers.BitfinexFetcher import BitfinexFetcher
from network.fetchers.PoloniexFetcher import PoloniexFetcher


def main():
    polo = PoloniexFetcher()
    polo_data = polo.getPoloniexTicker()
    bitfinex = BitfinexFetcher()
    bitfinex_data = bitfinex.getBitfinexTicker()

main()