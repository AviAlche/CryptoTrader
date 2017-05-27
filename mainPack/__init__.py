from network.fetchers.Bit2cFetcher import Bit2cFetcher
from network.fetchers.BitfinexFetcher import BitfinexFetcher
from network.fetchers.PoloniexFetcher import PoloniexFetcher


def main():
    polo = PoloniexFetcher()
    polo_data = polo.getTickers()
    print(polo_data)
    bitfinex = BitfinexFetcher()
    bitfinex_data = bitfinex.getTickers()
    print(bitfinex_data)
    bit2c = Bit2cFetcher()
    bit2c_data = bit2c.getTickers()
    print(bit2c_data)

main()