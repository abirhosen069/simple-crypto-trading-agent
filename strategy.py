# strategy.py
# Simple SMA crossover strategy implementation.
from typing import List
import pandas as pd


class SMACrossover:
def __init__(self, fast: int = 5, slow: int = 20):
if fast >= slow:
raise ValueError('fast period must be < slow period')
self.fast = fast
self.slow = slow


def compute(self, ohlcv: List[List]) -> pd.DataFrame:
# ohlcv rows: [timestamp, open, high, low, close, volume]
df = pd.DataFrame(ohlcv, columns=['ts', 'open', 'high', 'low', 'close', 'vol'])
df['close'] = df['close'].astype(float)
df['sma_fast'] = df['close'].rolling(self.fast).mean()
df['sma_slow'] = df['close'].rolling(self.slow).mean()
return df


def signal(self, df: pd.DataFrame) -> str:
# examine last two rows to detect crossover
if len(df) < self.slow + 1:
return 'hold'
last = df.iloc[-1]
prev = df.iloc[-2]
# bullish crossover
if prev['sma_fast'] <= prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
return 'buy'
# bearish crossover
if prev['sma_fast'] >= prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
return 'sell'
return 'hold'
