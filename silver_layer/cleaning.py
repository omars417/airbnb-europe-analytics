import pandas as pd

def remove_technical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove non-business columns.
    """

    df = df.copy()

    return df.drop(
        columns=["Unnamed: 0"],
        errors="ignore" #Suppose a dataset already doesn't contain Then df.drop(columns=["Unnamed: 0"]) raises: KeyError The pipeline stops. Using     
                        #errors="ignore" means "Remove it if it exists, otherwise continue."
    )

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names.
    """

    df = df.copy()

    df.columns = df.columns.str.strip() #strip() removes whitespace from the beginning and end of a string.

    return df

EXPECTED_TYPES = {
    "person_capacity": "int64",
    "bedrooms": "int64",
    "realSum": "float64",
    "dist": "float64",
    "metro_dist": "float64",
    "cleanliness_rating": "float64",
    "guest_satisfaction_overall": "float64",
    "attr_index": "float64",
    "attr_index_norm": "float64",
    "rest_index": "float64",
    "rest_index_norm": "float64",
    "lat": "float64",
    "lng": "float64"
}

def standardize_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column data types.
    """

    df = df.copy()

    for column, dtype in EXPECTED_TYPES.items():

        if column not in df.columns:
            continue

        if "float" in dtype:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            ).astype(dtype)

        elif "int" in dtype:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            ).astype(dtype)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all cleaning steps.
    """

    df = remove_technical_columns(df)
    df = standardize_column_names(df)
    df = standardize_data_types(df)

    return df