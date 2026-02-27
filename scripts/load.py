import sqlite3


def load_to_warehouse(df):
    try:
        print("Starting load process...")

        # Connect to SQLite database (creates file if not exists)
        conn = sqlite3.connect("../data/warehouse.db")

        # Load dataframe into database table
        df.to_sql("transactions", conn, if_exists="replace", index=False)

        conn.close()

        print("Load Successful: Data stored in warehouse.db")

    except Exception as e:
        print("Error during load:", e)