import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
PATH = "/root/.wdm/drivers/chromedriver/linux64/101.0.4951.41"
driver = webdriver.Chrome(service=Service(PATH))

# PATH = "/Users/sanjana/chromedriver"

# driver = webdriver.Chrome()

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
