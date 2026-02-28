import logging
import sys
import json
from extract import extract_transactions
from transform import transform_transactions
from load import load_to_warehouse


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config(env):
    with open("../config/config.json") as f:
        config = json.load(f)
    return config[env]


def run_pipeline(file_path, env):
    try:
        logging.info(f"Pipeline started in {env} environment")

        config = load_config(env)

        df = extract_transactions(file_path)
        transformed_df = transform_transactions(df)
        load_to_warehouse(transformed_df, config["database_path"])

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pipeline.py <file_path> <environment>")
        sys.exit(1)

    file_path = sys.argv[1]
    environment = sys.argv[2]

    run_pipeline(file_path, environment)