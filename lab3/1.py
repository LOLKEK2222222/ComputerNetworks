import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SCROLL_AMOUNT = 2000

def collect_data_from_page(page_url):
    driver.get(page_url)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(f"window.scrollBy(0, {SCROLL_AMOUNT});")

        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__link")))
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "price__lower-price")))

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
    phone_elements = driver.find_elements(By.CLASS_NAME, "product-card__link")
    price_elements = driver.find_elements(By.CLASS_NAME, "price__lower-price")
    rating_elements = driver.find_elements(By.CLASS_NAME, "address-rate-mini--sm")
    number_of_ratings = driver.find_elements(By.CLASS_NAME, "product-card__count")

    phone_names = [element.get_attribute("aria-label") for element in phone_elements]
    phone_prices = [element.text for element in price_elements]
    phone_ratings = [element.text for element in rating_elements]
    phone_number_of_ratings = [element.text for element in number_of_ratings]

    return zip(phone_names, phone_prices, phone_ratings, phone_number_of_ratings)

driver = webdriver.Chrome()
base_url = "https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=popular&page="
num_pages = 2

with open('phones.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Название телефона', 'Цена', 'Рейтинг', 'Количество оценок'])
    
    for page in range(1, num_pages + 1):
        url = base_url + str(page)
        data = collect_data_from_page(url)
        for row in data:
            writer.writerow(row)
        writer.writerow([])

driver.quit()
