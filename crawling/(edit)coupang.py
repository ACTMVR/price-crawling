# chrome driver 세팅  
from selenium import webdriver
driver_path = './chromedriver'

service = webdriver.ChromeService(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.coupang.com/vp/products/7141699226')


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def foodspring(driver, base_url, product_id): 
#     driver.get(base_url+product_id)
#     WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "body"))
#     )

#     product_name = driver.find_element(By.CSS_SELECTOR, '.title-b-18').text 
#     price_plain = driver.find_element(By.CSS_SELECTOR, '.title-b-24').text 
#     price_coupon = driver.find_element(
#         By.CSS_SELECTOR,
#         '.flex.items-baseline.body-b-24.text-benefit-solid.gap-0\\.5 > div'
#     ).text

#     return product_name, price_plain, price_coupon
