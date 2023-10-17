# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:10:09 2023

@author: mehed
"""

from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime
from selenium import webdriver
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver as wiredriver

from .helper import *
def Scraper(url):
    db_host = '34.23.87.242'
    db_port = '3306'
    db_name = 'cleanster-logs'
    db_user = 'airbnb_root'
    db_password = '7BQ+NLokL<L,x@+r'
    print("proxy_username",proxy_username)
    print("proxy_password",proxy_password)
    chrome_options = Options()

    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-setuid-sandbox") 
    chrome_options.add_argument("--remote-debugging	-port=9222")  # this
    chrome_options.add_argument("--disable-dev-shm-using") 
    chrome_options.add_argument("--disable-extensions") 
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("disable-infobars")

    # Set proxy settings
    
    max_retry_count = 3  # Maximum number of retries
    retry_count = 0

    while retry_count < max_retry_count:
        proxy = get_random_proxy()
        print(f"Using proxy: {proxy}")
        proxy_options = {
        'proxy': {
            'https': f'https://yhboqpqa:vwxtikz2tphj@{proxy}'
        }
    }
        try:
            driver = wiredriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            seleniumwire_options=proxy_options,
            options=chrome_options
            )
            print(driver)
            driver.get(url)
            delay = 30 # seconds until timeout
            
            # driver = webdriver.Chrome()


            # Instantiate the Chrome webdriver
            scraped_data = {}

            # Navigate to the target website 
            wait = WebDriverWait(driver, delay)
            doc_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

            # Calculate the scroll distances for each part
            half_page_scroll = doc_height // 2
            three_quarter_page_scroll = doc_height * 3 // 4
            full_page_scroll = doc_height

            # Scroll down half page
            driver.execute_script(f"window.scrollTo(0, {half_page_scroll});")

            # Wait for 5 seconds
            time.sleep(5)

            # Scroll down 75 percent
            driver.execute_script(f"window.scrollTo(0, {three_quarter_page_scroll});")

            # Wait for 5 seconds
            time.sleep(5)

            # Scroll down full page
            driver.execute_script(f"window.scrollTo(0, {full_page_scroll});")

            # Wait for 10 seconds
            time.sleep(10)
            # Property ID

            try:
    # Wait for the title element to be present
                
                title_element = driver.find_element(By.CSS_SELECTOR, "h1.uitk-heading-2")
                
                # Find the title element
                if title_element:
                    property_title = title_element.text.strip()
                    print("Property Title:", property_title)
                else:
                    print("Property title not found.")
            except Exception as e:
                print("Error:", str(e))

            driver.quit()
            return scraped_data
        except Exception as e:
            print(f"An error occurred: {e}")
            retry_count += 1
            print(f"Retrying with a different proxy (attempt {retry_count}/{max_retry_count})")
        finally:
            if 'driver' in locals():
                driver.quit()

    print(f"Failed to scrape data after {max_retry_count} attempts.")
    return []
        
    



# Scraper("https://www.airbnb.com/rooms/755137040389728919?adults=1&category_tag=Tag%3A8102&children=0&infants=0&pets=0&check_in=2023-04-15&check_out=2023-04-20&federated_search_id=d120bd08-ed2b-4c79-8e1f-3fcc665546eb&source_impression_id=p3_1679502419_EarSIHPCIlX%2FRFLf")