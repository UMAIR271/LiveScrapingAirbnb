import random
from datetime import datetime
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

proxies = [
    "216.173.109.24:6255",
    "38.170.176.60:5455",
    "23.247.112.133:6789",
    "45.251.63.16:6088",
    "184.174.28.83:5098",
    "45.131.95.226:5890",
    "216.173.109.24:6255",
    "38.170.176.60:5455",
    "23.247.112.133:6789",
    "45.251.63.16:6088",
    "184.174.28.83:5098",
    "45.131.95.226:5890",
    "5.157.130.10:8014",
    "38.154.197.130:6796",
    "45.43.70.233:6520",
    "134.73.99.98:5790",
    "171.22.250.21:6140",
    "198.23.239.140:6546",
    "194.39.32.238:6535",
    "38.170.189.174:9740",
    "193.148.92.104:6031",
    "192.186.172.222:9222",
    "45.192.136.152:5446" ,
    "45.43.184.132:5806",
    "185.242.93.53:8393",
    "64.137.31.95:6709",
    "104.239.3.123:6083",
    "104.250.203.159:5849",
    "45.43.189.11:5682",
    "37.35.40.68:8158",
    "45.192.150.132:6315",
    "64.137.121.228:6483",
    "104.249.61.155:6810",
    "45.61.123.238:5917",
    "64.137.75.129:6049",
    "103.3.227.187:6740",
    "154.85.124.95:5956",
    "161.123.65.129:6838",
    "173.214.177.132:5823",
    "103.3.226.20:6296",
    "103.37.180.20:6414",
    "198.105.100.198:6449",
    "64.137.65.53:6732",
    "64.137.106.201:6694",
    "157.52.233.70:5697",
    "45.192.146.62:6073",
    "64.137.93.117:6574",
    "64.137.42.35:5080",
    "157.52.174.3:6212",
    "45.43.64.27:6285",
    "64.43.91.148:6919",
    "67.227.119.49:6378",
    "45.43.185.86:6092",
    "45.43.190.41:6559",
    "104.222.185.162:5725",
    "104.233.13.47:6042",
    "134.73.65.16:6568",
    "45.61.127.127:6066",
    "206.41.179.21:5697",
    "136.0.207.235:6184",
    "104.223.223.142:6727",
    "104.250.205.194:5941",
    "5.154.254.254:5265",
    "45.131.101.34:6301",
    "45.61.116.66:6744",
    "104.238.36.222:6229",
    "103.99.33.62:6057",
    "45.41.162.205:6842",
    "198.23.147.252:5267",
    "45.192.152.135:6073",
    "198.46.202.20:5300",
    "198.23.128.216:5844",
    "45.131.101.144:6411",
    "154.92.124.52:5080",
    "154.194.8.36:5567",
    "161.123.33.89:6112",
    "38.170.176.48:5443",
    "104.249.61.203:6858",
    "104.239.43.189:5917",
    "104.223.227.161:6684",
    "198.105.101.158:5787",
    "45.41.162.76:6713",
    "134.73.128.147:6105",
    "91.246.195.188:6957",
    "166.88.195.45:6050",
    "192.186.172.91:9091",
    "104.223.157.56:6295",
    "192.198.126.9:7052",
    "38.154.206.123:9614",
    "64.137.49.76:6617",
    "107.181.143.227:6358",
    "192.241.118.31:8598",
    "206.41.179.134:5810",
    "104.239.41.151:6506",
    "64.137.121.149:6404",
    "107.181.128.147:5159",
    "134.73.104.17:6651",
    "154.30.242.63:9457",
    "45.61.116.35:6713",
    "198.46.137.30:6234",
    "43.245.117.147:5731",
    "93.120.32.35:9219",
    "157.52.187.66:6006",
]


proxy_username = "yhboqpqa"
proxy_password = "vwxtikz2tphj"


def get_random_proxy():
    return random.choice(proxies)


def create_driver_with_proxy():
    max_retry_attempts = 3  # Adjust this value as needed

    for _ in range(max_retry_attempts):
        proxy = get_random_proxy()
        print(f"Using proxy: {proxy}")

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')

        proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy}"
        proxy_object = webdriver.Proxy()
        proxy_object.http_proxy = proxy_url
        proxy_object.ssl_proxy = proxy_url
        chrome_options.add_argument(f'--proxy-server={proxy_object}')

        try:
            driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=chrome_options)
            return driver
        except Exception as e:
            print(f"Proxy error: {str(e)}")
            proxies.remove(proxy)

    print("No working proxies available after multiple attempts.")
    return None


def savedataintodatabase(data):
    # db_host = '34.23.87.242'
    # db_port = '3306'
    # db_name = 'cleanster-logs'
    # db_user = 'airbnb_root'
    # db_password = '7BQ+NLokL<L,x@+r'

    # try:
    #     mydb = mysql.connector.connect(
    #         user = db_user,
    #         password=db_password,
    #         host= db_host,
    #         port = db_port,
    #         database=db_name
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
    print("data: {}".format(data))

    
