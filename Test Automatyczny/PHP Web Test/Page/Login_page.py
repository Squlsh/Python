
from Libs.Driver_commands import DriverCommands

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)

    #Elememts

    def login_field(self):
        self.driver_commands.wait_for_element_by_css_selector(".form-control.padding-10")
        return self.driver.find_elements_by_css_selector(".form-control.padding-10")[0]

    def password_field(self):
        return self.driver.find_elements_by_css_selector(".form-control.padding-10")[1]

    def login_button(self):
        self.driver_commands.wait_for_element_by_css_selector(".btn.btn-action.btn-block.loginbtn")
        return self.driver.find_element_by_css_selector(".btn.btn-action.btn-block.loginbtn")

    def admin_login_field(self):
        self.driver_commands.wait_for_element_by_css_selector(".form-control")
        return self.driver.find_elements_by_css_selector(".form-control")[0]

    def admin_password_field(self):
        return self.driver.find_elements_by_css_selector(".form-control")[1]

    def admin_login_button(self):
        self.driver_commands.wait_for_element_by_css_selector(".btn.btn-primary.btn-block.ladda-button.fadeIn.animated")
        return self.driver.find_element_by_css_selector(".btn.btn-primary.btn-block.ladda-button.fadeIn.animated")

    #Actions

    def fill_login_field(self, text):
        self.login_field().send_keys(text)

    def fill_password_field(self, text):
        self.password_field().send_keys(text)

    def click_login_button(self):
        self.login_button().click()

    def fill_admin_login_field(self, text):
        self.admin_login_field().send_keys(text)

    def fill_admin_password_field(self, text):
        self.admin_password_field().send_keys(text)

    def click_admin_login_button(self):
        self.admin_login_button().click()

    #Functions

    def login(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.click_login_button()

    def admin_login(self, login, password):
        self.fill_admin_login_field(login)
        self.fill_admin_password_field(password)
        self.click_admin_login_button()

