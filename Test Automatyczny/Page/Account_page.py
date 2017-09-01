from Libs.Driver_commands import DriverCommands

class AccountPage():                #potwierdzenie logowania
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)

    def check_login_result(self):
        self.driver_commands.wait_for_element_by_css_selector(".RTL")
        JohnSmithText = self.driver.find_elements_by_css_selector(".RTL")[1]
        if JohnSmithText.text == 'Hi, John Smith':
            return True
        return False

    def check_invalid_login_result(self):
        self.driver_commands.wait_for_element_by_css_selector(".alert.alert-danger")
        InvalidEmailOrPasswordText = self.driver.find_element_by_css_selector(".alert.alert-danger")
        if InvalidEmailOrPasswordText.text == 'Invalid Email or Password':
            return True
        return False