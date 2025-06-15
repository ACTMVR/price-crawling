# chrome driver 세팅  
from selenium import webdriver
driver_path = '../chromedriver'

service = webdriver.ChromeService(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

# 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://www.foodspring.co.kr/goods/detail/654981')
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

product_name = driver.find_element(By.CSS_SELECTOR, '.title-b-18').text 
price_plain = driver.find_element(By.CSS_SELECTOR, '.title-b-24').text 
price_coupon = driver.find_element(
    By.CSS_SELECTOR,
    '.flex.items-baseline.body-b-24.text-benefit-solid.gap-0\\.5 > div'
).text

from datetime import datetime
now = datetime.now()

print(product_name, price_plain, price_coupon, now.strftime('%Y-%m-%d'))

# from selenium.webdriver.common.keys import Keys

