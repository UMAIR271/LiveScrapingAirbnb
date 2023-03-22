# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:10:09 2023

@author: mehed
"""

# from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
import datetime
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import mysql.connector
import json

try:
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="",
      database="sony_airbnb"
    )  
except:
       
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="airbnb",
      passwd="airbnb@airbnb",
      database="airbnb"
    )  




def crawler(url):

    print("enter")
    print(url)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
#    driver = webdriver.Chrome(service=Service(executable_path=r"chromedriver"), options = options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
    
    # link = "https://www.airbnb.com/rooms/36343724?category_tag=Tag%3A8225&check_in=2022-12-10&check_out=2022-12-11&previous_page_section_name=1000"
    
    driver.get(url)
    delay = 15 # seconds until timeout
    
    # driver = webdriver.Chrome()


    # Instantiate the Chrome webdriver
    scraped_data = {}

    # Navigate to the target website
    

    # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.l1li2ovm dir dir-ltr")))
    
    wait = WebDriverWait(driver, delay)
    # print(wait, "Page is ready!\n\n")
    #get html source code


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

            scraped_data["city"] = words[0]
            print("City:", words[0])

            #property_state
            scraped_data["property_state"] = words[1]
            print("State:", words[1])

            #country
            scraped_data["country"] = words[2]
            print("Country:", words[2])
            print(locations.text)
        else:
            scraped_data["hotel"] = words[0]
            print("hotel:", words[0])

            scraped_data["city"] = words[1]
            print("City:", words[1])

            #property_state
            scraped_data["property_state"] = words[2]
            print("State:", words[2])

            #country
            scraped_data["country"] = words[3]
            print("Country:", words[3])
            print(locations.text)

        
    except:
        print("location _ezcept")
        time.sleep(10)
        # driver.execute_script("window.scrollBy(0, 700)")
        # locations = driver.find_element(By.CSS_SELECTOR, "div._152qbzi")
        # locations_data=locations.text
        # print(locations.text)
        # city, state, country = locations_data.split(", ")
            
        #city

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
    scraped_data["source"] = "vrbo"
    scraped_data["status"] = "1"
    time.sleep(10)
    print(scraped_data)
    driver.quit()
    return scraped_data


# Scraper("https://www.airbnb.ca/rooms/676499889269811829?adults=1&category_tag=Tag%3A8662&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-01-20&check_out=2023-01-25&federated_search_id=ec4bcd8f-5449-44d8-ae9f-c1e7762ffd5a&source_impression_id=p3_1678806666_si7KMqChQusbS90x")
    # write_cvs(scraped_data)