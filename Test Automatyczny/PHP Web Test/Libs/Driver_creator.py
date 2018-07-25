from selenium import webdriver

def create_driver():
    driver = webdriver.Firefox()
    return driver


def create_drivers_parametrize(browser):
    if browser == "Firefox":
        driver = webdriver.Firefox()
    if browser == "Chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    return driver



