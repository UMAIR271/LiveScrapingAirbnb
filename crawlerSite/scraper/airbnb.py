from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time


def Scraper(url):

# Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

# Set up the Chrome driver and pass the options
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Instantiate the Chrome webdriver
    scraped_data = {}
    # Navigate to the target website
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    print("============Title=======================")
    if len(driver.title) > 0:
        scraped_data["Title"]=driver.title
    else:
        print("love")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 500)")
    print("============Rating=======================")
    rating_result = driver.find_element(By.CSS_SELECTOR, "span._17p6nbba").text
    if len(rating_result) > 0:
        scraped_data["rating"]=driver.title
        print("rating",rating_result)
    else:
        print("love")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(10)
    print("============Reviews=======================")
    reviews_result = driver.find_elements(By.CSS_SELECTOR, "span._y10azs")
    for i in reviews_result:
        reviews_text = i.find_element(By.CSS_SELECTOR, "span._1jlwy4xq").text
        if len(reviews_text) > 0:
            scraped_data["reviews"]=driver.title
            print("reviews",reviews_text)
        else:
            print("reviews error")
    time.sleep(10)
    print("============Where will you sleep=======================")
    Bedroom = driver.find_element(By.CSS_SELECTOR, "div._1a5glfg").text
    Bedroom_data = []
    if len(Bedroom) > 0:
        scraped_data["Bedroom"]=Bedroom
    driver.execute_script("window.scrollBy(0, 200)")
    time.sleep(10)


    print("=================Amenities==================")
    allAmenities = driver.find_elements(By.CSS_SELECTOR, "div._19xnuo97")
    listAllAmenities = []
    for i in allAmenities:
        amenities = i.find_element(By.CSS_SELECTOR, "div.iikjzje").text
        if len(Bedroom) > 0:
            listAllAmenities.append(amenities)
        print("Amenities", amenities)

    scraped_data["Amenities"] = amenities

    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 300)")
    print("=================All Review item==================")
    allReviewItems = driver.find_elements(By.CSS_SELECTOR, "div._1s11ltsf")
    allReviewItems_data=[]
    for i in allReviewItems:
        eachItemHeading = i.find_element(By.CSS_SELECTOR, "div._y1ba89").text
        eachItemReviews = i.find_element(By.CSS_SELECTOR, "span._4oybiu").text
        if len(eachItemReviews) > 0:
            allReviewItems_data.append(eachItemReviews)
        print(eachItemHeading, eachItemReviews)

    scraped_data["All Review item"]=allReviewItems_data


    time.sleep(10)
    print(scraped_data)
    driver.quit()
    return scraped_data

def write_cvs(data):
        header = ['Title', 'Rating', 'Reviews','Bedroom', 'Amenities','Cleanliness','Accuracy', 'Communication','Location','Check-in','Value']
        f_name = 'airbnb.csv'
        with open(f_name,    'w') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(header)
            for row in data:
                writer.writerow(row)
            data_file.close()
        return True

# write_cvs(scraped_data)



