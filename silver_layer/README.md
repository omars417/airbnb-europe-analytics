# Silver Layer

## Purpose

The Silver Layer transforms the raw Bronze datasets into a clean, consistent, and analytics-ready master dataset.

Unlike the Bronze Layer, which focuses on safe ingestion and traceability, the Silver Layer improves data quality and creates business value through cleaning, feature engineering, and dataset consolidation.

---

## Responsibilities

The Silver Layer is responsible for:

- Cleaning raw datasets
- Removing technical artifacts
- Handling missing values
- Removing duplicate records
- Engineering business features
- Merging all city datasets
- Generating a quality report
- Producing the master dataset for the Gold Layer

The Silver Layer does **not** perform SQL modeling or analytics.

---

## Architecture


---

## Modules

### cleaning.py

Responsible for improving data quality.

Tasks:

- Remove `Unnamed: 0`
- Remove duplicate rows
- Handle missing values
- Standardize column names

---

### merge.py

Combines every cleaned city dataset into one master DataFrame.

Output:
airbnb_master_dataset.csv


---

### feature_engineering.py

Creates new business features that improve downstream analysis.

Current engineered features:

- price_per_guest
- price_per_bedroom
- distance_category
- metro_accessibility
- luxury_listing
- city_price_tier

---

### quality.py

Generates a quality report summarizing the final Silver dataset.

Metrics include:

- Row count
- Column count
- Missing values
- Duplicate rows
- Numeric columns
- Categorical columns
- Engineered features

---

### pipeline.py

Coordinates the entire Silver workflow.

Execution order:

1. Load Bronze datasets
2. Clean datasets
3. Merge datasets
4. Engineer features
5. Generate quality report
6. Save outputs

---

## Outputs

The Silver Layer produces:

data/silver/

├── airbnb_master_dataset.csv
└── quality_report.json


---

## Downstream Usage

The Silver dataset becomes the source for:

- Gold Layer
- SQL Star Schema
- Power BI Dashboard