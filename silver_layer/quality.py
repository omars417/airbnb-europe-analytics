import json
from pathlib import Path

import pandas as pd

ENGINEERED_FEATURES = [
    "price_per_guest",
    "price_per_bedroom",
    "distance_category",
    "metro_accessibility",
    "luxury_listing",
    "city_price_tier"
]


def generate_quality_report(df: pd.DataFrame) -> dict:
    """
    Generate quality metrics for the Silver dataset.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()), #Why two .sum() calls? The first .sum() gives: missing values per column The second .sum() adds those together: to
                                                      # get total number of missing values in the dataset.
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_columns": len(
            df.select_dtypes(include="number").columns
        ),
        "categorical_columns": len(
            df.select_dtypes(exclude="number").columns
        ),
        "engineered_features": ENGINEERED_FEATURES,
    }

    return report

def save_quality_report(report: dict, output_path: Path) -> None:
    """
    Save the quality report as JSON.
    """
    with output_path.open("w", encoding="utf-8") as file: #context manager (with)guarantees that when the block finishes,the file is closed automatically.
                                                          #Even if an error occurs.

        json.dump( #converts the Python dictionary into JSON and writes it directly to the file
            report,
            file,
            indent=4
        )