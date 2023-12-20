from selenium import webdriver
from selenium.webdriver.common.by import By



# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


no_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text

print(no_of_articles)

# Closes browser
driver.quit()