import pandas as pd

def extract_metadata(dataset_name: str) -> tuple[str, str]:
    """
    Extract city and day type from a dataset name.
    Example:
        amsterdam_weekdays
            ->
        ("Amsterdam", "Weekdays")
    """

    city, day_type = dataset_name.rsplit("_", 1)

    return (
        city.title(),
        day_type.title()
    )

def merge_datasets(datasets: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Merge cleaned datasets into one master dataset.
    """

    merged_frames = []

    for dataset_name, df in datasets.items():

        city, day_type = extract_metadata(dataset_name)

        temp_df = df.copy()

        temp_df["City"] = city
        temp_df["Day Type"] = day_type

        merged_frames.append(temp_df)
#Repeated concatenation creates a new DataFrame on every iteration, which is inefficient. Building a list and concatenating 
# once is significantly faster and more scalable.
    master_df = pd.concat(
        merged_frames,
        ignore_index=True
    )

    return master_df