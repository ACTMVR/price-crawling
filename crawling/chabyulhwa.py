from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chabyulhwa(driver, base_url, product_id): 
    driver.get(base_url+product_id)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list-item-info-title'))
    )

    product_name = driver.find_element(By.CSS_SELECTOR, '.product-list-item-info-title').text 
    price_plain = driver.find_element(By.CSS_SELECTOR, '.product-list-item-info-discounted-price').text 
    price_coupon = driver.find_element(By.CSS_SELECTOR, '.product-list-item-info-discounted-price').text

    return product_name, price_plain, price_coupon

