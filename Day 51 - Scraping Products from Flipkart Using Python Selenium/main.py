from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)

close_login_modal_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/span')
close_login_modal_btn.click()

def search_product():
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("mobile phone under 10000")
    Submit = driver.find_element(
        By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
    sleep(2)
    Submit.click()

search_product()


def get_product_list():
    products = []
    nav_items = driver.find_elements(By.CSS_SELECTOR, '.yFHi8N .ge-49M')

    for index in range(9):
        product_names = driver.find_elements(By.CSS_SELECTOR, "._1AtVbE .col-7-12 ._4rR01T")
        product_prices = driver.find_elements(By.CSS_SELECTOR, "._1AtVbE .col-5-12 ._30jeq3")

        for i in range(len(product_prices)):
            products.append({'product_name': product_names[i].text, 'price': product_prices[i].text})
        
        nav_items[index+1].click()
        sleep(2)
    return products

products = get_product_list()

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(products)

print(df)

# Save the DataFrame to a CSV file
df.to_csv('mobiles_under_10000.csv', index=False)

driver.quit()