import numpy as np
import pandas as pd

def add_price_per_guest(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create price per guest feature.
    """

    df = df.copy()

    df["price_per_guest"] = (
        df["realSum"] /
        df["person_capacity"]
    )

    return df

def add_price_per_bedroom(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create price per bedroom feature.
    """

    df = df.copy()

    df["price_per_bedroom"] = np.where( #np.where() performs an element-wise conditional  For each row: If bedrooms == 0 Use price. Else Divide.
        df["bedrooms"] == 0,
        df["realSum"],
        df["realSum"] / df["bedrooms"]
    )
    return df
                    #This function receives a DataFrame and returns a DataFrame.
def add_distance_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize listings based on distance to city center.
    """

    df = df.copy()
                    #Everything larger than 5 km belongs in Outer Area
    bins = [0, 2, 5, float("inf")]

    labels = [
        "City Center",
        "Near Center",
        "Outer Area"
    ]

    df["distance_category"] = pd.cut( #Instead of many if statements: if dist < 2, use pd.cut()
        df["dist"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df

def add_metro_accessibility(df: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize metro accessibility.
    """

    df = df.copy()

    bins = [0, 0.5, 1.5, float("inf")]

    labels = [
        "Excellent",
        "Good",
        "Limited"
    ]

    df["metro_accessibility"] = pd.cut(
        df["metro_dist"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df

def add_luxury_listing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flag top 10% most expensive listings.
    """

    df = df.copy()

    threshold = df["realSum"].quantile(0.90)

    df["luxury_listing"] = (
        df["realSum"] >= threshold
    )

    return df

def add_city_price_tier(df: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize cities based on average listing price.
    """

    df = df.copy()

    city_avg = df.groupby("City")["realSum"].mean()

    high = city_avg.quantile(0.66)
    low = city_avg.quantile(0.33)

    mapping = {}

    for city, avg_price in city_avg.items():
        if avg_price >= high:
            mapping[city] = "Premium"
        elif avg_price <= low:
            mapping[city] = "Budget"
        else:
            mapping[city] = "Standard"

    df["city_price_tier"] = df["City"].map(mapping)

    return df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all feature engineering transformations.
    """

    df = add_price_per_guest(df)
    df = add_price_per_bedroom(df)
    df = add_distance_category(df)
    df = add_metro_accessibility(df)
    df = add_luxury_listing(df)
    df = add_city_price_tier(df)

    return df