"""
Gold Layer Pipeline

Orchestrates the complete scraping workflow.

Workflow
--------
1. Load master dataset
2. Extract unique cities
3. Create Selenium driver
4. Collect listing URLs
5. Parse listing details
6. Save scraped dataset
"""

from pathlib import Path
import sys
import pandas as pd
# ==========================
# Project Root
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Bronze layer path
BRONZE_PATH = PROJECT_ROOT / "bronze_layer"

# Add project root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Add bronze_layer BEFORE the current folder
if str(BRONZE_PATH) not in sys.path:
    sys.path.insert(0, str(BRONZE_PATH))
# Scraping folder path
SCRAPING_PATH = Path(__file__).resolve().parent

if str(SCRAPING_PATH) not in sys.path:
    sys.path.insert(0, str(SCRAPING_PATH))
# ==========================
# Imports
# ==========================

from bronze_layer.config import SILVER_DATA_PATH
from scraper_config import SCRAPED_DATA_PATH
from bronze_layer.logger import logger

from scraper import (
    create_driver,
    collect_listing_urls,
    close_driver,
)

from parser import parse_listing

# ==========================
# Paths
# ==========================

MASTER_DATASET_PATH = (
    SILVER_DATA_PATH /
    "airbnb_master_dataset.csv"
)

OUTPUT_PATH = (
    SCRAPED_DATA_PATH /
    "scraped_airbnb.csv"
)


def main():
    """
    Execute the Gold Layer pipeline.
    """

    logger.info("Loading master dataset...")

    master_df = pd.read_csv(MASTER_DATASET_PATH)

    cities = (
        master_df["City"]
        .drop_duplicates()
        .sort_values()
        .tolist()
    )

    logger.info(f"Found {len(cities)} cities.")

    driver = create_driver()

    scraped_data = []

    try:

        for city in cities:

            logger.info(f"Scraping {city}...")

            urls = collect_listing_urls(
                        driver,
                        city
            )

            logger.info(
                        f"Collected {len(urls)} listing URLs."
            )

            for url in urls:

                listing = parse_listing(driver,url)

                listing["city"] = city

                scraped_data.append(listing)

    finally:

        close_driver(driver)

    scraped_df = pd.DataFrame(scraped_data)

    scraped_df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    logger.info(
        f"Saved {len(scraped_df)} listings."
    )


if __name__ == "__main__":
    main()