"""
Market Intelligence Module

Purpose
-------
Transforms the scraped Airbnb listings into city-level market statistics.

Instead of using individual scraped listings, this module aggregates the
data to represent the current Airbnb market for each city.

The resulting market metrics are later merged into the Fact table to enrich
the original dataset with external business intelligence.

This module produces one record per city containing metrics such as:
- Average listing price
- Median listing price
- Average rating
- Average review count
- Superhost rate
- Guest Favorite rate
- Number of scraped listings

Why?
----
The Silver dataset contains historical Airbnb listings, while the scraped
dataset represents the current market. By aggregating the scraped data,
we create market intelligence that can be used for analytics, reporting,
and feature engineering in the Gold Layer.

Output
------
One row per city containing aggregated market statistics.
input:
Scraped Dataset

Barcelona  200
Barcelona  180
Barcelona  220
Barcelona  250
output:
City        AvgPrice    MedianPrice    AvgRating    ...

Barcelona      212          210           4.86
"""

from pathlib import Path

import pandas as pd


def aggregate_market_data(scraped_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate scraped Airbnb listings into city-level market statistics.

    Parameters
    ----------
    scraped_df : pd.DataFrame
        Scraped Airbnb listings.

    Returns
    -------
    pd.DataFrame
        One row per city containing market statistics.
    """

    market_df = (
        scraped_df
        .groupby("city")
        .agg(
            #Create a new column called CityAveragePrice
            CityAveragePrice=("price", "mean"),
            CityMedianPrice=("price", "median"),
            CityAverageRating=("rating", "mean"),
            CityAverageReviews=("reviews", "mean"),
            SuperhostRate=("superhost", "mean"),
            GuestFavoriteRate=("guest_favorite", "mean"),
            ListingCount=("url", "count")
        )
        .reset_index()
    )

    return market_df


def save_market_data(market_df: pd.DataFrame,output_path: Path) -> None:
    """
    Save the aggregated market dataset.

    Parameters
    ----------
    market_df : pd.DataFrame
        Aggregated city market statistics.

    output_path : Path
        Destination CSV path.
    """

    market_df.to_csv(
        output_path,
        index=False
    )