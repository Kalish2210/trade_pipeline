import pandas as pd
import uuid
import random

# STEP 1: Load dataset
df = pd.read_csv("btcusd_1-min_data.csv",nrows=500)

# STEP 2: Remove empty rows
df = df.dropna()

# STEP 3: Create empty list
trades = []

# STEP 4: Loop through rows
for i in range(len(df) - 1):

    current = df.iloc[i]
    next_row = df.iloc[i + 1]

    # STEP 5: Choose BUY or SELL randomly
    trade_type = random.choice(["BUY", "SELL"])

    open_price = current["Open"]
    close_price = next_row["Close"]

    # STEP 6: Calculate profit
    if trade_type == "BUY":
        profit = close_price - open_price
    else:
        profit = open_price - close_price

    # STEP 7: Create trade object
    trade = {
        "trade_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1, 10)}",
        "symbol": "BTCUSD",
        "trade_type": trade_type,
        "open_time": pd.to_datetime(current["Timestamp"], unit='s'),
        "close_time": pd.to_datetime(next_row["Timestamp"], unit='s'),
        "open_price": open_price,
        "close_price": close_price,
        "lot_size": round(random.uniform(0.01, 1.0), 2),
        "profit_loss": round(profit, 2),
        "duration_secs": 60
    }

    trades.append(trade)

# STEP 8: Convert to DataFrame
trades_df = pd.DataFrame(trades)

# STEP 9: Save to CSV
trades_df.to_csv("trades.csv", index=False)

print("✅ trades.csv created successfully!")