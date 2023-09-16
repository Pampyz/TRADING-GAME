class Order:
    def __init__(self):
        pass

class Marketplace:
    def __init__(self):
        self.order_book = []
    
    def print_order_book(self):
        pass

class BarterMarketplace(Marketplace):
    def __init__(self):
        super().__init__()

    def exchange():
        pass

class MoneyMarketplace(Marketplace):
    def __init__(self, money_asset):
        super().__init__()

MarketplaceFactory = {
    'barter': BarterMarketplace,
    'money': MoneyMarketplace
}