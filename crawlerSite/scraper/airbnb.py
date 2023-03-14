from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import datetime
from bs4 import BeautifulSoup


def Scraper(url):
    try:
        print("hello")
        response = url
        return response
    # # Set up Chrome options for headless browsing
    #     chrome_options = Options()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--disable-gpu')

    # # Set up the Chrome driver and pass the options
    #     driver = webdriver.Chrome(chrome_options=chrome_options)
    #     # driver = webdriver.Chrome()


    #     # Instantiate the Chrome webdriver
    #     scraped_data = {}

    #     # Navigate to the target website

    #     driver.get(url)
    #     delay = 15
    #     # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.l1li2ovm dir dir-ltr")))
    #     wait = WebDriverWait(driver, delay)
    #     print(wait, "Page is ready!\n\n")
    #     #get html source code
    #     html_source = driver.page_source

    #     #save to html file with utf-8 encoding
    #     with open("airbnb.html", "w", encoding="utf-8") as file:
    #         file.write(html_source)

    #     #get desired data using selectors
    #     soup = BeautifulSoup(html_source, 'html.parser')
    #     print('----------------')


    #     # Property ID
    #     try:
    #         final_property_id = url.split("/rooms/")[1].split("?")[0] 
    #         if final_property_id:
    #             scraped_data["property_id"] = final_property_id 
    #             print("# Property ID",final_property_id)
    #         else:
    #             scraped_data["property_id"] = 'null' 
    #             print("# Property ID",final_property_id)
    #     except:
    #         scraped_data["property_id"] = 'null' 


    #     # today date
    #     try:
    #         today = datetime.now().date()
    #         if today:
    #             scraped_data["scrap_date"] = today 
    #             print(today)
    #         else:
    #             scraped_data["scrap_date"] = "null" 
    #             print(today)
    #     except:
    #         scraped_data["scrap_date"] = "null" 

    #     # current time  
    #     try:
    #         current_time = datetime.now().strftime("%H:%M:%S")
    #         if current_time:
    #             scraped_data["current_time"] = current_time 
    #             print("# current time",current_time)
    #         else:
    #             scraped_data["current_time"] = "null" 
    #             print("# current time",current_time)
    #     except:
    #         scraped_data["current_time"] = "null" 
    #         print("# current time",current_time)
        
    #     time.sleep(10)
    #     body = driver.find_element(By.TAG_NAME,'body')
    #     body.send_keys(Keys.PAGE_DOWN)

    #     #locations
    #     try:
    #         print("location _try")
    #         locations = driver.find_element(By.CSS_SELECTOR, "div._9ns6hl")
    #         locations_data=locations.text
    #         print(locations.text)
    #         city, state, country = locations_data.split(", ")
                
    #         #city
    #         scraped_data["city"] = city
    #         print("City:", city)

    #         #property_state
    #         scraped_data["property_state"] = state
    #         print("State:", state)

    #         #country
    #         scraped_data["country"] = country
    #         print("Country:", country)
    #         print(locations.text)
    #     except:
    #         print("location _ezcept")
    #         time.sleep(10)
    #         driver.execute_script("window.scrollBy(0, 700)")
    #         locations = driver.find_element(By.CSS_SELECTOR, "div._152qbzi")
    #         locations_data=locations.text
    #         print(locations.text)
    #         city, state, country = locations_data.split(", ")
                
    #         #city
    #         scraped_data["city"] = city
    #         print("City:", city)

    #         #property_state
    #         scraped_data["property_state"] = state
    #         print("State:", state)

    #         #country
    #         scraped_data["country"] = country
    #         print("Country:", country)
    #         print(locations.text)

    #     #building_type
    #     try:
    #         building_type = driver.find_element(By.CSS_SELECTOR, "div._1n81at5")
    #         if len(building_type.text) > 0:
    #             scraped_data["building_type"]=building_type.text
    #         else:
    #             scraped_data["building_type"]= "null"
    #     except:
    #         scraped_data["building_type"]= "null"
    #     time.sleep(3)

    #     #post_code
    #     try:
    #         scraped_data["post_code"]="null"
    #     except:
    #         scraped_data["post_code"]= "null"
    #     time.sleep(3)
        
    #     print("============Title=======================")
    #     try:
    #         title = driver.find_element(By.CSS_SELECTOR, "div._cv5qq4")
    #         if len(title.text) > 0:
    #             scraped_data["property_title"]=title.text
    #         else:
    #             scraped_data["property_title"]= "null"
    #     except:
    #         scraped_data["property_title"]= "null"
    #     time.sleep(10)
    #     body = driver.find_element(By.TAG_NAME,'body')
    #     body.send_keys(Keys.PAGE_UP)

    #     #sub_title
    #     try:
    #         scraped_data["sub_title"]="null"
    #     except:
    #         scraped_data["sub_title"]= "null"

    #     #description
    #     try:
    #         scraped_data["description"]="null"
    #     except:
    #         scraped_data["description"]= "null"

    #     print("============bed guest etc=======================")
    #     try:
    #         try:
    #             guests = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(1) span:nth-child(1)').text
    #             guests = int(guests.split()[0])
    #             scraped_data["guests"] = guests
    #             print('Guests:', guests)
    #         except:
    #             scraped_data["guests"] = "null"

    #         try:
    #             bedrooms = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(2) span:nth-child(2)').text
    #             bedrooms = int(bedrooms.split()[0])
    #             scraped_data["bedrooms"] = bedrooms
    #             print('Bedrooms:', bedrooms)
    #         except:
    #             scraped_data["bedrooms"] = "null"
            
    #         try:
    #             beds = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(3) span:nth-child(2)').text
    #             beds = int(beds.split()[0])
    #             scraped_data["beds"] = beds
    #             print('Beds:', beds)
    #         except:
    #             scraped_data["beds"] = "null"
            
    #         try:
    #             baths = driver.find_element(By.CSS_SELECTOR,'div._tqmy57 li:nth-child(4) span:nth-child(2)').text
    #             baths = int(baths.split()[0])
    #             scraped_data["baths"] = baths
    #             print('Baths:', baths)
    #         except:
    #             scraped_data["baths"] = "null"
    #     except:
    #             scraped_data["guests"] = "null"
    #             scraped_data["bedrooms"] = "null"
    #             scraped_data["beds"] = "null"
    #             scraped_data["baths"] = "null"
    #     time.sleep(10)
    #     driver.execute_script("window.scrollBy(0, 500)")

    #     #night_rate
    #     try:
                    
    #         # Price Data Collect
    #         #    night_price_tabs = soup.find("div", {"data-plugin-in-point-id":"BOOK_IT_SIDEBAR"}).findAll("div", {"class":"_1fpuhdl"})
    #         night_price_tabs = soup.find("div", {"data-plugin-in-point-id":"BOOK_IT_SIDEBAR"}).findAll("div", {"class":"_1fpuhdl"})
    #         # print(night_price_tabs)
            
    #         per_night_final_price = 0
    #         cleaning_fee_final_price = 0
    #         service_fee_final_price = 0
    #         print(night_price_tabs,"night_price_tabs")
    #         for single_night_price_tabs in night_price_tabs:
                
    #             print(single_night_price_tabs)
    #             print("''''''''''''''''/n")
                
    #             button_name = single_night_price_tabs.find("div", {"class":"_m6lwl6"}).string
                
    #             try:
    #                 night_button_name = str(button_name).split("x")[1].split(" ")[2].strip()
                    
    #                 # print(night_button_name)
                    
    #                 if night_button_name == "night" or night_button_name == "nights":
    #                     per_night_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()
        
    #             except:
    #                 print("")
    #                 # print("night price button not working")
    #                 night_button_name = ""
                    
                    
    #             try:
    #                 if button_name == "Cleaning fee":
    #                     cleaning_fee_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()
    #             except:
    #                 print("")
    #                 # print("cleaning fee not found")
                
                    
                
    #             try:
    #                 if button_name == "Service fee":    
    #                     service_fee_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()
    #             except:
    #                 print("")
    #                 # print("servie fee not found")
                
                
    #             print("=================\n\n")
                
    #         print("per_night_final_price",per_night_final_price)
    #         print("cleaning_fee_final_price",cleaning_fee_final_price)
    #         print("service_fee_final_price",service_fee_final_price)
            

    #     except:
    #         scraped_data["night_rate"] = "null"

    #     #cleaing
    #     try:
    #         cleaning_fee = driver.find_element(By.CSS_SELECTOR, "div._18x0pkv")
    #         print(cleaning_fee)
    #     except:
    #         print("not found")

    #     # currency   

    #     scraped_data["currency"] = "USD"

    #     #image_links
    #     try:
    #         image_links = driver.find_elements(By.CSS_SELECTOR,'img._6tbg2q')
    #         if len(image_links) > 0:
    #             all_image_links = []
    #             for link in image_links:
    #                 all_image_links.append(link.get_attribute('src'))
    #                 print(link.get_attribute('src'))
    #             scraped_data["property_photos"] = all_image_links
                
    #         else:
    #             scraped_data["property_photos"] = "null"
            
    #     except:
    #         scraped_data["property_photos"] = "null"


    #     #single_room
    #     try:
    #         scraped_data["single_room"] = url
            
    #     except:
    #         scraped_data["single_room"] = "null" 

    #     #source
    #     scraped_data["source"] = "airbnb"
    #     scraped_data["status"] = "1"
    #     time.sleep(10)
    #     print(scraped_data)
    #     driver.quit()
    #     return scraped_data
    except:
        response = "Loading took too much time!\n\n"
        return response


    # write_cvs(scraped_data)



