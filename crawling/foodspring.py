from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def foodspring(driver, base_url, product_id): 
    driver.get(base_url+product_id)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.title-b-18'))
    )

    product_name = driver.find_element(By.CSS_SELECTOR, '.title-b-18').text 
    price_plain = driver.find_element(By.CSS_SELECTOR, '.title-b-24').text 
    price_coupon = driver.find_element(
        By.CSS_SELECTOR,
        '.flex.items-baseline.body-b-24.text-benefit-solid.gap-0\\.5 > div'
    ).text

    return product_name, price_plain, price_coupon

