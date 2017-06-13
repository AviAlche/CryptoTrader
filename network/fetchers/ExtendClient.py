from network.fetchers.Client import Client

class ExtendClient(Client):

    def __init__(self,APIKey = None, Secret = None):
        Client.__init__(self,APIKey, Secret)

    def getTickers(self):
        pass

    def getTicker(self,symbol = None):
        pass

