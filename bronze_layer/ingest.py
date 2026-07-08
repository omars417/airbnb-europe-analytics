import pandas as pd

from config import RAW_DATA_PATH
from logger import logger


def load_raw_data():
    """
    Load all CSV files from the raw data folder.

    Returns:
        dict:
            {
                filename: dataframe
            }
    """

    datasets = {}

    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    logger.info(f"Found {len(csv_files)} CSV files.")

    for file in csv_files:

        try:

            logger.info(f"Reading {file.name}") #file is data/raw/Paris.csv    file.name returns Paris.csv

            df = pd.read_csv(file)

            datasets[file.stem] = df           #file is Paris.csv .stem returns paris

            logger.info(
                f"Successfully loaded {file.name} ({len(df)} rows)"
            )

        except Exception as e:

            logger.error(f"Failed to load {file.name}")

            logger.error(str(e))

    return datasets


if __name__ == "__main__":

    data = load_raw_data()

    print(f"\nLoaded {len(data)} datasets successfully.")