import sqlite3
import logging


def load_to_warehouse(df, db_path):
    try:
        logging.info("Starting load process...")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Step 1: Load into staging table
        df.to_sql("transactions_staging", conn, if_exists="replace", index=False)
        logging.info("Loaded data into staging table")

        # Step 2: Create main table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions AS
            SELECT * FROM transactions_staging WHERE 1=0
        """)

        # Step 3: Delete existing matching records (simulate upsert)
        cursor.execute("""
            DELETE FROM transactions
            WHERE transaction_id IN (
                SELECT transaction_id FROM transactions_staging
            )
        """)

        # Step 4: Insert new records
        cursor.execute("""
            INSERT INTO transactions
            SELECT * FROM transactions_staging
        """)

        conn.commit()
        conn.close()

        logging.info("Merge into main table successful")

    except Exception as e:
        logging.error(f"Error during load: {e}")
        raise