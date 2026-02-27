import logging
from extract import extract_transactions
from transform import transform_transactions
from load import load_to_warehouse


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    try:
        logging.info("Pipeline started")

        file_path = "../data/transactions_raw.csv"

        df = extract_transactions(file_path)
        transformed_df = transform_transactions(df)
        load_to_warehouse(transformed_df)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()