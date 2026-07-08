# 🏡 Airbnb Europe Analytics Platform

> An end-to-end Data Engineering & Business Intelligence pipeline that transforms raw Airbnb datasets into a SQL Server Data Warehouse and interactive Power BI dashboards.

---

# 📖 Project Overview

This project was developed as part of the **Instant Summer Internship Sprint 1**.

The objective was to build a complete data pipeline capable of ingesting raw Airbnb datasets, cleaning and enriching the data, modeling it into a dimensional data warehouse, and delivering business-ready insights through Power BI.

Unlike traditional dashboard projects, this solution follows a modern **Medallion Architecture (Bronze → Silver → Gold)**, simulating how data engineering teams process data in production environments.

The project also enriches the original dataset by scraping additional Airbnb information such as ratings, reviews, Guest Favorite status, Superhost status, and current listing prices.

---

# 🏗️ Architecture

```
                    Raw CSV Files
                          │
                          ▼
                  🥉 Bronze Layer
             Data Ingestion & Validation
                          │
                          ▼
                  🥈 Silver Layer
       Cleaning • Feature Engineering • EDA
                          │
                          ▼
              🌐 Selenium Web Scraping
       Ratings • Reviews • Prices • Enrichment
                          │
                          ▼
                  🥇 Gold Layer
       Star Schema • Fact & Dimension Tables
                          │
                          ▼
                 SQL Server Warehouse
                          │
                          ▼
               📊 Power BI Dashboard
```

---

# 📂 Project Structure

```
Airbnb-Europe-Analytics/

│
├── bronze_layer/
│   ├── ingest.py
│   ├── validate.py
│   ├── metadata.py
│   ├── logger.py
│   └── pipeline.py
│
├── silver_layer/
│   ├── cleaning.py
│   ├── feature_engineering.py
│   ├── merge.py
│   ├── quality.py
│   └── pipeline.py
│
├── gold_layer/
│   ├── dimensions.py
│   ├── market.py
│   ├── fact.py
│   ├── create_schema.sql
│   ├── load_data.py
│   └── pipeline.py
│
├── scraping/
│   ├── scraper.py
│   ├── repair_prices.py
│   └── ...
│
├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── scraped/
│
├── powerbi/
│   └── Airbnb Dashboard.pbix
│
└── README.md
```

---

# 🥉 Bronze Layer

The Bronze Layer is responsible for collecting and validating the raw datasets.

### Features

- Automatic CSV discovery
- Schema validation
- Metadata generation
- Pipeline logging
- Automated ingestion

### Output

- Raw validated datasets
- Metadata report
- Pipeline logs

---

# 🥈 Silver Layer

The Silver Layer transforms raw data into analytics-ready datasets.

### Features

- Missing value handling
- Duplicate removal
- Data cleaning
- Data type validation
- Feature engineering
- Master dataset generation
- Data quality reports

### Engineered Features

- Price Per Person
- Price Per Bedroom
- Distance Category
- Metro Accessibility
- Luxury Listing
- City Price Tier
- Weekend Flag

---

# 🌐 Web Scraping

To enrich the original dataset, Selenium was used to collect additional Airbnb information.

### Extracted Data

- Current Listing Price
- Ratings
- Reviews
- Guest Favorite Status
- Superhost Status

The scraper automatically repaired missing prices and enriched the analytical dataset.

---

# 🥇 Gold Layer

The Gold Layer transforms the Silver dataset into a dimensional model following the **Star Schema** architecture.

### Dimension Tables

- DimCity
- DimRoom
- DimDayType

### Fact Table

- FactListing

### Market Intelligence

- CityMarket

The Gold Layer is optimized for business intelligence and reporting.

---

# 🗄️ SQL Server Data Warehouse

The dimensional model was implemented in SQL Server.

### Features

- Primary Keys
- Foreign Keys
- Fact Table
- Dimension Tables
- SQL DDL Scripts
- Automated Data Loading using SQLAlchemy

---

# 📊 Power BI Dashboard

The project includes a five-page executive dashboard.

## 🏠 Executive Overview

- Total Listings
- Average Price
- Average Guest Satisfaction
- Price per Person
- City Comparison
- Weekend vs Weekday Analysis

---

## 📈 Market Intelligence

Using scraped Airbnb data:

- Average Market Price
- Average Rating
- Average Reviews
- Superhost Rate
- Guest Favorite Rate

---

## 🌍 Geographic Insights

- Listing Map
- Distance vs Price
- Metro Distance Analysis
- Geographic Price Distribution

---

## 🏡 Listing Analysis

- Bedrooms vs Price
- Capacity vs Price
- Guest Satisfaction vs Price
- Room Type Analysis
- Price Distribution

---

## 🧠 Feature Engineering Insights

Custom engineered features including:

- Price Per Person
- Price Per Bedroom
- Distance Category
- Metro Accessibility
- Luxury Listing
- City Price Tier

---

# 📈 Technologies Used

- Python
- Pandas
- NumPy
- Selenium
- SQL Server
- SQLAlchemy
- Power BI
- Git
- VS Code

---

# 📊 Data Engineering Concepts

This project demonstrates practical implementation of:

- ETL Pipelines
- Medallion Architecture
- Star Schema
- Fact & Dimension Modeling
- Data Warehousing
- Data Validation
- Feature Engineering
- Data Quality Assessment
- Business Intelligence
- Dashboard Design

---

# 🚀 Key Business Insights

The final dashboard enables decision-makers to answer questions such as:

- Which European cities have the highest Airbnb prices?
- How does location affect pricing?
- Do weekends increase listing prices?
- How do room types impact revenue?
- What factors characterize premium listings?
- Which cities have the strongest Airbnb market?

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/airbnb-europe-analytics.git
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Bronze Layer

```bash
python bronze_layer/pipeline.py
```

## 4. Run the Silver Layer

```bash
python silver_layer/pipeline.py
```

## 5. Run the Gold Layer

```bash
python gold_layer/pipeline.py
```

## 6. Execute SQL Schema

Run:

```
create_schema.sql
```

inside SQL Server Management Studio.

## 7. Load the Warehouse

```bash
python gold_layer/load_data.py
```

## 8. Open the Power BI Dashboard

Open:

```
Airbnb Dashboard.pbix
```

Refresh the SQL Server connection.

---

# 🔮 Future Improvements

- Incremental data loading
- Automated scheduling
- Cloud deployment
- Docker support
- CI/CD pipeline
- Real-time Airbnb data ingestion
- Machine Learning price prediction
- Interactive web dashboard

---

# ⭐ Acknowledgements

Developed during the **Instant Summer Internship – Sprint 1**.

The project demonstrates an end-to-end modern Data Engineering workflow, from raw data ingestion to executive business intelligence reporting.