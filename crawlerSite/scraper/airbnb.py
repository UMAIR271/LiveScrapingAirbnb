# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:10:09 2023

@author: mehed
"""

from selenium.webdriver.common.keys import Keys
import time
import datetime
import json
from datetime import datetime
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .helper import *
db_host = '34.23.87.242'
db_port = '3306'
db_name = 'cleanster-logs'
db_user = 'airbnb_root'
db_password = '7BQ+NLokL<L,x@+r'

try:
    mydb = mysql.connector.connect(
        user = db_user,
        password=db_password,
        host= db_host,
        port = db_port,
        database=db_name
    )  
except:
       
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="airbnb",
      passwd="airbnb@airbnb",
      database="airbnb"
    )  


mycursor = mydb.cursor()
mycursor.execute('SET NAMES utf8mb4')
mycursor.execute("SET CHARACTER SET utf8mb4")
mycursor.execute("SET character_set_connection=utf8mb4")



def Scraper(url):
    print("proxy_username",proxy_username)
    print("proxy_password",proxy_password)
    options = webdriver.ChromeOptions()
    proxy_auth = f"{proxy_username}:{proxy_password}"
    options.add_argument(f'--proxy-auth={proxy_auth}')
    options.add_argument('headless')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    max_retry_count = 3  # Maximum number of retries
    retry_count = 0

    while retry_count < max_retry_count:
        proxy = get_random_proxy()
        print(f"Using proxy: {proxy}")
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
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
                final_property_id = url.split("/rooms/")[1].split("?")[0] 
                if final_property_id:
                    scraped_data["property_id"] = final_property_id 
                    print("# Property ID",final_property_id)
                    time.sleep(5)
                else:
                    scraped_data["property_id"] = 'null' 
                    print("# Property ID",final_property_id)
            except:
                scraped_data["property_id"] = 'null' 


            #today date
            today = datetime.now().date()
            scraped_data = {"scrap_date": today, "current_time": datetime.now().strftime("%H:%M:%S")}
            body = driver.find_element(By.TAG_NAME,'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(20)
            #locations
            class_names_to_check_location = ["_8x4fjw", "_152qbzi","_leqb4t","_9xiloll"]
            for class_name in class_names_to_check_location:
                try:
                    location_element = driver.find_element(By.CSS_SELECTOR, f"span.{class_name}, div.{class_name}")
                    
                    # If the element is found, extract data
                    location_text = location_element.text
                    city, state, country = location_text.split(", ")
                    scraped_data["city"] = city
                    scraped_data["property_state"] = state
                    scraped_data["country"] = country
                    
                    # Exit the loop since we found a valid location element
                    break
                except:
                    # If the element is not found, continue to the next class name
                    scraped_data["city"] = 'null'
                    scraped_data["property_state"] = 'null'
                    scraped_data["country"] = 'null'

            all_image_links=[]
            class_name_to_check_building_type = ['_1xxgv6l','_1n81at5']
            for class_name in class_name_to_check_building_type:
                try:
                    building_type = driver.find_elements(By.CSS_SELECTOR, f"div.{class_name}, span.{class_name}")
                    if building_type:
                        scraped_data["building_type"] = building_type[0].text
                except:
                    scraped_data["building_type"] = "null"

            # post code
            scraped_data["post_code"] = "null"

            # title
            class_name_to_check_property_title = ['_1xxgv6l','_8lgpy8']
            for class_name in class_name_to_check_property_title:
                try:

                    title = driver.find_elements(By.CSS_SELECTOR, f"div.{class_name}")
                    if title:
                        scraped_data["property_title"] = title[0].text
                except:
                        scraped_data["property_title"] = "null"

            # scroll up
            body.send_keys(Keys.PAGE_UP)

            # sub title
            scraped_data["sub_title"] = "null"

            # description
            try:
                list_of_description=driver.find_element(By.CSS_SELECTOR, 'div[style="line-height: 24px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 6; -webkit-box-orient: vertical;"]')
                if list_of_description:
                    scraped_data["description"] = list_of_description.text
            except:
                scraped_data["description"] = "null"
            
            print("============bed guest etc=======================")
            try:
                try:
                    guests = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(1) span:nth-child(1)').text
                    guests = int(guests.split()[0])
                    scraped_data["guests"] = guests
                    print('Guests:', guests)
                except:
                    scraped_data["guests"] = "null"

                try:
                    bedrooms = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(2) span:nth-child(2)').text
                    bedrooms = int(bedrooms.split()[0])
                    scraped_data["bedrooms"] = bedrooms
                    print('Bedrooms:', bedrooms)
                except:
                    scraped_data["bedrooms"] = "null"
                
                try:
                    beds = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(3) span:nth-child(2)').text
                    beds = int(beds.split()[0])
                    scraped_data["beds"] = beds
                    print('Beds:', beds)
                except:
                    scraped_data["beds"] = "null"
                
                try:
                    baths = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(4) span:nth-child(2)').text
                    baths = int(baths.split()[0])
                    scraped_data["baths"] = baths
                    print('Baths:', baths)
                except:
                    scraped_data["baths"] = "null"
            except:
                    scraped_data["guests"] = "null"
                    scraped_data["bedrooms"] = "null"
                    scraped_data["beds"] = "null"
                    scraped_data["baths"] = "null"
            time.sleep(10)
            driver.execute_script("window.scrollBy(0, 500)")

            #night_rate
            try:
                night_price_element = driver.find_element(By.CSS_SELECTOR, 'div._ati8ih span._r1nvod:nth-child(2)')
                if night_price_element:
                    scraped_data["night_rate"] = night_price_element.text
            except:
                scraped_data["night_rate"] = "null"

            #cleaing
            try:
                cleaning_fee = driver.find_element(By.CSS_SELECTOR, "div._1k4xcdh:nth-child(2)")
                scraped_data["cleaning_fee"] = cleaning_fee
            except:
                scraped_data["cleaning_fee"] = "null"
                

            # currency   

            scraped_data["currency"] = "USD"

            #image_links
            try:
                image_links = driver.find_elements(By.CSS_SELECTOR,'img._6tbg2q')
                if len(image_links) > 0:
                    
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

            final_property_type = "null"
            #source
            scraped_data["source"] = "airbnb"
            scraped_data["status"] = "1"


            mycursor.execute("SELECT property_id FROM rooms WHERE property_id = '" + final_property_id + "' AND  scrap_date = '" + str(today) + "'")
            myresult3 = mycursor.fetchall()      
            existingRowCount3 = len(myresult3)
            print(myresult3)
            print("Total Duplicate Found: " + str(existingRowCount3))
            if existingRowCount3 >= 1:
                print("Allready Exists")
                pass
            
            else: 
                sql2 = "INSERT INTO  rooms (property_id, scrap_date, scrap_time, building_type, city, property_state, country, property_title, guest, beds, bedrooms, bathrooms, night_rate, cleaning_fee, property_photos, single_room) VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
                val2 = (final_property_id, today, datetime.now().strftime("%H:%M:%S"), final_property_type, city, state, country, final_title, guests, beds, bedrooms, baths, "", "", json.dumps(all_image_links), url)
                mycursor.execute(sql2, val2)
                mydb.commit()
                print("\nInsert successfully\n")
            print(scraped_data)
            mydb.close()
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