# Exploratory Data Analysis Report

## Objective

Understand the datasets before implementing cleaning and feature engineering.

---

## Dataset Overview

- 20 datasets
- 10 European cities
- 51,707 listings
- 20 original columns

---

## Missing Values

No missing values were detected.

Result

No imputation was required.

---

## Duplicate Rows

No duplicate rows were found.

Result

Duplicate removal remains in the pipeline as a defensive measure.

---

## Data Types

Numeric and categorical columns were correctly inferred.

No type conversion was required.

---

## Outlier Analysis

Outliers were detected in:

- Price
- Distance
- Attraction Index
- Restaurant Index

Result

Outliers appear to represent legitimate premium listings and were retained.

---

## Correlation Analysis

Strongest correlations with price:

- Attraction Index (Normalized)
- Bedrooms
- Person Capacity
- Attraction Index

Weak correlations:

- Guest Satisfaction
- Cleanliness Rating
- Metro Distance

Conclusion

Existing features provide moderate predictive value.

Additional enrichment through web scraping was recommended by the project requirements.

---

## Cleaning Decisions

Based on the EDA:

- Remove technical columns
- Preserve legitimate outliers
- Do not perform missing value imputation
- Keep duplicate removal as a safeguard
- Preserve original data types

These decisions were implemented in the Silver Layer.