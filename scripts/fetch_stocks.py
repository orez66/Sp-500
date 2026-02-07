import yfinance as yf
import json
from datetime import datetime

SYMBOLS = [
    ("AAPL", "Apple"),
    ("MSFT", "Microsoft"),
    ("GOOGL", "Alphabet"),
    ("AMZN", "Amazon"),
    ("META", "Meta Platforms"),
    ("NVDA", "NVIDIA"),
    ("TSLA", "Tesla"),
]

data = []
tickers = [s[0] for s in SYMBOLS]
yf_data = yf.Tickers(" ".join(tickers))

for symbol, name in SYMBOLS:
    stock = yf_data.tickers[symbol]
    price = stock.fast_info.get("last_price")

    data.append({
        "symbol": symbol,
        "name": name,
        "price": price,
        "updated": datetime.utcnow().isoformat() + "Z"
    })

output = {
    "last_updated": datetime.utcnow().isoformat() + "Z",
    "stocks": data
}

with open("data/stocks.json", "w") as f:
    json.dump(output, f, indent=2)
