# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"} 

# @app.post("/product-list")
# async def price_list(): 
     

# chrome driver 세팅  
from selenium import webdriver
driver_path = './chromedriver'

service = webdriver.ChromeService(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36')
options.add_argument('--lang=ko-KR')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
)

from crawling.foodspring import foodspring 
from crawling.baemin import baemin 
from crawling.chabyulhwa import chabyulhwa 
from crawling.orderplus import orderplus 
from crawling.ewangmart import ewangmart 
import csv

import uuid
import requests, json
# URL = "https://google.com"

# # data with json
# data = {"outer": {"inner": "value"}}
# response = requests.post(URL, data=data)
# response = requests.post(URL, data=json.dumps(data))

# # json
# response = requests.post(URL, json={"name": "test"})

# # files
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
# 출처: https://light-tree.tistory.com/6 [All about:티스토리]


from datetime import datetime
now = datetime.now()

# 랜덤 UUID 생성

with open('product_list.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # 각 행이 리스트 형태로 출력됨
        product_name, price_plain, price_coupon = globals()[row['platform']](driver, row['base_url'], row['product_id'])
        random_uuid = uuid.uuid4()
        data = {
            'id': random_uuid,
            'product': row['product'],
            'platform': row['platform'],
            'product_name': product_name,
            'price_plain': price_plain,
            'price_coupon': price_coupon,
            'date': now.strftime('%Y-%m-%d')
        }
        response = requests.post('https://hooks.zapier.com/hooks/catch/19458092/uy2z3ad/', data=data)
        print(product_name, price_plain, price_coupon)

