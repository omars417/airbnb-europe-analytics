"""
The project includes an independent Selenium-based scraping pipeline that collects current Airbnb listing information
for selected cities. The scraped dataset is generated separately from the historical dataset and 
is intended for exploratory analysis and comparison rather than direct row-level enrichment.

To improve consistency across cities, scraping was limited to Entire Home/Apt listings with two bedrooms.
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

SCRAPED_DATA_PATH = PROJECT_ROOT / "data" / "scraped"

SCRAPED_DATA_PATH.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = SCRAPED_DATA_PATH / "airbnb_scraped.csv"

BASE_URL = "https://www.airbnb.com/s"

MAX_LISTINGS_PER_CITY = 30

HEADLESS = False #Chrome behaves like a normal browser You can watch everything Selenium is doing. HEADLESS = True Chrome becomes invisible.

PAGE_LOAD_TIMEOUT = 30 #Wait at most 30 seconds.

IMPLICIT_WAIT = 10 # when a site loads a button may still not appear Whenever you search for an element...keep trying for up to 10 seconds.