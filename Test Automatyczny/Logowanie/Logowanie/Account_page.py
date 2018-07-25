from Libs.Driver_commands import DriverCommands
from Page.Login_page import LoginPage
from Libs.Driver_helpers import DriverHelpers


class AccountPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)
        self.driver_helpers = DriverHelpers(self.driver)
        self.login_page = LoginPage(self.driver)

    def check_login_result(self, testName):
        self.login_page.log_result()
        self.driver_commands.wait_for_element_by_css_selector("div.ng-binding")
        CorectEmailOrPasswordText = self.driver.find_element_by_css_selector("div.ng-binding")
        if CorectEmailOrPasswordText.text == "Logged in as : testowy":
            return True
        self.driver_helpers.save_screenshot(testName)
        self.driver.get("https://10.4.11.244:5601/logout")
        return False


    def check_admin_login_result(self, testName):
        self.login_page.log_result()
        self.driver_commands.wait_for_element_by_css_selector(".container > div:nth-child(1)")
        CorectEmailOrPasswordText = self.driver.find_element_by_css_selector(".container > div:nth-child(1)")
        if CorectEmailOrPasswordText.text == "Logged in as : logserver":
            return True
        self.driver_helpers.save_screenshot(testName)
        self.driver.get("https://10.4.11.244:5601/logout")
        return False

    def check_invalid_login_result(self, testName):
        self.driver_commands.wait_for_element_by_css_selector("#kibanaLoginForm > h4:nth-child(4)")
        InvalidEmailOrPasswordText = self.driver.find_element_by_css_selector("#kibanaLoginForm > h4:nth-child(4)")
        if InvalidEmailOrPasswordText.text == "Invalid username or password":
            return True
        self.driver_helpers.save_screenshot(testName)
        self.driver.get("https://10.4.11.244:5601/logout")
        return False
