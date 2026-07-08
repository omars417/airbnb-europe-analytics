"""
Parser Module

Extracts information from an Airbnb listing page.

Responsibilities:
- Visit listing page
- Extract listing attributes
- Return structured data

Does NOT:
- Navigate search results
- Save CSV files
- Manage Selenium driver
"""

import re #Regular expressions help us extract numbers from text. ex ★ 4.92 · 387 reviews  re: rating = 4.92  reviews = 387 or 2400$ to 2400

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException #Not every listing has all attributes instead of crashing we'll return None
from selenium.common.exceptions import TimeoutException
  

def safe_find_text(driver, by, value):
    """
    Return element text or None if not found.
    """

    try:
        return driver.find_element(by,value).text.strip()

    except NoSuchElementException:
        return None
    
def get_title(driver):
    """
    Extract listing title.
    """

    return safe_find_text(driver,By.TAG_NAME,"h1")

def get_price(driver):
    """
    Extract listing price.
    """
    price = safe_find_text(
        driver,
        By.CSS_SELECTOR,
        '[data-xray-jira-component="Guest: Price Display: P3"] button span'
    )

    print(f"Raw price: {price}")

    if price is None:
        return None

    numbers = re.sub(r"[^\d]", "", price)

    if not numbers:
        return None

    print(f"Parsed price: {numbers}")

    return int(numbers)

def get_rating(driver):
    """
    Extract Airbnb rating.
    """

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-testid="pdp-reviews-highlight-banner-host-rating"]'
    )

    print(f"Found {len(elements)} rating elements")

    if len(elements) == 0:
        print(f"No rating found on: {driver.current_url}")
        return None

    for i, element in enumerate(elements):
        print(f"Rating {i}: {repr(element.text)}")

    return None


def get_reviews(driver):
    """
    Extract review count.
    """

    reviews = safe_find_text(
        driver,
        By.CSS_SELECTOR,
        '[data-testid="pdp-reviews-highlight-banner-host-review"]'
    )

    if reviews is None:
        return None

    numbers = re.sub(r"[^\d]", "", reviews)

    if not numbers:
        return None

    return int(numbers)

def get_superhost(driver):
    """
    Return whether the host is a Superhost.
    """

    return "Superhost" in driver.page_source #Why not Selenium  Because we only need t/f  Searching the HTML is simpler.


def get_guest_favorite(driver):
    """
    Return whether the listing is Guest Favorite.
    """

    return len(driver.find_elements(By.CSS_SELECTOR,'[aria-label="Guest Favorite Listing."]')) > 0
"""
Why find_elements()?
Remember find_element()
If nothing exists
↓
Exception.

find_elements()

If nothing exists
↓
[]
Empty list. No exception.

Why
> 0  Suppose find_elements(...) returns [element] Length 1
↓
1 > 0 True

Suppose []
↓
Length 0
↓
0 > 0
False
"""

def parse_listing(driver, url):
    try:
        driver.get(url)

        return {
            "url": url,
            "title": get_title(driver),
            "price": get_price(driver),
            "rating": get_rating(driver),
            "reviews": get_reviews(driver),
            "superhost": get_superhost(driver),
            "guest_favorite": get_guest_favorite(driver),
        }

    except Exception as e:
        print(e)
        raise
        return {
            "url": url,
            "title": None,
            "price": None,
            "rating": None,
            "reviews": None,
            "superhost": False,
            "guest_favorite": False,
        }