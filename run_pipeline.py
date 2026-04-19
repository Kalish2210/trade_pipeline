import os
from data_pipeline.ingestion import load_data
from data_pipeline.cleaning import clean_trade   # ✅ ADD THIS
from data_pipeline.validation import validate_trade
from data_pipeline.storage import insert_trade

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "trades.csv")

def run():
    print(f"🔍 Looking for file at: {DATA_PATH}")
    
    if not os.path.exists(DATA_PATH):
        print(f"❌ ERROR: file not found at {DATA_PATH}")
        return

    trades = load_data(DATA_PATH)
    count = 0

    for trade in trades:

        # 🧹 STEP 1: CLEAN
        trade = clean_trade(trade)

        # 🚫 STEP 2: VALIDATE
        valid, result = validate_trade(trade)

        if valid:
            insert_trade(result)
            count += 1
        else:
            print(f"⚠️ Validation failed for trade: {result}")

    print(f"✅ Successfully stored {count} trades in PostgreSQL")


if __name__ == "__main__":
    run()