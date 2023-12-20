from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


events = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget li")

python_upcoming_events = {}

for index, value in enumerate(events):
    python_upcoming_events[index] = {'time': value.text.split(
        "\n")[0], 'name': value.text.split("\n")[1]}

print("Python Upcoming Events: ", python_upcoming_events)

# Closes current tab
# driver.close()

# Closes browser
driver.quit()
