# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv 
 
driver_path = './chromedriver'
 
service = webdriver.ChromeService(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
 
data = [
    ['id', 'product_category', 'name', 'base_url', 'product_id'],
    ['1', '닭 정육', 'coupang', 'https://www.coupang.com/vp/products/', '7141699226']
]

driver.get('https://www.coupang.com/vp/products/7141699226')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# li_elements= driver.find_elements(By.TAG_NAME, 'li')

# for li_element in li_elements:
#     try:
#         a_tag = li_element.find_element(By.TAG_NAME, 'a')
#         href = a_tag.get_attribute('href')
#         print(href)
#     except:
#         # li 안에 a 태그가 없는 경우 예외 처리
#         continue
# search_box = driver.find_element_by_xpath('//*[@id="google_search"]')

