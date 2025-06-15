from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ewangmart(driver, base_url, product_id): 
    driver.get(base_url+product_id)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#wrap > main > section.detail-viewed-section > div > div.detail-txt-wrap > p.title.type2'))
    )

    product_name = driver.find_element(By.CSS_SELECTOR, '#wrap > main > section.detail-viewed-section > div > div.detail-txt-wrap > p.title.type2').text 
    price_plain = driver.find_element(By.CSS_SELECTOR, '#wrap > main > section.detail-viewed-section > div > div.detail-txt-wrap > p.price.type2 > span.discount').text 
    price_coupon = driver.find_element(By.CSS_SELECTOR, '#wrap > main > section.detail-viewed-section > div > div.detail-txt-wrap > p.price.type2 > span.discount'
    ).text

    return product_name, price_plain, price_coupon
