from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Remote(
        command_executor=f"http://localhost:4646/wd/hub", options=options)

    driver.get("https://google.com")

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"
    print(value)
    driver.quit()


test_eight_components()
