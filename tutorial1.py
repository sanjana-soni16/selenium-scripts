import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# PATH = "/Users/sanjana/chromedriver"

print("Path : ",os.path)
driver = webdriver.Chrome(service=Service(os.path))

# driver = webdriver.Chrome(service=Service(PATH))

driver.get("https://www.google.com")

driver.title  # => "Google"

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

driver.quit()
