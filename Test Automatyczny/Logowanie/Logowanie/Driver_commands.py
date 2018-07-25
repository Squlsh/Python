
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Libs.Driver_helpers import DriverHelpers


class DriverCommands():

    def __init__(self, driver):
        self.driver = driver
        self.driver_helpers = DriverHelpers(self.driver)

    def open_page(self, URL):
        self.driver.get(URL)

    def wait_for_element_by_css_selector(self, element):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

