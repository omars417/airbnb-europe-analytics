"""
Fact Table Module

Purpose
-------
Creates the central Fact table for the Gold Layer.

The Fact table combines:

- Silver dataset
- Dimension keys
- Market intelligence

into one analytical table.

Instead of storing descriptive values such as city names or room types,
the Fact table stores surrogate keys that reference dimension tables.

This follows the Star Schema design used in data warehouses.

Output
------
fact_listing.csv

Replace City with CityID

↓

Replace RoomType with RoomID

↓

Replace DayType with DayTypeID

↓

Merge Market Intelligence

↓

Engineer Business KPIs
"""

import pandas as pd


def replace_dimension_keys(fact_df: pd.DataFrame,dim_city: pd.DataFrame,dim_room: pd.DataFrame,dim_day: pd.DataFrame) -> pd.DataFrame:
    """
    Replace descriptive values with surrogate keys.
    """

    fact_df = fact_df.merge(
        dim_city,
        on="City", #Match the rows where the "City" column is equal in both DataFrames.
        how="left" #It keeps every row from the left table.(silver)
    )

    fact_df = fact_df.merge(
        dim_room,
        left_on="room_type", #Use room_type from the left table.
        right_on="RoomType", #Use RoomType from the right table. bec not same name like city
        how="left"
    )

    fact_df = fact_df.merge(
        dim_day,
        left_on="Day Type",
        right_on="DayType",
        how="left"
    )
    # Remove duplicated columns

    fact_df = fact_df.drop(
        columns=[
            "City",
            "room_type",
            "Day Type",
            "RoomType",
            "DayType"
        ]
    )

    return fact_df


def merge_market_data(
    fact_df: pd.DataFrame,
    market_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge city-level market intelligence into the Fact table.
    """

    fact_df = fact_df.merge(
        market_df,
        left_on="City",
        right_on="city",
        how="left"
    )

    fact_df.drop(
        columns=["city"],
        inplace=True
    )

    return fact_df


import numpy as np


def engineer_business_features(
    fact_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Create business-oriented KPIs for analytics.
    """

    # ----------------------------------
# Price Per Person
# ----------------------------------

    fact_df["PricePerPerson"] = (
        fact_df["realSum"] /
        fact_df["person_capacity"]
    )

    return fact_df

def create_fact_table(
    silver_df: pd.DataFrame,
    market_df: pd.DataFrame,
    dim_city: pd.DataFrame,
    dim_room: pd.DataFrame,
    dim_day: pd.DataFrame
) -> pd.DataFrame:
    """
    Create the Gold Layer Fact table.

    Workflow
    --------
    1. Merge city market intelligence.
    2. Replace descriptive values with dimension keys.
    3. Engineer business KPIs.
    4. Generate a surrogate ListingID.

    Parameters
    ----------
    silver_df : pd.DataFrame
        Silver dataset.

    market_df : pd.DataFrame
        Aggregated city market statistics.

    dim_city : pd.DataFrame
        City dimension.

    dim_room : pd.DataFrame
        Room dimension.

    dim_day : pd.DataFrame
        Day Type dimension.

    Returns
    -------
    pd.DataFrame
        Business-ready Fact table.
    """

    fact_df = silver_df.copy()

    # ----------------------------------
    # Merge Market Intelligence
    # ----------------------------------

    fact_df = merge_market_data(
        fact_df,
        market_df
    )

    # ----------------------------------
    # Replace descriptive values
    # ----------------------------------

    fact_df = replace_dimension_keys(
        fact_df,
        dim_city,
        dim_room,
        dim_day
    )

    # ----------------------------------
    # Engineer business KPIs
    # ----------------------------------

    fact_df = engineer_business_features(
        fact_df
    )

    # ----------------------------------
    # Create surrogate key
    # ----------------------------------

    fact_df.insert(
        0,
        "ListingID", #primary key.
        range(1, len(fact_df) + 1)
    )

    return fact_df

