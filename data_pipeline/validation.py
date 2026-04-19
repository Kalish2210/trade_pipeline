ALLOWED_SYMBOLS = {"EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "BTCUSD", "US30", "NAS100"}

def validate_trade(trade):
    try:
        if trade["symbol"] not in ALLOWED_SYMBOLS:
            return False, "Invalid symbol"

        if trade["trade_type"] not in ["BUY", "SELL"]:
            return False, "Invalid type"

        if float(trade["lot_size"]) < 0.01 or float(trade["lot_size"]) > 100:
            return False, "Invalid lot size"

        if int(trade["duration_secs"]) <= 0:
            return False, "Invalid duration"

        return True, trade

    except Exception as e:
        return False, str(e)