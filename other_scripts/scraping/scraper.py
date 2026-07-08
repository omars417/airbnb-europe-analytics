"""
Scraper Module

Handles browser automation using Selenium.

Responsibilities:
- Create browser instance
- Navigate Airbnb
- Build search URLs
- Collect listing URLs

Does NOT:
- Parse listing details
- Save data
- Create DataFrames
"""

from urllib.parse import quote

from selenium import webdriver #Selenium's interface to control the browser.
from selenium.webdriver.chrome.options import Options #lets us configure Chrome before it starts. ex window size With it: We customize Chrome before opening it. else default chrome settings
from selenium.webdriver.common.by import By #locate elements Instead of driver.find_element("css selector", ...) we use the safer driver.find_element(By.CSS_SELECTOR, ...)
import time #We're going to pause briefly after scrolling. ecause React needs time to render the newly loaded cards.

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from scraper_config import (
    BASE_URL,
    HEADLESS,
    IMPLICIT_WAIT,
    PAGE_LOAD_TIMEOUT,
    MAX_LISTINGS_PER_CITY,
)

def create_driver() -> webdriver.Chrome:
    """
    Create and configure a Chrome WebDriver.
    """

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled") #Chrome normally tells websites: I'm being controlled by Selenium Some websites detect this. This flag hides some automation indicators.
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.implicitly_wait(IMPLICIT_WAIT)

    return driver

def build_search_url(city: str) -> str:
    """
    Build an Airbnb search URL for a city.
    """
    #Why quote()? city = "New York" Without encoding: https://www.airbnb.com/s/New York/homes Invalid URL. With quote New%20York
    city = quote(city)

    return f"{BASE_URL}/{city}/homes"


def collect_listing_urls(driver,city: str) -> list[str]:
    """
    Collect Airbnb listing URLs for a city.
    """

    url = build_search_url(city)

    driver.get(url) #This is equivalent to typing the URL into Chrome.

    links = set()#A set automatically removes duplicates

    previous_height = 0

    while len(links) < MAX_LISTINGS_PER_CITY:

        # Collect every rooms hyperlink
        elements = driver.find_elements(
        By.CSS_SELECTOR,
        'a[href*="/rooms/"]'
        )

        for element in elements:

            try:
                href = element.get_attribute("href")#<a href="https://www.airbnb.com/rooms/12345">

                if href and "/rooms/" in href:
                    links.add(href)

            except StaleElementReferenceException:
                continue

        # Stop if enough listings were collected
        if len(links) >= MAX_LISTINGS_PER_CITY:
            break

        # Scroll to the bottom execute_script executes java script
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(3) #after scroll wait until react loads

        # Check if new content loaded
        current_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if current_height == previous_height:
            break

        previous_height = current_height

    return list(links)[:MAX_LISTINGS_PER_CITY] #slice keep only the first 50 links

def close_driver(driver) -> None:
    """
    Close the browser.
    """

    driver.quit() # unlike close() quit closes all tabs