import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_binary

from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())

# options = webdriver.ChromeOptions()
# options.headless = False
# driver = webdriver.Remote(
#     command_executor=f"http://localhost:4444/wd/hub", options=options)
driver = webdriver.Chrome(service=service)

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
