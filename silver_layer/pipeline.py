"""
Silver Layer Pipeline

Orchestrates the complete Silver Layer workflow.

Workflow:
1. Load Bronze datasets
2. Clean datasets
3. Merge datasets
4. Engineer features
5. Generate quality report
6. Save outputs
"""

from pathlib import Path

import pandas as pd
from pathlib import Path
import sys

# Project root (sprint1)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# bronze_layer folder
BRONZE_PATH = PROJECT_ROOT / "bronze_layer"

# Add project root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Add bronze_layer folder
if str(BRONZE_PATH) not in sys.path:
    sys.path.insert(0, str(BRONZE_PATH))

from ingest import load_raw_data        #The Bronze layer already knows how to load every CSV safely. Reuse it.
from config import SILVER_DATA_PATH
from logger import logger

from silver_layer.cleaning import clean_data
from silver_layer.merge import merge_datasets
from silver_layer.feature_engineering import engineer_features
from silver_layer.quality import (
    generate_quality_report,
    save_quality_report
)

MASTER_DATASET_PATH = (SILVER_DATA_PATH /"airbnb_master_dataset.csv")

QUALITY_REPORT_PATH = (SILVER_DATA_PATH /"quality_report.json")


def main() -> None:
    """
    Execute the Silver Layer pipeline.
    """

    datasets = load_raw_data()

    cleaned_datasets = {}

    for name, df in datasets.items():
        cleaned_datasets[name] = clean_data(df)
    
    master_df = merge_datasets(cleaned_datasets)

    master_df = engineer_features(master_df) #after merging. city_price_tier needs all cities.

    quality_report = generate_quality_report(master_df)

    master_df.to_csv(
        MASTER_DATASET_PATH,
        index=False #index=False If we don't use it  Pandas creates Unnamed: 0
    )

    save_quality_report(
        quality_report,
        QUALITY_REPORT_PATH
    )

    logger.info("Silver Layer completed successfully.")

if __name__ == "__main__": #Only run the pipeline if this file is executed directly.
    main()