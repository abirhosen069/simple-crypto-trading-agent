import ccxt
import time


class ExchangeClient:
def __init__(self, config: dict):
ex = getattr(ccxt, config.get('exchange'))
self.exchange = ex({
'apiKey': config.get('api', {}).get('key'),
'secret': config.get('api', {}).get('secret'),
'enableRateLimit': True,
})


def fetch_ohlcv(self, symbol: str, timeframe: str='1m', limit: int=100):
return self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)


def fetch_ticker(self, symbol: str):
return self.exchange.fetch_ticker(symbol)


def create_limit_buy(self, symbol, price, amount):
return self.exchange.create_limit_buy_order(symbol, amount, price)


def create_limit_sell(self, symbol, price, amount):
return self.exchange.create_limit_sell_order(symbol, amount, price)


def create_market_buy(self, symbol, amount):
return self.exchange.create_market_buy_order(symbol, amount)


def create_market_sell(self, symbol, amount):
return self.exchange.create_market_sell_order(symbol, amount)


def sleep(self, seconds):
time.sleep(seconds)
