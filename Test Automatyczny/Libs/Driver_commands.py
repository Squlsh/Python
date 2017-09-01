import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverCommands():

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element_by_css_selector(self, element):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_element_by_xpath(self, element):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))

    def return_url(self):
        return self.driver.current_url

    def wait_for_page_to_load(self):
        time.sleep(5)