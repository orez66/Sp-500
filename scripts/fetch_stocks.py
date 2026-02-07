import yfinance as yf
import json
from datetime import datetime
import pandas as pd
import os

# 1. קבלת רשימת S&P 500 עדכנית
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
tables = pd.read_html(url)
sp500_table = tables[0]
symbols = sp500_table['Symbol'].tolist()
names = sp500_table['Security'].tolist()

# 2. יצירת חבילה YFinance
tickers = yf.Tickers(" ".join(symbols))

data = []
for symbol, name in zip(symbols, names):
    try:
        price = tickers.tickers[symbol].fast_info.get("last_price")
        data.append({
            "symbol": symbol,
            "name": name,
            "price": price
        })
    except Exception as e:
        # אם יש בעיה עם מניה מסוימת, נדלג עליה
        continue

output = {
    "last_updated": datetime.utcnow().isoformat() + "Z",
    "stocks": data
}

os.makedirs("data", exist_ok=True)
with open("data/stocks.json", "w") as f:
    json.dump(output, f, indent=2)
