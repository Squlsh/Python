
class MainPage():
    def __init__(self, driver):
        self.driver = driver

    #Elements

    def main_button(self):
        main_button = self.driver.find_elements_by_css_selector(".dropdown-toggle")[1]
        return main_button

    def login_button(self):
        login_button = self.driver.find_elements_by_css_selector(".dropdown-menu>li>a")[11]
        return login_button

    #Action

    def click_main_button(self):
        self.main_button().click()

    def click_login_button(self):
        self.login_button().click()
