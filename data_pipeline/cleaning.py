import logging
from datetime import datetime

logging.basicConfig(filename="cleaning.log", level=logging.INFO)

def clean_trade(trade):

    # Normalize text
    trade["symbol"] = trade["symbol"].strip().upper()
    trade["trade_type"] = trade["trade_type"].strip().upper()

    # Fix timestamps
    trade["open_time"] = parse_time(trade["open_time"])
    trade["close_time"] = parse_time(trade["close_time"])

    # Handle missing values
    if trade.get("open_price") is None:
        trade["open_price"] = trade.get("close_price")
        logging.info(f"Filled open_price for {trade['trade_id']}")

    return trade


def parse_time(t):
    return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")