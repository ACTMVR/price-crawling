from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def baemin(driver, base_url, product_id): 
    driver.get(base_url+product_id)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[2]/div'))
    )

    product_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[2]/div').text 
    price_plain = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[4]/div/div[1]/span[2]').text 
    price_coupon = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[1]/section/div[2]/section[1]/div[4]/div/div[2]/div[1]/span[1]'
    ).text

    return product_name, price_plain, price_coupon
