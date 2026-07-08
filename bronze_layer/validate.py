from config import EXPECTED_COLUMNS
from logger import logger
from ingest import load_raw_data

def validate_schema(datasets):
    """
    Validate that every dataset contains
    the expected columns.
    """

    validation_results = {}
        #dict
    for dataset_name, df in datasets.items():
        
        if "Unnamed: 0" in df.columns:
            df = df.drop(columns=["Unnamed: 0"])

        actual_columns = set(df.columns)
        expected_columns = set(EXPECTED_COLUMNS)

        missing_columns = expected_columns - actual_columns
        extra_columns = actual_columns - expected_columns

        is_valid = (
            len(missing_columns) == 0
            and
            len(extra_columns) == 0
        )

        validation_results[dataset_name] = {
            "valid": is_valid,
            "missing_columns": list(missing_columns),
            "extra_columns": list(extra_columns)
        }

        if is_valid:

            logger.info(f"{dataset_name}: Schema validation passed.")

        else:

            logger.error(f"{dataset_name}: Schema validation failed.")

            if missing_columns:
                logger.error(
                    f"Missing columns: {missing_columns}"
                )

            if extra_columns:
                logger.error(
                    f"Unexpected columns: {extra_columns}"
                )

    return validation_results


if __name__ == "__main__":

    datasets = load_raw_data()

    results = validate_schema(datasets)

    passed = sum(
        result["valid"]
        for result in results.values()
    )

    print(f"\n{passed}/{len(results)} datasets passed validation.")