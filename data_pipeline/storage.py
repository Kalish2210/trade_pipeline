import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="trade_db",
        user="postgres",
        password="Bala@"
    )

def insert_trade(trade):
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO trades (
                trade_id, user_id, symbol, trade_type,
                open_time, close_time, open_price, close_price,
                lot_size, profit_loss, duration_secs
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            trade["trade_id"],
            trade["user_id"],
            trade["symbol"],
            trade["trade_type"],
            trade["open_time"],
            trade["close_time"],
            trade["open_price"],
            trade["close_price"],
            trade["lot_size"],
            trade["profit_loss"],
            trade["duration_secs"]
        ))

        conn.commit()

    except Exception as e:
        print("DB Error:", e)

    finally:
        cur.close()
        conn.close()