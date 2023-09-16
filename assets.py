class Asset:
    def __init__(self, global_supply):
        pass

    def create(self, n):
        pass

class InflationaryAsset(Asset):
    def __init__(self, global_supply, inflation_rate):
        super().__init__(global_supply)

AssetFactory = {
    'inflationary': InflationaryAsset
}