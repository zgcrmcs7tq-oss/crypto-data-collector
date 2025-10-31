import requests
import pandas as pd
import time
from datetime import datetime

SYMBOL = "BTCUSDT"
INTERVAL = "1h"
LIMIT = 500
UPDATE_INTERVAL = 60*5

def get_binance_data(symbol=SYMBOL, interval=INTERVAL, limit=LIMIT):
    url = f"https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "Open time", "Open", "High", "Low", "Close", "Volume",
        "Close time", "Quote asset volume", "Number of trades",
        "Taker buy base", "Taker buy quote", "Ignore"
    ])
    df["Open time"] = pd.to_datetime(df["Open time"], unit='ms')
    df["Close time"] = pd.to_datetime(df["Close time"], unit='ms')
    df = df[["Open time", "Open", "High", "Low", "Close", "Volume"]].astype(float)
    return df

def save_to_csv(df, filename="btc_data.csv"):
    df.to_csv(filename, index=False)
    print(f"[{datetime.now()}] ✅ Đã lưu dữ liệu vào {filename}")

df = get_binance_data()
save_to_csv(df)
print(df.tail(5))