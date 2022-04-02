from polygon import RESTClient

class PolygonAPIHandler:

    def __init__(self, authKey):
        self.client = RESTClient(authKey)
    
    def get_client(self):
        return self.client

    def get_previous_close(self, stockName):
        return self.client.stocks_equities_previous_close(stockName).results