from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import mysql.connector
import datetime
from datetime import datetime


def night_rate():
    # options = webdriver.ChromeOptions()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #    driver = webdriver.Chrome(service=Service(executable_path=r"chromedriver"), options = options)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    link = "https://www.airbnb.com/rooms/769413267609103828?adults=1&category_tag=Tag%3A8538&children=0&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2023-03-13&check_out=2023-03-20&federated_search_id=ff6185bb-62ca-48f0-9c84-aeae436d6dd1&source_impression_id=p3_1678725220_Pkz%2F7ALm4dYq4g13"
    driver.get(link)
    delay = 30 # seconds until timeout

    try:
        
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#site-content > div > div:nth-child(1) > div:nth-child(3) > div > div._1s21a6e2 > div > div > div:nth-child(1) > div > div > div > div > div > div > div > div._c7v1se > div:nth-child(1) > div > span > div > span._tyxjp1')))

        print( "Page is ready!\n\n")
        driver.save_screenshot('screenshot.png')
        
    except TimeoutError:
        print( "Loading took too much time!\n\n")

    #get html source code
    html_source = driver.page_source

    #save to html file with utf-8 encoding
    with open("airbnb.html", "w", encoding="utf-8") as file:
        file.write(html_source)

    #get desired data using selectors
    soup = BeautifulSoup(html_source, 'html.parser')
    print('----------------')


    # Price Data Collect
    #    night_price_tabs = soup.find("div", {"data-plugin-in-point-id":"BOOK_IT_SIDEBAR"}).findAll("div", {"class":"_1fpuhdl"})
    night_price_tabs = soup.find("div", {"data-plugin-in-point-id":"BOOK_IT_SIDEBAR"}).findAll("div", {"class":"_1fpuhdl"})
    # print(night_price_tabs)

    per_night_final_price = 0
    cleaning_fee_final_price = 0
    service_fee_final_price = 0

    for single_night_price_tabs in night_price_tabs:
        
        print(single_night_price_tabs)
        print("''''''''''''''''/n")
        
        button_name = single_night_price_tabs.find("div", {"class":"_m6lwl6"}).string
        
        try:
            night_button_name = str(button_name).split("x")[1].split(" ")[2].strip()
            
            # print(night_button_name)
            
            if night_button_name == "night" or night_button_name == "nights":
                per_night_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()

        except:
            print("")
            # print("night price button not working")
            night_button_name = ""
            
            
        try:
            if button_name == "Cleaning fee":
                cleaning_fee_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()
        except:
            print("")
            # print("cleaning fee not found")
        
            
        
        try:
            if button_name == "Service fee":    
                service_fee_final_price = single_night_price_tabs.find("span", {"class":"_1k4xcdh"}).string.strip()
        except:
            print("")
            # print("servie fee not found")
        
        
        print("=================\n\n")
        
    print(per_night_final_price)
    print(cleaning_fee_final_price)
    print(service_fee_final_price)


night_rate()