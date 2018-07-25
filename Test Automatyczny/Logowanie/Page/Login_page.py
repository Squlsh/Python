
from Libs.Driver_commands import DriverCommands

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)


    #Elememts

    def login_field(self):
        self.driver_commands.wait_for_element_by_css_selector("input.form-control:nth-child(5)")
        return self.driver.find_element_by_css_selector("input.form-control:nth-child(5)")

    def password_field(self):
        return self.driver.find_element_by_css_selector("input.form-control:nth-child(7)")

    def login_button(self):
        self.driver_commands.wait_for_element_by_css_selector(".btn")
        return self.driver.find_element_by_css_selector(".btn")

    def option_field(self):
        self.driver_commands.wait_for_element_by_css_selector(".fa-th")
        return self.driver.find_element_by_css_selector(".fa-th")

    def option_button(self):
        self.driver_commands.wait_for_element_by_css_selector(".fa-th")
        return self.driver.find_element_by_css_selector(".fa-th")

    def config_field(self):
        self.driver_commands.wait_for_element_by_css_selector("div.app-link:nth-child(2) > a:nth-child(1) > div:nth-child(1)")
        return self.driver.find_element_by_css_selector("div.app-link:nth-child(2) > a:nth-child(1) > div:nth-child(1)")

    def config_button(self):
        self.driver_commands.wait_for_element_by_css_selector("div.app-link:nth-child(2) > a:nth-child(1) > div:nth-child(1)")
        return self.driver.find_element_by_css_selector("div.app-link:nth-child(2) > a:nth-child(1) > div:nth-child(1)")

    #Actions

    def fill_login_field(self, text):
        self.login_field().send_keys(text)

    def fill_password_field(self, text):
        self.password_field().send_keys(text)

    def click_login_button(self):
        self.login_button().click()

    def click_option_button(self):
        self.option_button().click()

    def click_config_button(self):
        self.config_button().click()

    #Functions

    def login(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.click_login_button()

    def log_result(self):
        self.click_option_button()
        self.click_config_button()
