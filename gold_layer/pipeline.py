"""
Gold Layer Pipeline

Purpose
-------
Coordinates the complete Gold Layer ETL workflow.

The Gold Layer transforms the Silver dataset into a
Star Schema and publishes it to the SQL Server
Data Warehouse.

Workflow
--------
1. Load the Silver dataset.
2. Load the scraped Airbnb dataset.
3. Create dimension tables.
4. Aggregate market intelligence.
5. Create the Fact table.
6. Save Gold CSV files.
7. Load SQL Server Data Warehouse.

Outputs
-------
- dim_city.csv
- dim_room.csv
- dim_day_type.csv
- city_market.csv
- fact_listing.csv

- SQL Server Warehouse (AirbnbDW)
"""

from pathlib import Path
import sys

import pandas as pd

# ==================================
# Project Paths
# ==================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BRONZE_PATH = PROJECT_ROOT / "bronze_layer"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if str(BRONZE_PATH) not in sys.path:
    sys.path.insert(0, str(BRONZE_PATH))

# ==================================
# Imports
# ==================================

from bronze_layer.config import (
    SILVER_DATA_PATH,
    SCRAPED_DATA_PATH,
    GOLD_DATA_PATH,
)

from bronze_layer.logger import logger

from dimensions import (
    create_dim_city,
    create_dim_room,
    create_dim_day_type,
)

from market import (
    aggregate_market_data,
    save_market_data,
)

from fact import (
    create_fact_table,
)

from load_data import load_data

# ==================================
# File Paths
# ==================================

SILVER_MASTER_PATH = (
    SILVER_DATA_PATH /
    "airbnb_master_dataset.csv"
)

SCRAPED_PATH = (
    SCRAPED_DATA_PATH /
    "scraped_airbnb.csv"
)

DIM_CITY_PATH = GOLD_DATA_PATH / "dim_city.csv"

DIM_ROOM_PATH = GOLD_DATA_PATH / "dim_room.csv"

DIM_DAY_PATH = GOLD_DATA_PATH / "dim_day_type.csv"

CITY_MARKET_PATH = GOLD_DATA_PATH / "city_market.csv"

FACT_PATH = GOLD_DATA_PATH / "fact_listing.csv"

# ==================================
# Pipeline
# ==================================

def main() -> None:
    """
    Execute the complete Gold Layer pipeline.
    """

    # ----------------------------------
    # Load datasets
    # ----------------------------------

    logger.info("Loading datasets...")

    silver_df = pd.read_csv(SILVER_MASTER_PATH)

    scraped_df = pd.read_csv(SCRAPED_PATH)

    # ----------------------------------
    # Create Dimensions
    # ----------------------------------

    logger.info("Creating dimensions...")

    dim_city = create_dim_city(silver_df)

    dim_room = create_dim_room(silver_df)

    dim_day = create_dim_day_type(silver_df)

    # ----------------------------------
    # Market Intelligence
    # ----------------------------------

    logger.info("Aggregating market intelligence...")

    market_df = aggregate_market_data(scraped_df)

    # ----------------------------------
    # Fact Table
    # ----------------------------------

    logger.info("Creating fact table...")

    fact_df = create_fact_table(
        silver_df=silver_df,
        market_df=market_df,
        dim_city=dim_city,
        dim_room=dim_room,
        dim_day=dim_day,
    )

    # ----------------------------------
    # Save Gold CSVs
    # ----------------------------------

    logger.info("Saving Gold tables...")

    dim_city.to_csv(
        DIM_CITY_PATH,
        index=False,
    )

    dim_room.to_csv(
        DIM_ROOM_PATH,
        index=False,
    )

    dim_day.to_csv(
        DIM_DAY_PATH,
        index=False,
    )

    save_market_data(
        market_df,
        CITY_MARKET_PATH,
    )

    fact_df.to_csv(
        FACT_PATH,
        index=False,
    )

    # ----------------------------------
    # Load SQL Server
    # ----------------------------------

    logger.info("Loading Gold Layer into SQL Server...")

    try:

        load_data()

        logger.info("SQL Server warehouse loaded successfully.")

    except Exception as error:

        logger.error(f"Failed to load SQL Server: {error}")

        raise

    logger.info("Gold Layer completed successfully.")

if __name__ == "__main__":
    main()