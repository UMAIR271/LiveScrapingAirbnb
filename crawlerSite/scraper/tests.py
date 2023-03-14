from django.test import TestCase

# Create your tests here.
# print("============Reviews=======================")
    # try:
    #     reviews_result = driver.find_elements(By.CSS_SELECTOR, "span._y10azs")
    #     for i in reviews_result:
    #         reviews_text = i.find_element(By.CSS_SELECTOR, "span._1jlwy4xq").text
    #         if len(reviews_text) > 0:
    #             scraped_data["reviews"]=reviews_text
    #             print("reviews",reviews_text)
    #         else:
    #             scraped_data["reviews"]="null"
    # except:
    #     scraped_data["reviews"]="null"

    # time.sleep(10)
    # print("============all user reviews=======================")
    # try:
    #     all_user_review = driver.find_elements(By.CSS_SELECTOR, "div._162hp8xh")
    #     print(all_user_review,"all_user_reviews")
    #     for i in all_user_review:
    #         user_name = i.find_element(By.CSS_SELECTOR, "h3._14i3z6h").text
    #         print(user_name,"user_name")
    #         user_reviews = i.find_element(By.CSS_SELECTOR, "span.ll4r2nl").text
    #         print(user_reviews,"user_reviews")

    #         if len(reviews_text) > 0:
    #             scraped_data[f"user_name {user_name}"]=user_name
    #             scraped_data[f"{user_name}"]=user_reviews
    #             print("reviews",scraped_data[f"{user_name}"])
    #         else:
    #             print("reviews error")
    # except:
    #         scraped_data[f"user_name {user_name}"]="null"
    #         scraped_data[f"{user_name}"]='null'
    # time.sleep(10)
    # print("============Where will you sleep=======================")
    # try:
    #     Bedroom = driver.find_element(By.CSS_SELECTOR, "div._1a5glfg").text
    #     Bedroom_data = []
    #     if len(Bedroom) > 0:
    #         scraped_data["Bedroom"]=Bedroom
    #     else:
    #         scraped_data["Bedroom"]="null"
    # except:
    #     scraped_data["Bedroom"]="null"


    # driver.execute_script("window.scrollBy(0, 200)")
    # time.sleep(10)

# def write_cvs(data):
#         header = ['Title', 'Rating', 'Reviews','Bedroom', 'Amenities','Cleanliness','Accuracy', 'Communication','Location','Check-in','Value']
#         f_name = 'airbnb.csv'
#         with open(f_name,    'w') as data_file:
#             writer = csv.writer(data_file)
#             writer.writerow(header)
#             for row in data:
#                 writer.writerow(row)
#             data_file.close()
#         return True
