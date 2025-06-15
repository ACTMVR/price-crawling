# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from selenium.webdriver.common.by import By

import csv 
 
driver_path = './chromedriver'
 
service = webdriver.ChromeService(executable_path=driver_path)
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36')
options.add_argument('--lang=ko-KR')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-http2')

driver = webdriver.Chrome(service=service, options=options)
 
driver.get("https://www.coupang.com/vp/products/7141699226")

driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
)


# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv 

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

product_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[2]/div').text 
price_plain = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[4]/div/div[1]/span[2]').text 
price_coupon = driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[4]/div/div[2]/div[1]/span[1]'
).text

from datetime import datetime
now = datetime.now()

print(product_name, price_plain, price_coupon, now.strftime('%Y-%m-%d'))


