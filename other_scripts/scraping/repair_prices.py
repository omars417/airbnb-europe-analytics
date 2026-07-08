"""
Repair missing prices in the scraped Airbnb dataset.

Workflow
--------
1. Load scraped_airbnb.csv
2. Skip rows that already have a price
3. Visit each missing listing URL
4. Scrape only the price
5. Save immediately after every successful update
6. Stop gracefully if Airbnb blocks the scraper
"""

from pathlib import Path
import random
import time

import pandas as pd

from scraper import create_driver, close_driver
from parser import get_price


# ===================================
# Paths
# ===================================

CSV_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "scraped"
    / "scraped_airbnb.csv"
)


# ===================================
# Main
# ===================================

def main():

    df = pd.read_csv(CSV_PATH)

    driver = create_driver()

    try:

        total = len(df)

        for index, row in df.iterrows():

            # Skip listings that already have a price
            if pd.notna(row["price"]):
                continue

            print(f"[{index + 1}/{total}] Visiting listing...")

            driver.get(row["url"])

            # Airbnb blocked us
            if "/500" in driver.current_url:
                print("\nAirbnb blocked the scraper.")
                print("Progress has already been saved.")
                break

            # Wait for page to finish rendering
            time.sleep(random.uniform(3, 6))

            price = get_price(driver)

            print(f"Price: {price}")

            if price is not None:
                df.at[index, "price"] = price

                # Save after every successful update
                df.to_csv(
                    CSV_PATH,
                    index=False
                )

                print("Saved.")

            else:
                print("Price not found.")

            # Human-like delay before next listing
            time.sleep(random.uniform(2, 5))

        print("\nRepair finished.")

    finally:

        close_driver(driver)


# ===================================
# Entry Point
# ===================================

if __name__ == "__main__":
    main()