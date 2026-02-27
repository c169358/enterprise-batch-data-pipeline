import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def filter_completed_transactions(df):
    return df[df["status"] == "COMPLETED"]


def validate_positive_amount(df):
    return df[df["amount"] > 0]


def remove_duplicate_transactions(df):
    before = len(df)
    df = df.drop_duplicates(subset=["transaction_id"])
    after = len(df)
    logging.info(f"Duplicate records removed: {before - after}")
    return df


def standardize_transaction_date(df):
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    return df


def classify_transaction_amount(df):
    df["transaction_category"] = df["amount"].apply(
        lambda x: "HIGH_VALUE" if x > 5000 else "NORMAL"
    )
    return df


def transform_transactions(df):
    try:
        logging.info("Starting transformation...")

        # Preserve original count for anomaly detection
        raw_count = len(df)

        df = filter_completed_transactions(df)
        df = validate_positive_amount(df)
        df = remove_duplicate_transactions(df)
        df = standardize_transaction_date(df)
        df = classify_transaction_amount(df)

        cleaned_count = len(df)

        # Basic anomaly detection rule
        if cleaned_count < raw_count * 0.5:
            logging.warning(
                "Anomaly detected: cleaned records dropped below 50% of raw records."
            )

        logging.info(f"Records after cleaning: {cleaned_count}")
        logging.info("Transformation Successful")

        return df

    except Exception as e:
        logging.error(f"Error during transformation: {e}")
        raise
    