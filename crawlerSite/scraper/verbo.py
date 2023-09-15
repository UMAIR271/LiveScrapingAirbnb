# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:10:09 2023

@author: mehed
"""


from selenium.webdriver.common.keys import Keys
import datetime
import re
from .helper import *
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.chrome.service import Service
import mysql.connector
import json

# try:
#     mydb = mysql.connector.connect(
#       host="127.0.0.1",
#       user="root",
#       passwd="",
#       database="sony_airbnb"
#     )  
# except:
       
#     mydb = mysql.connector.connect(
#       host="127.0.0.1",
#       user="airbnb",
#       passwd="airbnb@airbnb",
#       database="airbnb"
#     )  


# mycursor = mydb.cursor()
# mycursor.execute('SET NAMES utf8mb4')
# mycursor.execute("SET CHARACTER SET utf8mb4")
# mycursor.execute("SET character_set_connection=utf8mb4")





def crawler(url):

    print("enter")
    print(url)

    proxy = get_random_proxy()
    print(f"Using proxy: {proxy}")
    print("proxy_username",proxy_username)
    print("proxy_password",proxy_password)
    options = webdriver.ChromeOptions()
    proxy_auth = f"{proxy_username}:{proxy_password}"
    options.add_argument(f'--proxy-auth={proxy_auth}')
    # options.add_argument('headless')
    # options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    max_retry_count = 3  # Maximum number of retries
    retry_count = 0
   
    while retry_count < max_retry_count:
        proxy = get_random_proxy()
        print(f"Using proxy: {proxy}")
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
            driver.get(url)
            delay = 15 # seconds until timeout
            scraped_data = {}
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
                match = re.search(r'\d+', url)
                final_property_id = url.split("/www.vrbo.com/")[1].split("?")[0] 
                if match:
                    scraped_data["property_id"] = int(match.group()) 
                    print("# Property ID",final_property_id)
                else:
                    scraped_data["property_id"] = 'null' 
            except:
                scraped_data["property_id"] = 'null' 
                print("# Property ID",final_property_id)


            # today date
            try:
                today = datetime.now().date()
                if today:
                    scraped_data["scrap_date"] = today 
                    print(today)
                else:
                    scraped_data["scrap_date"] = "null" 
                    print(today)
            except:
                scraped_data["scrap_date"] = "null" 

            # current time  
            try:
                current_time = datetime.now().strftime("%H:%M:%S")
                if current_time:
                    scraped_data["current_time"] = current_time 
                    print("# current time",current_time)
                else:
                    scraped_data["current_time"] = "null" 
                    print("# current time",current_time)
            except:
                scraped_data["current_time"] = "null" 
                print("# current time",current_time)
            
            time.sleep(10)
            body = driver.find_element(By.TAG_NAME,'body')
            body.send_keys(Keys.PAGE_DOWN)

            #locations
            try:
                print("location _try")
                locations = driver.find_element(By.CSS_SELECTOR, "div.Description--location")
                locations_data=locations.text
                print(locations.text)
                words= locations_data.split(", ")
                    
                #city
                if len(words)>=4:
                    city = words[0]
                    scraped_data["city"] = words[0]
                    print("City:", words[0])

                    #property_state
                    state = words[1]
                    scraped_data["property_state"] = words[1]
                    print("State:", words[1])

                    #country
                    country = words[2]
                    scraped_data["country"] = words[2]
                    print("Country:", words[2])
                    print(locations.text)
                else:
                    scraped_data["hotel"] = words[0]
                    print("hotel:", words[0])

                    city = words[1]
                    scraped_data["city"] = words[1]
                    print("City:", words[1])

                    #property_state
                    state = words[1]
                    scraped_data["property_state"] = words[2]
                    print("State:", words[2])

                    #country
                    country = words[3]
                    scraped_data["country"] = words[3]
                    print("Country:", words[3])
                    print(locations.text)

                
            except:
                print("location _ezcept")
                time.sleep(10)
                scraped_data["city"] = "null"
                #property_state
                scraped_data["property_state"] = "null"
                #country
                scraped_data["country"] = "null"
            #building_type
            try:
                building_type = driver.find_element(By.CSS_SELECTOR, "div.property-headline")
                print(building_type, "building_type")
                if len(building_type.text) > 0:
                    scraped_data["building_type"]=building_type.text
                else:
                    print("hello")
                    scraped_data["building_type"]= "null"
            except:
                print("hello43")
                scraped_data["building_type"]= "null"
            time.sleep(3)

            #post_code
            try:
                scraped_data["post_code"]="null"
            except:
                scraped_data["post_code"]= "null"
            time.sleep(3)
            
            print("============Title=======================")
            try:
                title = driver.find_element(By.CSS_SELECTOR, "div.property-headline")
                if len(title.text) > 0:
                    scraped_data["property_title"]=title.text
                    final_title = title.text
                else:
                    scraped_data["property_title"]= "null"
            except:
                scraped_data["property_title"]= "null"
            time.sleep(10)
            body = driver.find_element(By.TAG_NAME,'body')
            body.send_keys(Keys.PAGE_UP)

            #sub_title
            try:
                scraped_data["sub_title"]="null"
            except:
                scraped_data["sub_title"]= "null"

            #description
            try:
                scraped_data["description"]="null"
            except:
                scraped_data["description"]= "null"

            print("============bed guest etc=======================")
            try:
                try:
                    li_elements = driver.find_elements(By.CSS_SELECTOR,".four-pack > li")
                    # house_type = ""
                    bedrooms = ""
                    beds = ""
                    sleeps = ""
                    bathrooms = ""
                    baths = ""
                    # kitchen = False
                    # patio = False

                    # Loop through the li elements and extract the data
                    for li in li_elements:
                        print("hello")
                        text = li.text
                        print(text,"loop iteration!\n\n")
                        if "House" in text:
                            pass
                        try:
                            if "bedrooms" in text or "bedroom" in text:
                                bedrooms = text
                                bedrooms = int(bedrooms.split()[0])
                                scraped_data["bedrooms"] = bedrooms
                                try:
                                    beds = li.find_element(By.CSS_SELECTOR, ".four-pack__detail-item:nth-of-type(1)").text
                                    beds = int(beds.split()[0])
                                    scraped_data["beds"] = beds
                                except:
                                    scraped_data["beds"] = "null"
                                try:
                                    print("enter the sleep\n\n")
                                    sleeps = li.find_element(By.CSS_SELECTOR, ".four-pack__detail-item:nth-of-type(2)").text
                                    sleeps = int(sleeps.split()[0])
                                    scraped_data["sleeps"] = sleeps
                                except:
                                    scraped_data["sleeps"] = "null"
                        except:
                            scraped_data["bedrooms"] = "null"
                        try:
                            print("enter the bathroom==================================\n\n")
                            if "bathrooms" in text or "bathroom" in text:
                                print("bathrooms\n\n",text)
                                bathrooms = text
                                bath_number = int(bathrooms.split()[0])
                                print(bath_number, "==bath==\n\n")
                                scraped_data["bathrooms"] = bath_number
                            else:
                                scraped_data["baths"] = "null"
                        except:
                            scraped_data["bathrooms"] = "null"
                    print("Bedrooms:", bedrooms)
                    print("Beds:", beds)
                    print("Sleeps:", sleeps)
                    print("Bathrooms:", bathrooms)
                    guests = "null"

                except:
                    scraped_data["guests"] = "null"
            except:
                    scraped_data["guests"] = "null"
                    scraped_data["bedrooms"] = "null"
                    scraped_data["beds"] = "null"
                    scraped_data["baths"] = "null"
            time.sleep(10)
            driver.execute_script("window.scrollBy(0, 500)")

            #night_rate
            try:
                night_rate=driver.find_element(By.CSS_SELECTOR,"span.rental-price__amount").text
                scraped_data["night_rate"] = night_rate   
                
            except:
                scraped_data["night_rate"] = "null"

            #cleaing
            try:
                cleaning_fee = driver.find_element(By.CSS_SELECTOR, "div._18x0pkv")
                print(cleaning_fee)
            except:
                scraped_data["cleaning_fee"] = "null"

            #service
            try:
                cleaning_fee = driver.find_element(By.CSS_SELECTOR, "div._18x0pkv")
                print(cleaning_fee)
            except:
                scraped_data["service_fee"] = "null"


            # currency   

            scraped_data["currency"] = "USD"

            #image_links
            try:
                image_links = driver.find_elements(By.CSS_SELECTOR,'img.photo-grid__photo')
                if len(image_links) > 0:
                    all_image_links = []
                    for link in image_links:
                        all_image_links.append(link.get_attribute('src'))
                        print(link.get_attribute('src'))
                    scraped_data["property_photos"] = all_image_links
                    
                else:
                    scraped_data["property_photos"] = "null"
                
            except:
                scraped_data["property_photos"] = "null"


            #single_room
            try:
                scraped_data["single_room"] = url
                
            except:
                scraped_data["single_room"] = "null" 

            #source
            # scraped_data["source"] = "vrbo"
            # scraped_data["status"] = "1"
            # sql2 = "INSERT INTO  rooms (property_id, scrap_date, scrap_time, building_type, city, property_state, country, property_title, guest, beds, bedrooms, bathrooms, night_rate, cleaning_fee, property_photos, single_room) VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
            # val2 = (final_property_id, today, datetime.now().strftime("%H:%M:%S"), building_type, city, state, country, final_title, guests, beds, bedrooms, baths, "", "", json.dumps(all_image_links), url)
            # mycursor.execute(sql2, val2)
            # mydb.commit()
            print("\nInsert successfully\n")
            time.sleep(10)
            print(scraped_data)
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
        