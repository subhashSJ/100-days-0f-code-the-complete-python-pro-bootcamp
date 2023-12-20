from selenium import webdriver
from selenium.webdriver.common.by import By



# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("subhash")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("jadhav")

email = driver.find_element(By.NAME, "email")
email.send_keys("subhash@gamil.com")

signup_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
signup_btn.click()

# Closes browser
# driver.quit()