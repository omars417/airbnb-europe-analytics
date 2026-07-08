import json

from ingest import load_raw_data
from config import METADATA_FILE
from logger import logger

def generate_metadata(datasets):
    """
    Generate metadata for every dataset.
    """

    metadata = {}
    for dataset_name, df in datasets.items():
        metadata[dataset_name] = {

            "rows": len(df),

            "columns": len(df.columns),

            "column_names": df.columns.tolist(), #JSON cannot directly serialize a Pandas Index object, so we convert it into a regular Python list.

            "missing_values": df.isnull().sum().to_dict(),

            "data_types": df.dtypes.astype(str).to_dict()
        }   
    logger.info("Metadata generated successfully.")

    return metadata     

def save_metadata(metadata):
    """
    Save metadata as JSON.
    """

    with open(METADATA_FILE, "w") as file: # "w" means write mode.

        json.dump(
            metadata,
            file,
            indent=4
        )
        #metadata → the data to save.     file → the file object to write into.   indent=4 → formats the JSON with 4 spaces of indentation, making it easy to read.

    logger.info("Metadata saved successfully.")

if __name__ == "__main__":

    datasets = load_raw_data()

    metadata = generate_metadata(datasets)

    save_metadata(metadata)

    print(
        "Metadata generated successfully."
    )