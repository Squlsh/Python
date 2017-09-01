from Libs.Driver_commands import DriverCommands

class AdminPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)

    def check_id_result(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[3]")
        IdText = self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[3]")
        if IdText.text == '47':
            return True
        return False

    def check_ref_no_result(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[4]")
        RefNoText = self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[4]")
        if RefNoText.text == '7504':
            return True
        return False

    def check_customer_result(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]")
        CustomerText = self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]")
        if CustomerText.text == 'John':
            return True
        return False
