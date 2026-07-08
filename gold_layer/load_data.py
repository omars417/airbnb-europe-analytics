"""
SQL Server Data Loader

Purpose
-------
Loads the Gold Layer CSV files into the SQL Server
data warehouse.

Responsibilities
----------------
- Read Gold CSV files
- Connect to SQL Server
- Insert data into existing tables

The database schema is created separately using
create_schema.sql.
"""

from pathlib import Path
import sys

import pandas as pd

# ==========================
# Project Root
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BRONZE_PATH = PROJECT_ROOT / "bronze_layer"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if str(BRONZE_PATH) not in sys.path:
    sys.path.insert(0, str(BRONZE_PATH))

from bronze_layer.config import GOLD_DATA_PATH
from bronze_layer.logger import logger

from database import get_engine

DIM_CITY_PATH = GOLD_DATA_PATH / "dim_city.csv"

DIM_ROOM_PATH = GOLD_DATA_PATH / "dim_room.csv"

DIM_DAY_PATH = GOLD_DATA_PATH / "dim_day_type.csv"

CITY_MARKET_PATH = GOLD_DATA_PATH / "city_market.csv"

FACT_PATH = GOLD_DATA_PATH / "fact_listing.csv"

def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a Gold CSV file.
    """

    return pd.read_csv(path)

def insert_table(
    dataframe: pd.DataFrame,
    table_name: str,
    engine,
) -> None:
    """
    Insert rows into SQL Server.
    """

    dataframe.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
    )
    #to_sql(..., if_exists="append") translates every DataFrame row into SQL INSERT statements behind the scenes.

    logger.info(f"{table_name} loaded successfully.")

def load_data() -> None:
    """
    Load the Gold Layer into SQL Server.
    """

    logger.info("Connecting to SQL Server...")

    engine = get_engine()
    from sqlalchemy import text

    with engine.begin() as connection:
        #Before loading the data, clear the tables.
        connection.execute(text("DELETE FROM FactListing"))
        connection.execute(text("DELETE FROM CityMarket"))
        connection.execute(text("DELETE FROM DimRoom"))
        connection.execute(text("DELETE FROM DimDayType"))
        connection.execute(text("DELETE FROM DimCity"))

    logger.info("Reading Gold CSV files...")

    dim_city = load_csv(DIM_CITY_PATH)

    dim_room = load_csv(DIM_ROOM_PATH)

    dim_day = load_csv(DIM_DAY_PATH)

    city_market = load_csv(CITY_MARKET_PATH)

    fact_listing = load_csv(FACT_PATH)

    logger.info("Loading tables...")

    insert_table(
        dim_city,
        "DimCity",
        engine
    )

    insert_table(
        dim_room,
        "DimRoom",
        engine
    )

    insert_table(
        dim_day,
        "DimDayType",
        engine
    )

    insert_table(
        city_market,
        "CityMarket",
        engine
    )
    insert_table(
        fact_listing,
        "FactListing",
        engine
    )

    logger.info("Gold Layer loaded successfully.")

if __name__ == "__main__":
    load_data()