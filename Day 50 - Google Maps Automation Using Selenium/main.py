from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/maps/@18.5160028,73.8301434,15z?entry=ttu")
sleep(2)


def searchplace():
    Place = driver.find_element(By.NAME, "q")
    Place.send_keys("Ayodhya")
    Submit = driver.find_element(
        By.XPATH, '//*[@id="searchbox-searchbutton"]')
    Submit.click()


searchplace()


def directions():
    sleep(10)
    directions = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/div')
    directions.click()


directions()


def find():
    sleep(6)
    find = driver.find_element(By.XPATH, '//*[@id="sb_ifc50"]/input')
    find.send_keys("Pune")
    sleep(2)
    search = driver.find_element(By.XPATH, '//*[@id="directions-searchbox-0"]/button[1]')
    search.click()


find()


def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)
    Bus = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[1]')
    print("Bus Travel:", Bus.text)
    sleep(7)
    Bike = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[1]')
    print("Bike Travel:", Bike.text)
    sleep(7)


kilometers()
driver.quit()